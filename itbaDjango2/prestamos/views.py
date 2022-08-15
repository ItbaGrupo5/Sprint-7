from django.shortcuts import render, redirect
from datetime import date
from django.contrib.auth.decorators import login_required
from prestamos.models import Prestamo
from clientes.models import Cliente
from cuentas.models import Cuenta, Movimiento
# Create your views here.


def getPrestamoActual(request):
    prestamoActual = 0
    cliente = Cliente.objects.get(customer_dni=request.user.username)
    prestamo = Prestamo.objects.filter(customer_id=cliente.customer_id)
    if prestamo:
        if len(prestamo) > 1:
            for query in prestamo:
                prestamoActual += query.loan_total
        else:
            prestamoActual = prestamo[0].loan_total
    return prestamoActual


def getPrestamos(request):
    cliente = Cliente.objects.get(customer_dni=request.user.username)
    prestamos = Prestamo.objects.filter(customer_id=cliente.customer_id)
    return prestamos


def getCreditoDisponible(request):
    creditoDisponible = 0
    prestamoActual = getPrestamoActual(request)
    cliente = Cliente.objects.get(customer_dni=request.user.username)
    tipo = cliente.cliente_type
    if tipo == 'CLASSIC':
        creditoDisponible = 100000 - prestamoActual
    elif tipo == 'GOLD':
        creditoDisponible = 300000 - prestamoActual
    elif tipo == 'BLACK':
        creditoDisponible = 500000 - prestamoActual
    return creditoDisponible


@login_required
def prestamos(request):

    creditoDisponible = getCreditoDisponible(request)
    prestamoActual = getPrestamoActual(request)
    msgPrestamo = ''
    prestamos = getPrestamos(request)
    cliente = Cliente.objects.get(customer_dni=request.user.username)
    prestamo = Prestamo.objects.filter(customer_id=cliente.customer_id)
    tipo = cliente.cliente_type

    if prestamo != 0:
        msgPrestamo = f"Posee un prestamo por {prestamoActual}"
    else:
        msgPrestamo = 'No posee ningun prestamo'

    return render(request, 'base.html', {'prestamo': msgPrestamo, 'creditoDisponible': creditoDisponible, 'tipo': tipo, 'surname': cliente.customer_surname, 'prestamos': prestamos})


@login_required
def solicitar(request):
    cliente = Cliente.objects.get(customer_dni=request.user.username)
    cuenta = Cuenta.objects.get(customer_id=cliente)
    creditoDisponible = getCreditoDisponible(request)
    if request.method == 'POST':
        monto = request.POST.get('monto')
        if int(monto) > creditoDisponible or int(monto) < 0:
            return render(request, 'home.html')
        else:
            today = date.today()
            currentdate = today.strftime("%b-%d-%Y")
            Prestamo.objects.create(
                loan_type='base', loan_date=currentdate, loan_total=monto, customer=cliente)
            cuenta.balance = (cuenta.balance + int(monto))
            cuenta.save()
            nuevoMovimiento = Movimiento.objects.create(
                tipo_operacion='DEPOSITO', numero_cuenta=cuenta, hora=currentdate, monto=monto)
            nuevoMovimiento.save()
            return(redirect('/prestamos'))
    return render(request, 'solicitar.html', {'creditoDisponible': creditoDisponible, 'surname': cliente.customer_surname})

# 27030559
