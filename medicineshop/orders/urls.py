from django.conf.urls import url
from . import views

urlpatterns = [
    url('create/', views.order_create, name='order_create'),
]