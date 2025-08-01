from django.db import models

# Create your models here.

class Programa(models.Model):
    NIVEL_FORMACION_CHOICES = [
        ('AUX', 'Auxiliar'),
        ('OPE', 'Operario'),
        ('TEC', 'Técnico'),
        ('ESP', 'Especialización  Tecgnologica'),
        ('COM', 'Complementario'),
    ]
    
    MODALIDAD_CHOICES = [
        ('PRE', 'Presencial'),
        ('VIR', 'Virtual'),
        ('MIX', 'Híbrida'),
    ]
    
    ESTADO_CHOICES = [
        ('ACT', 'Activo'),
        ('INA', 'Inactivo'),
        ('SUS', 'Suspendido'),
        ('CAN', 'Cancelado'),
    ]
    
    codigo = models.CharField(max_length=10, unique=True, verbose_name='Código del Programa')
    nombre = models.CharField(max_length=100, verbose_name='Nombre del Programa')
    nivel_formacion = models.CharField(max_length=10, choices=NIVEL_FORMACION_CHOICES, verbose_name='Nivel de Formación')
    modalidad = models.CharField(max_length=10, choices=MODALIDAD_CHOICES, default='PRE', verbose_name='Modalidad')
    duracion_horas = models.PositiveIntegerField(verbose_name='Duración en Horas')
    duracion_meses = models.PositiveIntegerField(verbose_name='Duración en Meses')
    descripcion = models.TextField(verbose_name='Descripción del Programa')
    competencias = models.TextField(verbose_name='Competencias del Programa')
    perfil_egreso = models.TextField(verbose_name='Perfil de Egreso')
    requisitos_ingreso = models.TextField(verbose_name='Requisitos de Ingreso')
    centro_formacion = models.CharField(max_length=200, verbose_name='Centro de Formación')
    regional = models.CharField(max_length=100, verbose_name='Regional')
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='ACT', verbose_name='Estado del Programa')
    fecha_creacion = models.DateTimeField(verbose_name='Fecha de Creación del Programa')
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')
    
    class Meta:
        verbose_name = 'Programa'
        verbose_name_plural = 'Programas'
        ordering = ['nombre']
        
    def __str__(self):
        return f"{self.codigo} - {self.nombre}"
    
    def get_duracion_completa(self):
        return f"{self.duracion_meses} meses {self.duracion_horas} horas"
    
    def is_activo(self):
        return self.estado == 'ACT'
    
    
