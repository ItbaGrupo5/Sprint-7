# Generated by Django 4.1 on 2022-08-11 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cuenta',
            new_name='Cliente',
        ),
    ]