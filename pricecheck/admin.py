from django.contrib import admin

# Register your models here.

from pricecheck.models import Item, Price

admin.site.register(Item)
admin.site.register(Price)
