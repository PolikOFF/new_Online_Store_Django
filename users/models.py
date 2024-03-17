from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


class User(AbstractUser):
    username = None
    phone = models.CharField(max_length=50, verbose_name='номер телефона', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватарка', **NULLABLE)
    country = models.CharField(max_length=100, verbose_name='страна', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='email')

    token = models.CharField(max_length=30, verbose_name='токен', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
