from django.contrib import admin
# Register your models here.
from .models import UserAccount


class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'second_name', 'nick_name','password')

admin.site.register(UserAccount, UserAccountAdmin)