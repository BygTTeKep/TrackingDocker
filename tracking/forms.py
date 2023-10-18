from django import forms
from .models import DockerUser

class LoginForm(forms.ModelForm):
    Email = forms.EmailField(widget=forms.TextInput(attrs={'class':"form-control", "placeholder":"Email"}))
    UserName = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control", "placeholder":"UserName"}))
    Password = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control", "placeholder":"Password", "type":"password"}))
    class Meta:
        model = DockerUser
        fields = '__all__'