from tkinter import Widget
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class archivo(forms.Form):

    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    profesion = forms.CharField(max_length=40)
    titulo= forms.CharField(max_length=40) #str corto
    cuerpo = forms.CharField()
    fecha = forms.DateField()
    adjunto = forms.URLField()
    autor = forms.CharField(max_length=40) # str corto


class UserEditForm(UserCreationForm):
    
    email = forms.EmailField(label="Modificar")
    password1 = forms.CharField(label="Contraseña" , widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña" , widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email' , 'password1' , 'password2']
        help_text = {k:"" for k in fields}

class archivo(forms.Form):

    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    profesion = forms.CharField(max_length=40)
    titulo= forms.CharField(max_length=40) #str corto
    cuerpo = forms.CharField()
    fecha = forms.DateField()
    adjunto = forms.URLField()
    autor = forms.CharField(max_length=40) # str corto

class Mensaje_formulario (forms.Form):
    nombre = forms.CharField(max_length=40)
    email = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)


