from django.db import models
# Create your models here.

class UserAccount(models.Model):
    name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    nick_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(verbose_name='E-mail')

    def __str__(self):
        return self.name
