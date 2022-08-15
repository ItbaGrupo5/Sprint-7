
from django.db import models

class Cliente(models.Model):
    BLACK = 'BLACK'
    GOLD = 'GOLD'
    CLASSIC = 'CLASSIC'

    types = [(BLACK, 'BLACK'),(GOLD, 'GOLD'),(CLASSIC, 'CLASSIC')]

    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    cliente_type = models.CharField(max_length= 9, choices=types, default=CLASSIC)
    customer_surname = models.TextField()  # This field type is a guess.
    customer_dni = models.TextField(db_column='customer_DNI')  # Field name made lowercase.
    branch_id = models.IntegerField()
    dob = models.TextField()

    class Meta:
        db_table = 'cliente'
