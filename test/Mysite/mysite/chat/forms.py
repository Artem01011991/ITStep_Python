from django import forms

class RegistrationForm(forms.Form):
    name = forms.CharField(max_length=20)
    second_name = forms.CharField(max_length=20)
    nick_name = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, max_length=100)
    repassword = forms.CharField(widget=forms.PasswordInput, max_length=100)
    email = forms.EmailField(widget=forms.EmailInput, label='E-mail')