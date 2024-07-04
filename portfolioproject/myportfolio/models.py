from django.db import models
from ckeditor.fields import RichTextField
from .utils import encrypt_message, decrypt_message

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Tecnologia(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='proyectos/')
    descripcion = models.TextField()
    contenido = RichTextField()
    tecnologias = models.ManyToManyField(Tecnologia)
    link_sitio = models.URLField(max_length=200)
    link_repositorio = models.URLField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class ImagenProyecto(models.Model):
    proyecto = models.ForeignKey(Proyecto, related_name='imagenes_set1', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='proyectos/set1/')

    def __str__(self):
        return f"Imagen set1 para {self.proyecto.titulo}"

class ImagenProyecto2(models.Model):
    proyecto = models.ForeignKey(Proyecto, related_name='imagenes_set2', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='proyectos/set2/')

    def __str__(self):
        return f"Imagen set2 para {self.proyecto.titulo}"

class ImagenProyecto3(models.Model):
    proyecto = models.ForeignKey(Proyecto, related_name='imagenes_set3', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='proyectos/set3/')

    def __str__(self):
        return f"Imagen set3 para {self.proyecto.titulo}"

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    mensaje_cifrado = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

def save(self, *args, **kwargs):
    self.mensaje_cifrado = encrypt_message(self.mensaje_cifrado)
    super().save(*args, **kwargs)

def get_mensaje(self):
    return decrypt_message(self.mensaje_cifrado)

def __str__(self):
    return self.nombre