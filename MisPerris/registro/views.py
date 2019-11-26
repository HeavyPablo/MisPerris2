from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .forms import UserProfileForm, ExtendedUserCreationForm

# Create your views here.
# def registro_mascota(request):
#   posts = PostAnimal.objects.all()
#  return render(request, 'registro/registro_mascota.html', {'posts': posts})


def home(request):
    return render(request, 'registro/home.html', {})


def register(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if profile_form.is_valid() and form.is_valid():
            user = form.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            _user = authenticate(username=username, password=password)
            login(request, _user)

            return redirect('home')
    else:
        form = ExtendedUserCreationForm()
        profile_form = UserProfileForm()

    context = {'form': form, 'profile_form': profile_form}
    return render(request, 'registro/register.html', context)
