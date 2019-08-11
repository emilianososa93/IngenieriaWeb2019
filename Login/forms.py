from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm


class RegisterForm(forms.Form):
    usuario = forms.CharField(max_length=20, label='Usuario')
    nombre = forms.CharField(max_length=30, label='Nombre')
    apellido = forms.CharField(max_length=20, label='Apellido')
    email = forms.EmailField(max_length=50,label='Email')
    contraseña = forms.CharField(label='Contraseña',widget=forms.PasswordInput(attrs={'class' : 'validate'}))
    confirmarcontraseña = forms.password=forms.CharField(label='Repetir contraseña',widget=forms.PasswordInput(attrs={'class' : 'validate'}))
    
class LoginForm(forms.Form):
    username =forms.CharField(label='Usaurio')
    password = password= forms.password=forms.CharField(max_length=30, label='Password',widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Ingrese su clave','required':''}))
