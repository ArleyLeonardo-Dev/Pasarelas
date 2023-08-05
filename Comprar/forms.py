from django import forms

class FormDatosUser(forms.Form):
	usuario = forms.CharField(label = "Nombre y Apellidos ", max_length = 100)
	correo = forms.EmailField(label = "Correo Electronico ")
	metodo = forms.ChoiceField(choices = (("Nequi","Nequi"),("Tarjeta","Tarjeta")), label = "Metodo De Pago ")

class FormPagoNequi(forms.Form):
	numero = forms.CharField(label = "Numero ")

class FormPagoTarjeta(forms.Form):
	numero = forms.CharField(label = "Numero De Tarjeta", max_length = 19)
	cvc = forms.CharField(label = "CVC", max_length = 3)
	exp_mes = forms.CharField(label = "Mes", max_length = 3)
	exp_year = forms.CharField(label = "Año", max_length = 3)
	nombre = forms.CharField(label = "Nombre Propietario", max_length = 100)