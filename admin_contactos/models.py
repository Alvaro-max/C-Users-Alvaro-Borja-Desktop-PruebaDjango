from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH


# Create your models here.

class Contactos(models.Model): 

    numeroCelular = models.CharField(max_length=15 , verbose_name="Numero de Telefono")
    nombre = models.CharField(max_length=75, verbose_name="Nombres")
    apellido = models.CharField(max_length=75, verbose_name="Apellidos")
    correo = models.EmailField(verbose_name="Email")
    imagenContacto = models.ImageField(blank=True, null=True, upload_to="contactos", verbose_name="Foto Perfil")

    def __str__(self):
        return self.nombre
