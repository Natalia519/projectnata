import logging

from django.core.serializers import json
from django.shortcuts import render
from django.template.defaultfilters import register
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import Cart, CartItem, CartState

from userprofile.models import User
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
                cart = Cart.objects.get(userId=user_id)
                cart_id = cart.pk
        except ObjectDoesNotExist as e:
            logger.debug("exception: %s", e)
            cart = None
        logger.debug("cart: %s", cart)
        try:
            cart_items = CartItem.objects.filter(cartId=cart_id)
        except ObjectDoesNotExist as e:
            logger.debug("exception: %s", e)
            cart_items = None

        logger.debug("cart_item: %s", cart_items)
        full = 0
        for i in range(len(cart_items)):
            cart_items[i].product = Product.objects.get(name=cart_items[i].goodsId)
            cart_items[i].quantity = int(cart_items[i].quantity)
            cart_items[i].goods = Goods.objects.get(productId=cart_items[i].product.pk)
            full = full + cart_items[i].quantity * cart_items[i].price
        objector = type('objector', (object,), {})
        cartout = objector()
        cartout.full = full
        cartout.items = cart_items
        logger.debug("cart_item 2: %s", cart_items)

        return render(request, self.template_name, {'cartout': cartout})

    def post(self, request, pk):
        logger.debug("POST debug %s", pk)
        return HttpResponse("CartView", content_type='text/plain')

    def delete(self, request, pk):
        logger.debug("DELETE debug %s", pk)
        return HttpResponse("CartView", content_type='text/plain')

    def put(self, request, pk):
        logger.debug("PUT debug %s", pk)
        return HttpResponse("CartView", content_type='text/plain')


@login_required
def cart_item_add(request, goods_id):
    cart = None
    cart_id = request.session.get("cart_id", None)
    logger.debug("cart_item_add cart_id: %s, goods_id: %s", cart_id, goods_id)

    try:
        cart = Cart.objects.get(pk=cart_id)
    except ObjectDoesNotExist as e:
        cart_id = None

    if not cart_id:
        cart = Cart(
            docStateId=CartState.objects.get(pk=0),
            userId=User.objects.get(pk=request.user.id),
            employeeUserId=User.objects.get(pk=request.user.id),
            comment="New order")
        cart.save()
        cart_id = cart.pk
        request.session["cart_id"] = cart_id

    goods = Goods.objects.get(pk=goods_id)
    price = goods.price

    try:
        cart_item = CartItem.objects.get(goodsId=goods_id)
        cart_item.quantity += 1
    except ObjectDoesNotExist as e:
        cart_item = None

    if not cart_item:
        cart_item = CartItem(
            cartId=cart,
            goodsId=goods,
            quantity=1,
            price=price
        )
    cart_item.save()

    return HttpResponse(
        {
            cart_item: cart_item.pk
        },
        content_type='application/json')


@login_required
def cart_item_inc_dec(request, quantity, goodsId):
    cart_id = request.session.get("cart_id", None)
    logger.debug("cart_item_inc cartId: %s, goodsId: %s, quantity: %s", cart_id, goodsId, quantity)
    if request.method == "POST" or request.method == "GET":
        try:
            cart = Cart.objects.get(pk=cart_id)
        except ObjectDoesNotExist as e:
            logger.debug("exception: %s", e)
            cart = None
        logger.debug("cart: %s", cart)
        try:
            cart_items = CartItem.objects.filter(cartId=cart_id)
        except ObjectDoesNotExist as e:
            logger.debug("exception: %s", e)
            cart_items = None

        logger.debug("cart_item: %s", cart_items)
        full = 0
        item = 0
        logger.debug("goodsId: %s", goodsId)

        for i in range(len(cart_items)):
            cart_items[i].quantity = int(cart_items[i].quantity)
            product = Product.objects.get(name=cart_items[i].goodsId)
            logger.debug("cart_items[i].goodsId: %s", product.pk)
            if goodsId == product.pk:
                goods = Goods.objects.get(productId=product.pk)
                if quantity > goods.quantity:
                    quantity = goods.quantity
                if quantity < 0:
                    quantity = 0

                cart_items[i].quantity = quantity
                cart_items[i].save()
                item = cart_items[i].quantity * cart_items[i].price
            full = full + cart_items[i].quantity * cart_items[i].price
    logger.debug("out.full: %s, out.item: %s", full, item)
    return JsonResponse({'full': full, 'item': item, 'quantity': quantity})
