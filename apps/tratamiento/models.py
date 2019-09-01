from django.db import models
from apps.administrador.models import Persona
# Create your models here.
class Tratamiento(models.Model):
	tratam_id= models.AutoField(primary_key=True)
	descripcion=models.TextField()
	precio=models.DecimalField (max_digits=4,decimal_places=2)
	duracion = models.DurationField()
	persona = models.ForeignKey(Persona,null=True,blank=True,on_delete=models.CASCADE)