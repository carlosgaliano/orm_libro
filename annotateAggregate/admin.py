from django.contrib import admin
from .models import Order, Seller

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ('seller', 'total',)
    list_filter = ('seller',)
    search_fields = ('total',) 


 

admin.site.register(Seller)
admin.site.register(Order, OrderAdmin)
