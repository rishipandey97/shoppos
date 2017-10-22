# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import HttpResponse, render, get_object_or_404
from django.views.generic import TemplateView, ListView, UpdateView,FormView
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy

from django.shortcuts import render

from .models import Product
from .forms import ProductForm
from django.utils import timezone

from django.utils.timezone import localtime, now

from django.contrib.sessions.models import Session
# Create your views here.

#
# def index(request):
#     return HttpResponse("Hello")

#
# def index(request):
#     # import datetime
#     # now = datetime.datetime.now().strftime('%H:%M:%S')
#     prod = models.Product.objects.all().order_by('category')
#     cat = models.Category.objects.values_list('product_category',flat=True).distinct()
#     prod_list = models.Product.objects.all().order_by('category')
#     # cat = models.Product.objects.order_by('category').distinct('category')
#
#
#     print(prod_list)
#     # print(cat)
#     # print(prod)
#
#     mytime = localtime(now())
#     somename = "placeholder"
#     context = {'mytime': mytime, 'cat': cat, 'prod': prod, 'prod_list': prod_list,}
#     return render(request, 'sales/pos.html', context)


class ProductListView(ListView):
    model = Product
    template_name = "sales/products.html"
    form_class = ProductForm

    success_url = 'home'


class ProductUpdateView(UpdateView, FormMixin):
    form_class = ProductForm
    model = Product
    # redirect_field_name = 'sales/products.html'
    success_url = reverse_lazy("sales:productlist")
    template_name = 'sales/productupdate.html'

    def get_context_data(self, **kwargs):
        context = super(ProductUpdateView, self).get_context_data(**kwargs)
        context['product_details'] = Product.objects.filter(pk=self.kwargs['pk'])
        return context


class POSView(TemplateView):
    template_name = 'sales/pos.html'

    def get_context_data(self, **kwargs):
        context = super(POSView, self).get_context_data(**kwargs)
        context['mytime'] = localtime(now())
        context['prod_list'] = Product.objects.filter(available=True).order_by('category')
        return context


class CheckoutView(TemplateView):
    template_name = 'sales/checkout.html'
    form_class = ProductForm
    initial = {'key': 'value'}




    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})


    def retrieve_anon_cart(self,request):
        key = self.request.session.session_key
        print key



            # def get(self, request):
    #     context_data = self.request
    #     return HttpResponse(context_data)
    #
    #     print request.GET.get('FilmName', None)
    #     if self.request.method == "GET":
    #         print "Inside the if"
    #         context_data = self.request
    #         return self.render({'context_data': context_data})
    #
    # def process_order(self,request):
    #     if request.method == 'GET':
    #         form = OrderForm(request.GET)
    #         if form.is_valid():
    #             print form





