from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import authenticate , login, logout

def registration_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            # Username and password should be received at raw form
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # Logs in the user for current session
            user = authenticate(request, username=username, password=raw_password)
            login(request, user)

            return redirect('/userpage/')
    # Whether user have authenticated already
    elif request.user.is_authenticated():

        return redirect('/userpage/')
    # Black form have been passed
    else:
        form = RegistrationForm()

    return render(request, 'register_page.html', {'form': form})

def user_page(request):
    if request.method == 'POST':
        logout(request)

        return redirect(r'^login/')

    if not request.user.is_authenticated():

        return redirect(r'^login/')

    return render(request, 'chat/userpage.html')



