from django.conf.urls import url
from . import views
from .views import ProductListView,ProductUpdateView,POSView, CheckoutView
from .import views

#template urls
app_name = 'sales'


urlpatterns = [
    # url(r'^POS/$', views.index, name='index'),
    url(r'^POS/$', POSView.as_view(), name='index'),
    url(r'^product/$', ProductListView.as_view(), name='productlist'),
    url(r'^product/update/(?P<pk>[0-9]+)$', ProductUpdateView.as_view(), name='productupdate'),
    url(r'^checkout/$', CheckoutView.as_view(), name='checkout'),
    # url(r'aboutus/$', views.about, name = 'about'),


]
