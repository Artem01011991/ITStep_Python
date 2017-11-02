from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.user_page),
    url(r'user_count/$', views.users_online)
]