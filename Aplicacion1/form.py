from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User
from Aplicacion1.models import avatar


#class login(forms.Form):

    #nombre = forms.CharField(max_length=30)
    #contra = forms.CharField(max_length=30)


class UsuarioRegistro(UserCreationForm):

    email = forms.EmailField()
    
    password1 =  forms.CharField(label= "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label= "Repetir la Contraseña", widget=forms.PasswordInput)
    

    class Meta:

        model = User
        fields = ["username","email","first_name", "last_name", "password1", "password2"]

class FormularioEditar(UserCreationForm):

    email = forms.EmailField()
    password1 =  forms.CharField(label= "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label= "Repetir la Contraseña", widget=forms.PasswordInput)
    

    class Meta:

        model = User
        fields = ["email","first_name", "last_name", "password1", "password2"]


class AvatarFormulario(forms.ModelForm):

    class Meta:

        model = avatar
        fields = [ "imagen"]



class Avatarformulario(forms.Form):

    class Meta:

        model = avatar
        fields = ["user" , "imagen"]
        