# Generated by Django 2.2.4 on 2019-11-29 02:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administrador', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=70)),
                ('edad', models.IntegerField()),
                ('sexo', models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('O', 'Other')], max_length=1)),
                ('fecha_naci', models.DateField()),
                ('nivelacademico', models.CharField(choices=[('Primary', 'Primaria'), ('High school', 'Secundaria'), ('Technician', 'Tecnico'), ('Professional', 'Profesional'), ('Specialist', 'Especialista'), ('Doctorate', 'Doctor')], max_length=12)),
                ('telefono', models.CharField(max_length=17)),
                ('email', models.EmailField(max_length=254)),
                ('direccion', models.TextField()),
                ('profecion', models.CharField(max_length=50)),
                ('estado', models.CharField(choices=[('1', 'Activated'), ('2', 'disabled')], max_length=12)),
                ('empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='administrador.empresas')),
            ],
        ),
    ]
