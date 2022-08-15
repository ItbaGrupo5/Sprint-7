from django.db import models
from clientes.models import Cliente

# Create your models here.


class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    balance = models.IntegerField()
    iban = models.TextField()

    class Meta:
        db_table = 'cuenta'


class Movimiento(models.Model):
    EXTRACCION = 'EXTRACCION'
    DEPOSITO = 'DEPOSITO'
    types = [(EXTRACCION, 'EXTRACCION'), (DEPOSITO, 'DEPOSITO')]
    movimiento_id = models.AutoField(primary_key=True)
    numero_cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    tipo_operacion = models.CharField(max_length=10, choices=types)
    hora = models.TextField()
    monto = models.IntegerField()

    class Meta:
        db_table = 'movimiento'
