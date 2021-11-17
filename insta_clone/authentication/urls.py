from django.urls import path
from authentication import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.SigninView.as_view(), name='signin_page'),
    path('signout/', login_required(views.SignoutView.as_view()), name = 'signout_page'),
    path('signup/', views.SignupView.as_view(), name='signup_page'),
    path('password/reset/',views.PRView.as_view(), name='password_reset'),
    path('password/reset/done/',views.PRDone.as_view(), name='password_reset_done'),
    path('password/reset/confirm/<token>/<uidb64>/',views.PRConfirm.as_view(), name='password_reset_confirm'),
    path('password/reset/complete',views.PRComplete.as_view(), name='password_reset_complete'),
    path('password/change/', views.PWDChangeView.as_view(), name="password_change"),
    path('password/change/done/', views.PWDChangeDoneView.as_view(), name="password_change_done"),
]
