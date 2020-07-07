from django import forms 
from .models import PasswordReset
from simplemooc.core.utils import generate_hash_key
from simplemooc.core.mail import send_mail_template
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model, password_validation
from django.shortcuts import render, redirect

User = get_user_model()


class PasswordResetForm(forms.Form):
    
    error_messages = {
        'password_mismatch': ('E-mail não cadastro!'),
    }

    email = forms.EmailField(label='E-mail')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            return email
        raise forms.ValidationError(
            self.error_messages['password_mismatch']
            )

    def save(self):
        user = User.objects.get(email=self.cleaned_data['email'])
        key = generate_hash_key(user.username)
        reset = PasswordReset(key=key, user=user)
        reset.save()
        template_name = 'accounts/password_reset_mail.html'
        subject = 'Criar Nova senha '
        context = {
            'reset':reset,
        }
        send_mail_template(subject, template_name, context, [user.email])


class RegisterForm(forms.ModelForm):

    #mensagem de Error senha
    error_messages = {
        'password_mismatch': ('Senhas não são iguais.'),
    }

    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Senha', widget=forms.PasswordInput)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                #Chamada var error mensagem
                self.error_messages['password_mismatch']
            )
        return password2

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()
        return user 

    class Meta:
        model = User
        fields = ['username',  'email']

class EditAccountForm(forms.ModelForm):

    
    class Meta:
        model = User
        fields = ['username', 'email', 'name']

