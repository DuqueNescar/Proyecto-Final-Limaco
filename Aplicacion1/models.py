from django.db import models

# Create your models here.
class Curso(models.Model): 
    codigo=models.CharField(primary_key=True,max_length=7)
    nombre=models.CharField(max_length=50)
    creditos=models.PositiveBigIntegerField()

    def __str__(self): #nombre y credito entre parentesis
        texto = "{0} ({1})"
        return texto.format(self.nombre,self.creditos)

class Curso1(models.Model):
    codigo1=models.CharField(primary_key=True,max_length=7)
    nombre1=models.CharField(max_length=50)
    creditos1=models.PositiveBigIntegerField()

    def __str__(self):
        texto = "{0} ({1})" #nombre y credito entre parentesis
        return texto.format(self.nombre1,self.creditos1)

class Curso2(models.Model):
    codigo2=models.CharField(primary_key=True,max_length=7)
    nombre2=models.CharField(max_length=50)
    creditos2=models.PositiveBigIntegerField()
    
    def __str__(self):
        texto = "{0} ({1})" #nombre y credito entre parentesis
        return texto.format(self.nombre2,self.creditos2)
