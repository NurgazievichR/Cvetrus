from django.urls import path

from apps.flower.views import products, single_product, offers, wallet, history_order

urlpatterns = [
    path('products/', products, name='products'),
    path('products/<int:id>', single_product, name='single_product'),
    path('offers/', offers, name='offers'),
    path('balance/', wallet, name='wallet'),
    path('history_orders/', history_order, name='history-order')
]