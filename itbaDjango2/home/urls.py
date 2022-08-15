from django.urls import path , include
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [path('', views.homebanking), path('cotizaciones', views.cotizaciones)]
