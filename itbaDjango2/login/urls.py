from django.urls import path , include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [path('', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login') , path('registro/', views.registro, name="registro"),path('logout',views.logout_view, name="logout")]
