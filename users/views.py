import random
import string

from django.conf import settings
from django.contrib.auth.views import LoginView as BaseLoginView, PasswordResetView, PasswordResetConfirmView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, UserForm, UserForgotPasswordForm, UserSetNewPasswordForm
from users.models import User

import secrets


class LoginView(BaseLoginView):
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'

    def get_success_url(self):
        return reverse('users:login')

    def form_valid(self, form):
        host = self.request.get_host()
        token = secrets.token_hex(10)
        user = form.save()
        user.token = token
        user.is_active = False
        user.save()
        link = f'http://{host}/users/confirm_register/{token}'
        message = f"Добро пожаловать на наш сайт. Для авторизации, подтвердите адрес электронной почты. {link}"
        send_mail('Верификация почты', message, settings.EMAIL_HOST_USER, [user.email,])
        return super().form_valid(form)


def confirm_email(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


class UserUpdateView(UpdateView):
    model = User
    success_url = reverse_lazy('users:profile')
    form_class = UserForm

    def get_object(self, queryset=None):
        return self.request.user


class UserForgotPasswordView(SuccessMessageMixin, PasswordResetView):

    form_class = UserForgotPasswordForm
    template_name = 'users/user_password_reset.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Письмо с инструкцией по восстановлению доступа отправлено на ваш email'
    subject_template_name = 'users/email/password_subject_reset_mail.txt'
    email_template_name = 'users/email/password_reset_mail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Запрос на восстановление пароля'
        return context


class UserPasswordResetConfirmView(SuccessMessageMixin, PasswordResetConfirmView):

    form_class = UserSetNewPasswordForm
    template_name = 'users/user_password_set_new.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Пароль успешно изменен. Можете авторизоваться на сайте.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Установить новый пароль'
        return context
