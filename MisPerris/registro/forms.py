from django import forms

from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import HttpResponseRedirect

from .models import Profile, Rescatado

class Login(auth_views.LoginView):
    def form_valid(self, form):
        login(self.request, form.get_user())
        self.request.session['username'] = self.request.POST['username']
        return HttpResponseRedirect(self.get_success_url())

class ExtendedUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )

        labels = {
            'username': 'Nombre de Usuario',
            'email': 'Email',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'password1': 'Contraseña',
            'password2': 'Confirmar Contraseña',
        }

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'type': 'email'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'rut',
            'fechanacimiento',
            'telefono',
            'region',
            'ciudad',
            'tipovivienda',
        )

        labels = {
            'rut': 'Rut',
            'fechanacimiento': 'Fecha de Nacimiento',
            'telefono': 'Teléfono',
            'region': 'Región',
            'ciudad': 'Ciudad',
            'tipovivienda': 'Tipo de Vivienda',
        }

        widgets = {
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'fechanacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control'}),
            'region': forms.Select(attrs={'class': 'custom-select'}),
            'ciudad': forms.Select(attrs={'class': 'custom-select'}),
            'tipovivienda': forms.Select(attrs={'class': 'custom-select'}),
        }

class RescatadoForm(forms.ModelForm):
    class Meta:
        model = Rescatado
        fields = (
            'imagen',
            'nombre',
            'raza',
            'descripcion',
            'estado',
        )

        labels = {
            'imagen': 'Imagen',
            'nombre': 'Nombre Mascota',
            'raza': 'Raza Mascota',
            'descripcion': 'Descripción',
            'estado': 'Estado',
        }

        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'raza': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'estado': forms.Select(attrs={'class': 'custom-select'}),
        }
