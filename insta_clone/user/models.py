from django.db import models
from django.contrib.auth.models import AbstractUser
from user.managers import CustomUserManager
# Create your models here.
class User(AbstractUser):
    profile_pic = models.ImageField(upload_to='profile_pic',blank=True,null=True)
    full_name=models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    website = models.URLField(blank=True,null=True)
    bio = models.TextField( max_length=100, blank=True,null=True)
    gender = models.CharField(max_length=20, blank=True,null=True)
    phone_number = models.IntegerField(blank=True,null=True)
    first_name=None
    last_name=None

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['full_name','username']

    objects=CustomUserManager()

    def __str__(self):
        return self.email
