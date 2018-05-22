from django.db import models


# Create your models here.
class Product(models.Model):
	description = models.CharField(max_length = 50)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	quantity = models.PositiveIntegerField(default=0)
	image = models.ImageField(null=True, blank=True)
	available = models.BooleanField(default=True)
	updated = models.DateTimeField(auto_now=True)
