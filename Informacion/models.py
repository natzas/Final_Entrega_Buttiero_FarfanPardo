from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Archivo(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    profesion = models.CharField(max_length=40)
    titulo= models.CharField(max_length=40) #str corto
    cuerpo = models.TextField()
    fecha = models.DateField()
    adjunto = models.URLField()
    autor = models.CharField(max_length=40)
   

    def __str__(self):
        return self.titulo

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares' , null=True , blank=True)

class Mensaje (models.Model):
    nombre = models.CharField(max_length=40)
    email = models.EmailField()
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre
