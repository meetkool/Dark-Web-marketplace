from django.urls import re_path
from . import views

app_name = 'background'

urlpatterns = [
    re_path(r'^$', views.pull_crypto_price, name='pull_crypto_price'),
]
