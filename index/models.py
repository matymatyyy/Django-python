from django.db import models

# Create your models here.
class Usuario(models.Model):
    name = models.CharField(max_length=20)
    gmail= models.CharField(max_length=50)
    password=models.CharField(max_length=20)
    number=models.CharField(max_length=20)
    date=models.CharField(max_length=10, null=True)
    
    def __str__(self):
        return self.name

class Compra(models.Model):
    carrito=models.CharField(max_length=50)
    name=models.ForeignKey(Usuario,max_length=20, on_delete=models.CASCADE)
    