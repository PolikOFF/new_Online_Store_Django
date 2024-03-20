from django.urls import path

from users.apps import UsersConfig
from users.views import LoginView, LogoutView, RegisterView, confirm_email, UserUpdateView, UserForgotPasswordView, UserPasswordResetConfirmView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('confirm_register/<str:token>/', confirm_email, name='confirm_register'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
    path('password-reset/', UserForgotPasswordView.as_view(), name='password_reset'),
    path('set-new-password/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
