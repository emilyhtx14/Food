from django.db import models
from django.contrib import auth


# Create your models here.

class Donate(models.Model):
    user = models.CharField(max_length = 100, default= 'aoc')
    supermarket = models.CharField(max_length = 100)
    delivery_date = models.DateField()

    # starting cost of the delivery
    start_cost = models.DecimalField(max_digits = 100, decimal_places = 2, default = 0.00)

    # amount that the user wants to donate
    amount = models.DecimalField(max_digits = 100, decimal_places = 2)

    # default is that it's true so it's a donation
    cost_type = models.BooleanField(default = True)

