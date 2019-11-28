from django.db import models

# Create your models here.
class user(models.Model):
    SEXO = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('O', 'Other'),
    )
    ACADE = (
        ('Primary', 'pPrimaria'),
        ('High school', 'Secundaria'),
        ('Technician', 'Tecnico'),
        ('Professional', 'Profesional'),
        ('Specialist', 'Especialista'),
        ('Doctorate', 'Doctor'),
    )
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=70)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=1, choices=SEXO)
    fecha_naci = models.DateField()
    nivelacademico = models.CharField(max_length=1, choices=SEXO)
    telefono = models.CharField(max_length=17)
    email = models.EmailField()
    direccion = models.TextField()