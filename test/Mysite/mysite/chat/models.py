from django.contrib.auth.models import User
from django.db.models import ImageField
# Create your models here.

class UserAccount(User):
    user_photo = ImageField(null=True, blank=True)