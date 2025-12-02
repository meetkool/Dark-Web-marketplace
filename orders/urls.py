
from django.urls import re_path
from . import views

app_name = 'orders'

urlpatterns = [
    re_path(r'^create/(?P<product_id>\d+)/$', views.order_create, name='order_create'),
    re_path(r'^(?P<order_id>\d+)/(?P<product_id>\d+)/pay/$', views.pay, name='pay'),
    re_path(r'^waiting/(?P<order_id>\d+)/(?P<address>[-\w]+)/(?P<cost>\d+\.\d{8})$', views.waiting, name='waiting'),
]
