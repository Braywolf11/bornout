# Generated by Django 2.2.4 on 2019-11-29 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresas',
            name='numero_empleados',
            field=models.IntegerField(),
        ),
    ]
