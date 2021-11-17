from django.shortcuts import render,redirect
from django.views.generic import ListView,View,TemplateView, CreateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse_lazy
from authentication.forms import UserForm
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import (PasswordResetView,PasswordResetDoneView,
                                        PasswordResetConfirmView, PasswordResetCompleteView,
                                        PasswordChangeView, PasswordChangeDoneView,)

# Create your views here.
User = get_user_model()

class SignupView(CreateView):
    template_name= 'authentication/signup.html'
    form_class =UserForm
    success_url = reverse_lazy('signin_page')


    def form_valid(self, form):
        x = form.save(commit=False)
        x.password = make_password(x.password)
        x.save()
        return super().form_valid(form)

class SignoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('signin_page')

class SigninView(View):
        template_name = 'authentication/signin.html'

        def get(self, request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect('home_feed_page')
            return render(request, self.template_name)

        def post(self, request, *args, **kwargs):
            email_username = request.POST.get('email_username')
            password = request.POST.get('password')
            try:
                user_obj = User.objects.get(username=email_username)
                email = user_obj.email
            except:
                email = email_username

            user = authenticate(request, email=email, password=password)

            if user is None:
                messages.error(request,"Password and Username/Email didn't match")
                return render(request, self.template_name)

            login(request, user)
            return redirect('home_feed_page')

class PRView(PasswordResetView):
    template_name='authentication/password_reset.html'

class PRDone(PasswordResetDoneView):
    template_name='authentication/password_reset_done.html'

class PRConfirm(PasswordResetConfirmView):
    template_name='authentication/password_reset_confirm.html'

class PRComplete(PasswordResetCompleteView):
    template_name='authentication/password_reset_complete.html'
class PWDChangeView(PasswordChangeView):
    template_name = 'authentication/password_change.html'
class PWDChangeDoneView(PasswordChangeDoneView):
    template_name = 'authentication/password_change_done.html'
