from django import forms
from apps.usuarios.models import user

class UsuariosForm(forms.ModelForm):
    class Meta:
        model = user

        fields = [
            'nombre',
            'apellidos', 
            'edad', 
            'sexo', 
            'fecha_naci',
            'nivelacademico',
            'telefono',
            'email',
            'direccion',
            'profecion', 
            'empresa', 
            'estado',
        ]
        labels = {
            'nombre':'Nombre',
            'apellidos': 'Apellidos', 
            'edad': 'Edad', 
            'sexo': 'Sexo', 
            'fecha_naci': 'Fecha_naci',
            'nivelacademico': 'Nivelacademico:',
            'telefono': 'Telefono',
            'email': 'Email',
            'direccion': 'Direccion',
            'profecion': 'Profecion', 
            'empresa': 'Empresa', 
            'estado': 'Estado',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}), 
            'edad': forms.TextInput(attrs={'class': 'form-control'}), 
            'sexo': forms.CheckboxSelectMultiple(), 
            'fecha_naci': forms.TextInput(attrs={'class': 'form-control'}),
            'nivelacademico': forms.CheckboxSelectMultiple(), 
            'telefono':forms.TextInput(attrs={'class': 'form-control'}), 
            'email':forms.TextInput(attrs={'class': 'form-control'}), 
            'direccion':forms.TextInput(attrs={'class': 'form-control'}), 
            'profecion':forms.TextInput(attrs={'class': 'form-control'}),  
            'empresa':forms.TextInput(attrs={'class': 'form-control'}), 
            'estado': forms.CheckboxSelectMultiple(),

        }