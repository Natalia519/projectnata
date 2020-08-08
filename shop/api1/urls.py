from django.urls import path
from . import views

app_name = 'api1'
urlpatterns = [
    path('item/add/', views.item_add_to_cart, name='item_add_to_cart'),
    path('goods/cart/', views.get_cart_goods, name='get_cart_goods'),
    path('goods/', views.get_all_goods, name='get_all_goods'),
    path('item/incdec/', views.cart_item_inc_dec, name='cart_item_inc_dec'),
]


