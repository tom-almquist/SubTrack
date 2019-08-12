from django.db import models
from services.models import Service

class Customer(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	services = models.ForeignKey(
		Service,
		null=True,
		blank=True,
		default=None,
		on_delete=models.SET_NULL,
	)

	CONFIRMED = 'co'
	SET_UP = 'su'
	ACTIVE = 'ac'
	CANCELLED = 'ca'
	ACCOUNT_STATE_CHOICES = [
		(CONFIRMED, 'confirmed'),
		(SET_UP, 'set-up'),
		(ACTIVE, 'active'),
		(CANCELLED, 'cancelled'),
	]
	account_state = models.CharField(
		max_length=2,
		choices=ACCOUNT_STATE_CHOICES,
		default=CONFIRMED,
	)

	def __str__(self):
		return f"{self.first_name} {self.last_name}: {self.account_state}"

