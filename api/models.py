from django.db import models

# Create your models here.

class Ingrediente(models.Model):
    name = models.CharField(max_length=100)
    #url = models.URLField(blank=True)
    active = models.BooleanField(default=True)

class Plato(models.Model):
    name = models.CharField(max_length=100)
    ingredientes = models.ManyToManyField('api.Ingrediente', blank=True, related_name='platos')

class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    plato = models.ForeignKey('api.Plato', on_delete=models.PROTECT, null=True)

class MenuSemana(models.Model):
    title = models.CharField(max_length=200)
    menu = models.ForeignKey('api.Menu', on_delete=models.CASCADE, null=True)
