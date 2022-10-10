from enum import unique
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator
from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length = 255, unique = True)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    # password = models.CharField(validators=[
    #         MinLengthValidator(8, 'the field must contain at least 8 characters')
    #         ], max_length = 255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email