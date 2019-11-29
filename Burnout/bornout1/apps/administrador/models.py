from django.db import models

# Create your models here.
class empresas(models.Model):
    TIPO = (
        ('1', 'Agricultura; plantaciones, otros sectores rurales.'),
        ('2', 'Alimentación; bebidas; tabaco.'),
        ('3', 'Comercio.'),
        ('4', 'Construcción.'),
        ('5', 'Educación.'),
        ('6', 'Fabricación de material de transporte.'),
        ('7', 'Función pública.'),
        ('8', 'Hotelería, restauración, turismo.'),
        ('9', 'otros'),
    )
    nombre_empresa = models.CharField(max_length=50)
    sector = models.CharField(max_length=1, choices=TIPO)
    nombre_propietario = models.CharField(max_length=50)
    numero_empleados = models.IntegerField()
    direccion = models.TextField()
    
