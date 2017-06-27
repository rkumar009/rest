from django.contrib import admin

# Register your models here.
import menus.models as models



admin.site.register(models.FoodItem)
admin.site.register(models.Cuisine)
admin.site.register(models.Menu)
