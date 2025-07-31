from django.db import models

# Create your models here.
class Instructor(models.Model):
    TIPO_DOCUMENTO_CHOICES = [
        ('CC', 'Cédula de Ciudadanía'),
        ('CE', 'Cédula de Extranjería'),
        ('TI', 'Tarjeta de Identidad'),
        ('PA', 'Pasaporte'),
    ]
    NIVEL_EDUCATIVO_CHOISES = [
        ('Bachillerato', 'Bachillerato'),
        ('TEC', 'Técnico'),
        ('TGL', 'Tecnólogo'),
        ('PRE', 'Pregrado'),
        ('ESP', 'Especializacion'),
        ('MAE', 'Maestría'),
        ('DOC', 'Doctorado'),
    ]
    documento_identidad = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10, null=True)
    correo = models.EmailField(null=True)
    fecha_nacimiento = models.DateField()
    ciudad = models.CharField(max_length=100, null=True)
    nivel_educativo = models.CharField(max_length=100, choices= NIVEL_EDUCATIVO_CHOISES, default='Bachillerato') 
    especialidad = models.CharField(max_length=100)
    anos_experiencia = models.PositiveIntegerField(default=0)
    activo = models.BooleanField(default=True)
    fecha_vinculacion = models.DateField(null=True, blank=True)
    fecha_registro = models.DateField(auto_now_add=True)
    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.especialidad}"
    
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"