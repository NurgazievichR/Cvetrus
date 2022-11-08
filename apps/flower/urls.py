from django.urls import path

from apps.flower.views import products

urlpatterns = [
    path('products/', products, name='products'),
]