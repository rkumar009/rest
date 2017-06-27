from __future__ import unicode_literals

from django.db import models
import customers.models

# Create your models here.


class order(models.Model):
    customer = models.ForeignKey('customers.models.Customer')
    food_orders = models.ManyToManyField('FoodOrder')
    PurchaseStatus
    TimeStamp
    TotalPrice

class order(models.Model)