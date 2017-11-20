from django import forms
from django.contrib.auth.models import User

from .models import Mensagem



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())




class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class MensagemForm(forms.ModelForm):
    

    class Meta:
        model = Mensagem
        fields = ('memorando',)

   