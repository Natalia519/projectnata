import logging

from django.shortcuts import render
from django.template.defaultfilters import register
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import Cart, CartItem, CartState

from goods.models import Goods, Product
from django.db.models import ObjectDoesNotExist

logger = logging.getLogger(__name__)


@register.filter
def multiply(value, arg):
    return value * arg


class CartView(View):
    template_name = 'cart.html'

    def get(self, request, pk):
        logger.debug("GET debug %s", pk)
        user_id = None
        cart_id = request.session.get("cart_id", None)
        logger.debug("cart_id: %s", cart_id)
        if cart_id == None:
            user_id = request.session.get("_auth_user_id", None)
            logger.debug("user_id: %s", user_id)
        try:
            if cart_id != None:
                cart = Cart.objects.get(pk=cart_id)
            else:
                index = 0
                carts_all = Cart.objects.filter(userId=user_id)
                for v in carts_all:
                    if index < v.pk:
                        index = v.pk
                        cart = v
                cart_id = cart.pk
        except ObjectDoesNotExist as e:
            logger.debug("exception: %s", e)
            cart = None
        request.session['cart_id'] = cart_id
        logger.debug("cart: %s", cart)
        try:
            cart_items = CartItem.objects.filter(cartId=cart_id)
        except ObjectDoesNotExist as e:
            logger.debug("exception: %s", e)
            cart_items = None

        logger.debug("cart_item: %s", cart_items)
        full = 0
        cart_items_out = []
        for i in range(len(cart_items)):
            if int(cart_items[i].quantity) == 0:
                CartItem.objects.filter(pk=cart_items[i].pk).delete()
            else:
                cart_items[i].product = Product.objects.get(name=cart_items[i].goodsId)
                cart_items[i].quantity = int(cart_items[i].quantity)
                cart_items[i].goods = Goods.objects.get(productId=cart_items[i].product.pk)
                cart_items_out.append(cart_items[i])
                full = full + cart_items[i].quantity * cart_items[i].price
        objector = type('objector', (object,), {})
        cartout = objector()
        cartout.full = full
        cartout.items = cart_items_out
        request.session['cart_id'] = cart_id
        request.session['itemsCount'] = len(cart_items_out)
        return render(request, self.template_name, {'out': cartout, 'itemsCount': len(cart_items_out), 'cart_id': cart_id})

    def post(self, request, pk):
        logger.debug("POST debug %s", pk)
        return HttpResponse("CartView", content_type='text/plain')

    def delete(self, request, pk):
        logger.debug("DELETE debug %s", pk)
        return HttpResponse("CartView", content_type='text/plain')

    def put(self, request, pk):
        logger.debug("PUT debug %s", pk)
        return HttpResponse("CartView", content_type='text/plain')
