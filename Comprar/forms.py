from django import forms

class FormDatosUser(forms.Form):
	usuario = forms.CharField(label = "Nombre y Apellidos: ", max_length = 100)
	correo = forms.EmailField(label = "Correo Electronico: ")
	metodo = forms.ChoiceField(choices = (("Nequi","Nequi"),("Tarjeta","Tarjeta")), label = "Metodo De Pago: ")
