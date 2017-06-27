from django.contrib import admin

import customers.models as models

class CustomerAdmin(admin.ModelAdmin):

    model = models.Customer
    list_display = ('id',)
    search_fields = ('customer__user__first_name',
                     'customer__user__last_name',
                     'customer__user__email')


admin.site.register(models.Customer, CustomerAdmin)