from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetView, PasswordChangeView

app_name = 'users'


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path(
        'login/',
        LoginView.as_view(template_name='users/login.html'),
        name='login'
    ),
    path(
        'logout/',
        LogoutView.as_view(template_name='users/logged_out.html'),
        name='logout'
    ),
    path(
      'password_change/',
      PasswordChangeView.as_view(),
      name='password_change'
    ),
    path(
      'password_reset/',
      PasswordResetView.as_view(),
      name='password_reset'
    )
]
