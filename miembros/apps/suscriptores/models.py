from django.db import models

# Create your models here.


class sexo(models.Model):
    Id_Sexo = models.AutoField(primary_key=True)
    sexo = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.sexo

class Ciudad(models.Model):
    Id_Ciudad = models.AutoField(primary_key=True)
    ciudad  = models.CharField(max_length=30, null=False, blank=False)

    class Meta:
        ordering = ['ciudad']   

    def __str__(self):
        return self.ciudad

class Nacionalidad(models.Model):
    Id_Nacionalidad = models.AutoField(primary_key=True)
    nacionalidad = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.nacionalidad
 