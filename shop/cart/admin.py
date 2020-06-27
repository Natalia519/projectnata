from django.contrib import admin
from .models import Cart, CartItem, CartState


@admin.register(CartState)
class CartStateAdmin(admin.ModelAdmin):
    pass


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    pass


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    pass
