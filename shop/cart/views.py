import logging
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views import View
from .models import Cart, CartItem, CartState

from userprofile.models import User
from goods.models import Goods
from django.db.models import ObjectDoesNotExist


logger = logging.getLogger(__name__)


class CartView(View):
    def get(self, request, pk):
        logger.debug("GET debug %s", pk)
        return HttpResponse("CartView", content_type='text/plain')

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
    logger.debug("%s", cart_id)

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
def cart_item_inc(request, cartId, goodsId):
    return HttpResponse("CartView", content_type='text/plain')


@login_required
def cart_item_dec(request, cartId, pk):
    return HttpResponse("CartView", content_type='text/plain')

