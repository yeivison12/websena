from pyexpat import model
from tkinter.tix import Tree
from django.db import models
from django.forms import SlugField

# Create your models here.
class Link(models.Model):
    key = models.SlugField(  verbose_name="Nombre Clave ", max_length=100, unique=True)
    name =models.CharField(verbose_name="Red social", max_length=200)
    url = models.URLField(verbose_name="Enlace", max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated =models.DateTimeField(auto_now =True, verbose_name="Fecha de creación")
    class Meta:
        verbose_name = "Enlace"
        verbose_name_plural = "Enlaces"
        ordering = ["name"]
        
    def __str__(self):
        return self.name
#create a model with user things
