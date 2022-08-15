from django.urls import path
from . import views


urlpatterns = [path('prestamos/',views.prestamos, name="prestamos"),path('prestamos/solicitar', views.solicitar )]