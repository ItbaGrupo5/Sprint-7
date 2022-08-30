from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import RegistroForm
from django.contrib.auth.models import User
from django.contrib.auth import logout
import random
from random import randrange
from datetime import date

# Modelos utilizados al registrarse
from clientes.models import Cliente
from cuentas.models import Cuenta
from tarjetas.models import Tarjeta


def registro(request):
    registro_form = RegistroForm

    if request.method == "POST":
        registro_form = registro_form(data=request.POST)
        if registro_form.is_valid():
            cliente_id = request.POST.get('cliente_id')
            email = request.POST.get('email')
            pwd = request.POST.get('pwd')
            nombre = request.POST.get('nombre')
            apellido = request.POST.get('apellido')

            # DNI como username
            user = User.objects.create_user(
                cliente_id, email, pwd, last_name=apellido, first_name=nombre)
            user.save()

            # al usuario se le crea automaticamente una cuenta y una entrada como cliente en la DB , TIPO = classic
            tipos = ['CLASSIC', 'GOLD', 'BLACK']

            today = date.today()
            currentdate = today.strftime("%b-%d-%Y")
            cliente = Cliente.objects.create(
                customer_name=nombre, customer_surname=apellido, customer_dni=cliente_id, cliente_type=random.choice(tipos), dob=currentdate, branch_id=randrange(100))
            cliente.save()
            cuenta = Cuenta.objects.create(customer=cliente, balance=0, iban=0)
            cuenta.save()
            tiposTarjeta = ['DEBITO', 'CREDITO']
            tarjeta = Tarjeta.objects.create(
                customer=cliente, account=cuenta, tipo=random.choice(tiposTarjeta))
            tarjeta.save()

        return redirect(reverse('login'))
    return render(request, "registration/registro.html", {'form': registro_form})


def logout_view(request):
    logout(request)
    return render(request, "registration/logout.html")