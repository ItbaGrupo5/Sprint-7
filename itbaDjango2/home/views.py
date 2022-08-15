
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from clientes.models import Cliente
from cuentas.models import Cuenta
# Create your views here.


@login_required
def homebanking(request):
    cliente = Cliente.objects.get(customer_dni=request.user.username)
    cuenta = Cuenta.objects.get(customer_id = cliente.customer_id)
    name = cliente.customer_name + " " + cliente.customer_surname
    
    return render(request, "../templates/homebanking.html", {'name': name, 'surname': cliente.customer_surname, 'balance': cuenta.balance, 'numerocuenta': cuenta.account_id})

@login_required
def cotizaciones(request):
    return render(request, "../templates/cotizaciones.html")
