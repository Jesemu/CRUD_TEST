from django import forms
from django.forms import ModelForm
from django_iban.fields import IBANField
from app.models import *


class UserForm(forms.ModelForm):
	name=forms.CharField(min_length=2, max_length=15)
	surname=forms.CharField(max_length=200)
	iban=IBANField(enforce_database_constraint=True, unique=True)
	concatenado=forms.CharField(max_length=200, widget=forms.HiddenInput, required=False)

	class Meta:
		model = Usuario
		fields = ('concatenado','name','surname','iban')
	
	def clean_name(self):
		name=self.cleaned_data.get('name')
		return name.upper()	

	def clean_surname(self):
		surname=self.cleaned_data.get('surname')
		return surname.upper()

	def clean_iban(self):
		iban=self.cleaned_data.get('iban')
		if (Usuario.objects.filter(iban=iban)):
			raise forms.ValidationError("Error,  "+iban+" is registred")
			return iban
		return iban

	def clean_email(self):
		email=self.cleaned_data.get('email')
		lista_usuarios=Usuario.objects.all()
		if(Usuario.objects.filter(email=email)):
			raise forms.ValidationError("Error, email "+email+" is registred")
			return email
		return email


	def clean(self):
		if(self.is_valid()):
			name=self.cleaned_data.get('name')
			surname=self.cleaned_data.get('surname')
			self.cleaned_data['concatenado']=name+" "+surname