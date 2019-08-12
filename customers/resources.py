from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from customers.models import Customer


class CustomerResource(ModelResource):
	class Meta:
		queryset = Customer.objects.all()
		resource_name = 'customer'
		authorization = Authorization()