from django.conf import settings
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, UserForm
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
