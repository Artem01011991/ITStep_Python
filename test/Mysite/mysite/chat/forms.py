from django.forms import ModelForm, PasswordInput, ValidationError
from .models import UserAccount

class RegistrationForm(ModelForm):
    class Meta:
        model = UserAccount
        fields = '__all__'
        widgets = {'password': PasswordInput, 'repassword': PasswordInput}

    def clean(self):
        super(RegistrationForm, self).clean()
        pas1 = self.cleaned_data.get('password')
        pas2 = self.cleaned_data.get('repassword')

        if pas1 and pas1 != pas2:
            raise ValidationError(('Passwords do not match!'), code='PasswordError')


    def clean_nick_name(self):
        nn = self.cleaned_data['nick_name']

        for nn_db in UserAccount.objects.values_list('nick_name'):
            if tuple(nn) == nn_db:
                raise ValidationError(('Nickname is already exist.'), code='NicknameError')

        return nn

    def clean_email(self):
        em = self.cleaned_data.get('email')

        try:
            UserAccount.objects.get(email=em)
        except UserAccount.DoesNotExist:
            return em

        raise ValidationError('E-mail is already in use!', code='E-mailError')

