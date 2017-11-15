from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$', views.user_page, name='userpage'),
    url(r'login/$', login, {'template_name': 'chat/log-in.html'}, name='login'),
]
