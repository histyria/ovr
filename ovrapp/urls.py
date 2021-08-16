from django.urls import path, include
from . import views
from .views import create


urlpatterns = [
    path('', views.create , name= "create"),
    path('home/', views.home, name='home'),
    path('form2/', views.form2, name='form2'),
]