from django.db import models

# Create your models here.
class Persona(models.Model):
	admin_id= models.AutoField(primary_key=True)
	nombre=models.CharField(max_length=20)
	apellido=models.CharField(max_length=20)
	sexo=models.CharField(max_length=10)
	correo=models.EmailField ()
	telefono=models.CharField(max_length=10)

	def __str__(self):
		return '{} {}'.format(self.nombre,self.apellido)