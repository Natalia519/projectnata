from asgiref.server import logger
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, render
from django.views import generic

# from django.contrib.auth.decorators import login_required, permission_required
# from django.http import HttpResponsePermanentRedirect

# @login_required()
from cart.models import Cart, CartItem, CartState
from userprofile.models import User


def index(request):
    itemsCount = request.session.get("itemsCount", 0)
    cart_id = request.session.get("cart_id", None)
    if request.user.is_authenticated:
        if cart_id == None:
            user_id = request.session.get("_auth_user_id", None)
            logger.debug("user_id: %s", user_id)
        try:
            if cart_id != None:
                cart = Cart.objects.get(pk=cart_id)
            else:
                index = 0
                carts_all = Cart.objects.filter(userId=user_id)
                if len(carts_all) > 0:
                    for v in carts_all:
                        if index < v.pk:
                            index = v.pk
                            cart = v
                else:
                    cart = Cart(
                        docStateId=CartState.objects.get(pk=0),
                        userId=User.objects.get(pk=request.user.id),
                        employeeUserId=User.objects.get(pk=request.user.id),
                        comment="New order")
                    cart.save()
                cart_id = cart.pk
        except ObjectDoesNotExist as e:
            logger.debug("exception: %s", e)
        request.session['cart_id'] = cart_id
        logger.debug("cart: %s", cart)
        try:
            cart_items = CartItem.objects.filter(cartId=cart_id)
        except ObjectDoesNotExist as e:
            logger.debug("exception: %s", e)
            cart_items = None
        itemsCount = len(cart_items)
        request.session['itemsCount'] = itemsCount
        request.session['cart_id'] = cart_id
        return render(request, 'index.html', {'itemsCount': itemsCount, 'cart_id': cart_id})

    else:
    #     return HttpResponsePermanentRedirect("/accounts/login/")
        return render(request, 'index.html', {'itemsCount': itemsCount, 'cart_id': cart_id})

# class IndexView(generic.ListView):
#     template_name = 'index.html'
#
#     def get_queryset(self):
#         """
#         Return the last five published questions (not including those set to be
#         published in the future).
#         """
#         return ""


class ContactsView(generic.ListView):
    template_name = 'index.html'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return ""
