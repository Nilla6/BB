from django.db import models

# Create your models here.
class ContactMe(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    description =models.CharField(max_length=500)
