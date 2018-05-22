from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['description', 'price', 'quantity', 'available']
    list_filter = ['available', 'updated']
    list_editable = ['price','quantity', 'available']
admin.site.register(Product, ProductAdmin)
