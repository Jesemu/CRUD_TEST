from django.db import models
from django_iban.fields import IBANField
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User


# Create your models here.
@python_2_unicode_compatible
class Usuario(models.Model):
	owner=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	name=models.CharField(max_length=250, default="")
	surname=models.CharField(max_length=250, default="")
	iban=IBANField(enforce_database_constraint=True, unique=True)
	concatenado=models.CharField(max_length=200, default="")
	def __str__(self):
		return self.concatenado