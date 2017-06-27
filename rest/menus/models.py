from __future__ import unicode_literals

from django.db import models

# Create your models here.


class FoodItem(models.Model):
	VEG = 0
	NON_VEG = 1
	HALF = 0
	FULL = 1

	TYPE_OPTION = (
		(VEG, "veg"),
		(NON_VEG, "Non_Veg"),
	)

	SIZE_OPTION = (
		(HALF, "half"),
		(FULL, "full"),
	)

	name = models.CharField(max_length=150)
	cuisine = models.ForeignKey('Cuisine')
	food_price = models.DecimalField(max_digits=4, decimal_places=1,
									 verbose_name="price of food item (Rs.)")

	food_size = models.IntegerField(
		null=True, choices=SIZE_OPTION, db_index=True,
		help_text="size of food item half/full")

	food_type = models.IntegerField(
		null=True, choices=TYPE_OPTION, db_index=True,
		help_text="type of food veg/non_veg")

	def __unicode__(self):
		return u"%s" % self.name


class Cuisine(models.Model):
	name = models.CharField(max_length=50)

	def __unicode__(self):
		return u"%s" % self.name


class Menu(models.Model):
	name = models.CharField(max_length=50)
	food_items = models.ManyToManyField('FoodItem')

	def __unicode__(self):
		return u"%s" % self.name
