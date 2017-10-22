# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Category, Product

# Register your models here.

admin.site.register(Category)



class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'category', 'price', 'available']
    ordering = ['product_name']

admin.site.register(Product, ProductAdmin)