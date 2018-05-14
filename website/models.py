from django.db import models

# Create your models here.
class Products(models.Model):
	description = models.CharField(max_length = 250)
	price = models.FloatField()
	quantity = models.IntegerField()
