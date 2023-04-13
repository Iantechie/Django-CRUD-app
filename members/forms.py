from django import forms
from django.contrib.auth.models import User


class NewUser(forms.ModelForm):
    password = forms.CharField(label='Password',widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'email')
       
        


