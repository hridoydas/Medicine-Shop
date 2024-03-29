from django.conf.urls import url

from . import views

urlpatterns = [
    url('', views.cart_detail, name='cart_detail'),
    url('add/(?P<product_id>\d+)/',views.cart_add,name='cart_add'),
    url('remove/(?P<product_id>\d+)/',views.cart_remove,name='cart_remove'),
]