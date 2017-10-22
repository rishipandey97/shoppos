# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse

from django.db import models

# Create your models here.

from django.db import models

# Create your models here.


class Category(models.Model):
    product_category = models.CharField(max_length=50)

    def __unicode__(self):
        return '%s' % (self.product_category)

    class Meta:
        # app_label = 'product'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    product_name = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(Category)
    price = models.PositiveIntegerField(default= 0)
    available = models.BooleanField(default=True)

    # def __str__(self):
    #     return '%s %s' % (self.product_name, self.category)

    def get_absolute_url(self):
        return reverse('sales:productupdate',kwargs={'pk':self.pk})
    #,kwargs={'pk':self.pk}

    class Meta:
        # app_label = 'product'
        verbose_name_plural = 'Products'
#
#
# class CartItem(models.Model):
#     sales_id = models.AutoField(max_length=10,unique=True,)
#     product_name = models.ForeignKey(Product)
#     quantity = models.PositiveIntegerField()
#     total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)

