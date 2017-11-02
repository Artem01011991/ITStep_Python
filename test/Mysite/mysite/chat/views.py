from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import UserAccount
from .forms import RegistrationForm
# Create your views here.

def registration_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/userpage/')
    else:
        form = RegistrationForm()
    return render(request, 'register_page.html', {'form': form})


def user_page(request):
    return render(request, 'chat/userpage.html')

def users_online(request):
    UO_amount = UserAccount.objects.count()
    response = {'amount':UO_amount}
    return render(request, 'chat/count_users.html', response)
