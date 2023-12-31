from django.db import models

# Create your models here.
class Pago(models.Model):
	nombreApellidos = models.CharField(max_length = 100)
	email = models.EmailField()
	token = models.CharField(max_length = 1000)
	plan = models.CharField(max_length = 50)
	metodo = models.CharField(max_length = 50)

	def __str__(self):
		return f"{self.id}{self.nombreApellidos}{self.email}{self.token}{self.plan}{self.metodo}"

class DatosNequi(models.Model):
	usuario = models.ForeignKey("Pago", on_delete = models.CASCADE, default = 0)
	numero = models.CharField(max_length = 20)	

class DatosTarjeta(models.Model):
	usuario = models.ForeignKey("Pago", on_delete = models.CASCADE, default = 0)
	IdTransaccion = models.CharField(max_length = 1000, default = " ")
