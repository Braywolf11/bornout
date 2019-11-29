from django.db import models
from apps.administrador.models import empresas

# Create your models here.
class user(models.Model):
    SEXO = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('O', 'Other'),
    )
    ACADE = (
        ('Primary', 'Primaria'),
        ('High school', 'Secundaria'),
        ('Technician', 'Tecnico'),
        ('Professional', 'Profesional'),
        ('Specialist', 'Especialista'),
        ('Doctorate', 'Doctor'),
    )
    ESTADO = (
        ('1', 'Activated'),
        ('2', 'disabled'),
        
    )
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=70)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=1, choices=SEXO)
    fecha_naci = models.DateField()
    nivelacademico = models.CharField(max_length=12, choices=ACADE)
    telefono = models.CharField(max_length=17)
    email = models.EmailField()
    direccion = models.TextField()
    profecion = models.CharField(max_length=50)
    empresa = models.ForeignKey(empresas, null=True, blank=True, on_delete=models.CASCADE)
    estado = models.CharField(max_length=12, choices=ESTADO)

    