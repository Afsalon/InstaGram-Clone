from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import View,ListView,View,TemplateView,DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy,reverse
from core.forms import EditForm,CreatePostForm
from django.db.models import Q
from core.models import Post,Like,Comment,Follow
User = get_user_model()
# Create your views here.
class HomeFeedView(View):
    template_name='core/homefeed.html'
    def get(self, request, *args, **kwargs):
        all_posts=Post.objects.all()
        return render(request, self.template_name,{'all_posts':all_posts})

class ProfileView(View):
    template_name='core/profile.html'
    def get(self,request,*args,**kwargs):
        username = kwargs.get('username')
        try:
            user = User.objects.get(username=username)
        except:
            return HttpResponse('<h1>This user does not exist</h1>')

        is_follow = False
        try:
            found=Follow.objects.get(user=request.user, follow=user)
            is_follow = True
        except Exception as e:
            pass

        return render(request,'core/profile.html',{'user':user,'is_follow':is_follow})

class ProfileEditView(UpdateView):
    # template_name = 'core/profile_edit.html'
    # model = User
    # fields = ('full_name', 'username','email','profile_pic','website','bio','phone_number','gender')
    #
    #
    # def get_success_url(self):
    #     return reverse('user_profile_page', kwargs={'username':self.request.user.username})
    form_class = EditForm
    model = User
    template_name = 'core/profile_edit.html'
    def get(self, request, *args, **kwargs):
        username = kwargs.get('username')
        if username != request.user.username:
            return HttpResponse(str('This page does not exist'))

        form = self.form_class(instance=request.user)
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            form.save()
            # messages.success(request, 'Saved your details in a safe place.')
            return redirect('user_profile_page', username=request.user.username)

            # return reverse_lazy('user_profile_page', username=request.user.username)
        else:
            messages.error(request,'Looks like either username is not unique or something is entered wrongly')
            return render(request, self.template_name)

class ProfileSearchView(View):
    template_name='core/user_search.html'
    def post(self,request, *args, **kwargs):
        query=request.POST.get('searchbox')
        instagrammer=User.objects.filter(Q(username__contains=query)| Q(full_name__contains=query)).exclude(username__iexact=request.user.username)
        return render(request,self.template_name,{'instagrammer':instagrammer})


class FollowView(View):
    def post(self, request, *args, **kwargs):
        userpk=request.POST.get('userpk')
        followed_user_obj=User.objects.get(pk=userpk)
        try:
            Follow.objects.get(user=request.user, follow=followed_user_obj)
        except Exception as e:
            follow_obj=Follow.objects.create(follow=followed_user_obj)

        return redirect(request.META.get('HTTP_REFERER'))

class UnFollowView(View):
    def post(self, request, *args, **kwargs):
        userpk=request.POST.get('userppk')
        followed_user_obj=User.objects.get(pk=userpk)
        try:
            follow_obj=Follow.objects.get(user=request.user, follow=followed_user_obj)
            follow_obj.delete()
        except Exception as e:
            pass

        return redirect(request.META.get('HTTP_REFERER'))
class CreatePostView(View):
    form_class = CreatePostForm
    model = Post
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        form.save()
        return redirect('home_feed_page')

class DetailPostView(DetailView):
    model=Post
    template_name = 'core/post_detail.html'
    context_object_name = 'pot'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        pkvalue = self.kwargs['pk']
        try:
            Like.objects.get(user=self.request.user,post=pkvalue)
            is_like=True
        except:
            is_like=False
        context['is_like']=is_like
        return context

class DeletePostView(View):
    model=Post
    def post(self, request, *args, **kwargs):
        pkvalue=kwargs.get('pk')
        post_object = self.model.objects.get(pk=pkvalue)
        print(post_object.caption)
        decision=request.POST.get('decision')


        if decision == 'Delete':
            post_object.delete()
            return redirect('home_feed_page')
        else:
            return redirect(request.META.get('HTTP_REFERER'))
class LikeDoneView(View):
    def post(self, request, *args, **kwargs):
        pkvalue = kwargs.get('pk')
        post_obj=Post.objects.get(pk=pkvalue)
        try:
            Like.objects.get(user=request.user, post=post_obj)
        except:
            Like.objects.create(post=post_obj)
            return redirect(request.META.get('HTTP_REFERER'))
        return redirect(request.META.get('HTTP_REFERER'))


class UnlikeDoneView(View):
    def post(self, request, *args, **kwargs):
        pkvalue = kwargs.get('pk')
        post_obj=Post.objects.get(pk=pkvalue)
        try:
            like_object=Like.objects.get(user=request.user, post=post_obj)
            like_object.delete()
        except:
            return redirect(request.META.get('HTTP_REFERER'))
        return redirect(request.META.get('HTTP_REFERER'))

class CommentDoneView(View):
    model = Comment
    def post(self, request,*args, **kwargs):
        pkvalue = kwargs.get('pk')
        post_obj = Post.objects.get(pk=pkvalue)
        comm = request.POST.get('addcomm')
        self.model.objects.create(text=comm,post=post_obj)
        return redirect(request.META.get('HTTP_REFERER'))

class CommentUndoneView(View):
    model = Comment
    def post(self, request,*args, **kwargs):
        pkvalue = kwargs.get('pk')
        commentedon=kwargs.get('commentedon')
        post_obj = Post.objects.get(pk=pkvalue)

        try:
            comm_obj=self.model.objects.get(post=post_obj,commented_on=commentedon)
            comm_obj.delete()
        except:
            return redirect(request.META.get('HTTP_REFERER'))
        return redirect(request.META.get('HTTP_REFERER'))


# class SavedPostView(View):
#     pass
