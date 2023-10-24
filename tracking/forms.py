from django import forms
from django.contrib.auth.models import User
from .models import DockerUser

class LoginForm(forms.ModelForm):
    Email = forms.EmailField(widget=forms.TextInput(attrs={'class':"form-control"}))
    UserName = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    Password = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control","type":"password"}))
    class Meta:
        model = DockerUser
        fields = '__all__'