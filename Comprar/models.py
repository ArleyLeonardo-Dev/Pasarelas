from django.db import models

# Create your models here.
class Pago(models.Model):
	nombreApellidos = models.CharField(max_length = 100)
	email = models.EmailField()
	token = models.CharField(max_length = 1000)
	plan = models.CharField(max_length = 50)
	metodo = models.CharField(max_length = 50)

class DatosNequi(models.Model):
	usuario = models.ForeignKey("Pago", on_delete = models.CASCADE, default = 0)
	numero = models.CharField(max_length = 20)	

class DatosTarjeta(models.Model):
	usuario = models.ForeignKey("Pago", on_delete = models.CASCADE, default = 0)
	numero = models.CharField(max_length = 100)
	cvc = models.CharField(max_length = 100)
	exp_mes = models.CharField(max_length = 3)
	exp_year = models.CharField(max_length = 3)
	nombre = models.CharField(max_length = 100)