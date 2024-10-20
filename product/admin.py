from django.contrib import admin
from .models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','category','description','price')
    prepopulated_fields = {"slug":("name",)}
    

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)