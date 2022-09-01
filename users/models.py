from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    def __str__(self):
        return self.user.username

""" #! 👇 Method to append below existing table (POLYMORPHISM)

from django.contrib.auth.models import AbstractUser
from django.db import models
class User(AbstractUser):
    portfolio = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True) """