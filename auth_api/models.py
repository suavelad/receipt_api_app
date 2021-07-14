import sys
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from six import BytesIO
from .manager import CustomUserManager


class User(AbstractUser):
    SEX = (
        ('male','Male'),
        ('female','Female')
    )
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False, blank=True, null=True)
    is_admin = models.BooleanField(default=False, blank=True, null=True)
    is_active = models.BooleanField(default=False, blank=True)
    sex = models.CharField(max_length=7, choices=SEX, null=True, blank=True)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=11, null=True, blank=True)
    time_created = models.TimeField(auto_now_add=True)
    date_created = models.DateField(auto_now_add=True)



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()


    def __str__(self):
        return self.username