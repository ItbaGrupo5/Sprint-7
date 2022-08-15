from django.db import models
from clientes.models import Cliente
from cuentas.models import Cuenta

# Create your models here.


class Tarjeta(models.Model):

    DEBITO = 'DEBITO'
    CREDITO = 'CREDITO'
    types = [(DEBITO, 'DEBITO'), (CREDITO, 'CREDITO')]
    tarjeta_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    account = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=7,blank=True, choices=types, default=DEBITO)

    class Meta:
        db_table = 'tarjeta'
