from django.contrib.auth.models import User
from django.db import models
# Create your models here.


class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_photo = models.ImageField(upload_to='userphoto/')
