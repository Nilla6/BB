from django.db import models

# Create your models here.
class Products(models.Model):
	description = models.CharField(max_length = 50)
	price = models.FloatField(default=0)
	quantity = models.IntegerField(default=0)
	image = models.FileField(null=True, blank=True)
