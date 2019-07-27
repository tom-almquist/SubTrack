from django.db import models


class Service(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=280)
	price = models.DecimalField(max_digits=5, decimal_places=2)