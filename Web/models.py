from django.db import models

# Create your models here.
class Formulario(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    apellido = models.CharField(max_length=50, verbose_name="Apellido")
    dni = models.CharField(max_length=10, verbose_name="DNI")
    nacionalidad = models.BooleanField(verbose_name="Nacionalidad")
    edad = models.BooleanField(verbose_name="Edad")
    telefono = models.CharField(max_length=15, verbose_name="Telefono")
    email = models.EmailField(verbose_name="Email")
    empresa = models.CharField(max_length=50, verbose_name="Empresa")
    consulta = models.BooleanField(verbose_name="Consulta")
    comentarios = models.TextField(verbose_name="Comentarios")
    

    class Meta:
        verbose_name = "Formulario"
        verbose_name_plural = "Formularios"

    