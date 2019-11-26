from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('register_pet', views.rescatadoView, name='register_pet'),
    path('listview_pet', views.petListview, name='listview_pet'),
]
