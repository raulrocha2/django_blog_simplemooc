import re
from django.db import models
from django.core import validators
from django.contrib.auth.models import (AbstractBaseUser, UserManager, 
    PermissionsMixin)

class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(
        'Nome do Usuário', max_length=30, unique=True,
        validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'),
        'O Nome do usuario pode conter letras, numeros ou @ /. + - _', 'invalid')]
    )
    email = models.EmailField('E-mail', unique=True)
    name = models.CharField('Nome', max_length=100, blank=True)
    is_staff = models.BooleanField('É da Equipe?', blank=True, default=False)
    is_active = models.BooleanField('Esta Ativo?', blank=True, default=True)
    date_joined = models.DateTimeField('Data de  Entrada', auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.name or self.username

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return str(self)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'