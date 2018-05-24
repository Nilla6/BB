from django.db import models
from orders.choices import *


class Order(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    address2 = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    State = models.CharField(max_length=20, choices=STATE_CHOICES)
    Country = models.CharField(max_length=50, choices=COUNTRY_CHOICES)
    stripe_id = models.CharField(max_length=255, default='NULL')
