from django import forms

from apps.tratamiento.models import Tratamiento


class TratamientoForm(forms.ModelForm):

	class Meta:
		model = Tratamiento

		fields = [
			'tratam_id',
			'descripcion',
			'precio',
			'duracion',
			'persona',
		]
		labels = {
			'tratam_id': 'Trata_id',
			'descripcion': 'Descripcion',
			'precio': 'Precio',
			'duracion':'Duracion',
			'persona': 'Admin',
		}
		widgets = {
			'tratam_id': forms.TextInput(attrs={'class':'form-control'}),
			'descripcion': forms.TextInput(attrs={'class':'form-control'}),
			'precio': forms.TextInput(attrs={'class':'form-control'}),
			'duracion': forms.TextInput(attrs={'class':'form-control'}),
			'persona': forms.Select(attrs={'class':'form-control'}),

		}