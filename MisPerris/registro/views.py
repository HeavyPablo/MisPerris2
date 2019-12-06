from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import ProfileForm, ExtendedUserCreationForm, RescatadoForm
from .models import Rescatado

# Create your views here.
# def registro_mascota(request):
#   posts = PostAnimal.objects.all()
#  return render(request, 'registro/registro_mascota.html', {'posts': posts})


def home(request):
    return render(request, 'registro/home.html', {})


def register(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST or None)

        if profile_form.is_valid() and form.is_valid():
            user = form.save()

            profile = profile_form.save(commit=False)
            profile.usuario = user

            profile.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            _user = authenticate(username=username, password=password)
            login(request, _user)

            return redirect('home')
    else:
        form = ExtendedUserCreationForm()
        profile_form = ProfileForm()

    context = {
        'form': form,
        'profile_form': profile_form
    }
    return render(request, 'registro/register.html', context)


@login_required
def rescatadoView(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = RescatadoForm(request.POST, request.FILES)

        if form.is_valid():
            form = form.save(commit=False)
            form.autor = request.user
            form.save()
            return redirect('home')

    else:
        form = RescatadoForm()

    context = {
        'form': form,
    }
    return render(request, 'registro/register_pet.html', context)

def petListview(request):
    pets = Rescatado.objects.filter().order_by('id')

    paginator = Paginator(pets, 3)

    page = request.GET.get('page', 1)

    try:
        pets = paginator.page(page)
    except PageNotAnInteger:
        pets = paginator.page(1)
    except EmptyPage:
        pets = paginator.page(paginator.num_pages)

    context = {
        'pets': pets,
    }
    return render(request, 'registro/listview_pet.html', context)
