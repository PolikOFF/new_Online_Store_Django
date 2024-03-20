from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm, SetPasswordForm
from django import forms

from catalog.forms import StyleForMixin
from users.models import User


class UserRegisterForm(StyleForMixin, UserCreationForm):
    """Изменения стиля формы создания"""
    class Meta:
        """Выбор модели и полей регистрации"""
        model = User
        fields = ('email', 'password1', 'password2')


class UserForm(StyleForMixin, UserChangeForm):
    """Обновление стиля формы редактирования"""
    class Meta:
        """Выбор модели и добавление слов-исключений"""
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'phone', 'avatar', 'country')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()


class UserForgotPasswordForm(PasswordResetForm):
    """
    Запрос на восстановление пароля
    """
    def __init__(self, *args, **kwargs):
        """
        Обновление стилей формы
        """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })


class UserSetNewPasswordForm(SetPasswordForm):
    """
    Изменение пароля пользователя после подтверждения
    """
    def __init__(self, *args, **kwargs):
        """
        Обновление стилей формы
        """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })
