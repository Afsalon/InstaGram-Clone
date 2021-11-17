from django.urls import path
from core import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('feed/', login_required(views.HomeFeedView.as_view()), name='home_feed_page'),
    path('follow/', login_required(views.FollowView.as_view()), name='follow_page'),
    path('unfollow/', login_required(views.UnFollowView.as_view()), name='unfollow_page'),
    path('<str:username>/', login_required(views.ProfileView.as_view()), name ='user_profile_page'),
    path('<str:username>/edit/<int:pk>/', login_required(views.ProfileEditView.as_view()), name='profile_edit_page'),
    path('profile/search/', login_required(views.ProfileSearchView.as_view()), name='user_search_page'),
    path('create/newpost/', login_required(views.CreatePostView.as_view()), name='create_post_page'),
    path('post/detail/<int:pk>/',login_required(views.DetailPostView.as_view()), name='detail_post_page'),
    path('post/delete/<int:pk>/',login_required(views.DeletePostView.as_view()), name='delete_post_page'),
    path('like/done/<int:pk>/', login_required(views.LikeDoneView.as_view()), name='like_done_page'),
    path('unlike/done/<int:pk>/', login_required(views.UnlikeDoneView.as_view()), name='unlike_done_page'),
    path('comment/done/<int:pk>/', login_required(views.CommentDoneView.as_view()), name='comment_done_page'),
    path('comment/undone/<int:pk>/<commentedon>', login_required(views.CommentUndoneView.as_view()), name='comment_undone_page'),
    # path('saved/post/<int:pk>/',login_required(views.SavedPostView.as_view()), name='saved_post_page')
]
