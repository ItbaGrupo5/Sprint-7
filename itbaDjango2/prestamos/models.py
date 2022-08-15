from django.db import models
from clientes.models import Cliente

class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type = models.TextField()
    loan_date = models.TextField()
    loan_total = models.IntegerField()
    customer = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    class Meta:
        db_table = 'prestamo'
