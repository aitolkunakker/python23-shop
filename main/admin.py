from django.contrib import admin
from .models import Category,Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['tiltle', 'category','status']
    list_filter  = ['category', 'status']
    search_fields= ['title', 'decription']

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)

