from django.contrib import admin
# Register your models here.
from .models import UserAccount


class UserAccountAdmin(admin.ModelAdmin):
    list_display = tuple(UserAccount.objects.all())

admin.site.register(UserAccount, UserAccountAdmin)