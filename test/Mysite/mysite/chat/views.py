from django.shortcuts import render
from .models import UserAccount
from .forms import RegistrationForm
# Create your views here.

def registration_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            valid_form = form.cleaned_data


def main(request):
    return render(request, 'chat/temp1.html')

def users_online(request):
    UO_amount = UserAccount.objects.count()
    response = {'amount':UO_amount}
    return render(request, 'chat/count_users.html', response)
