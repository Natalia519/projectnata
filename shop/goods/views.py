import logging
from django.views.generic import ListView, DetailView
from django.shortcuts import render

from .models import Goods

logger = logging.getLogger(__name__)


class GoodsView(ListView):
    template_name = 'product_list.html'
    model = Goods

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get("cart_id", None)
        logger.debug("=====>>>> cart_id: %s", cart_id)
        itemsCount = self.request.session.get("itemsCount", None)
        logger.debug("=====>>>> itemsCount: %s", itemsCount)
        if cart_id == None:
            logger.debug("=====>>>> itemsCount not found")
            context['itemsCount'] = 0
            context['cart_id'] = 0
        else:
            context['itemsCount'] = itemsCount
            context['cart_id'] = cart_id
        return context

    # def get(self, request, **kwargs):
    #     itemsCount = request.session.get("itemsCount", 0)
    #     cart_id = request.session.get("cart_id", 0)
    #     return render(request, self.template_name, {'itemsCount': itemsCount, 'cartId': cart_id})


class GoodsPropsView(DetailView):
    template_name = 'single-product.html'
    model = Goods

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get("cart_id", None)
        logger.debug("=====>>>> cart_id: %s", cart_id)
        itemsCount = self.request.session.get("itemsCount", None)
        logger.debug("=====>>>> itemsCount: %s", itemsCount)
        if cart_id == None:
            logger.debug("=====>>>> itemsCount not found")
            context['itemsCount'] = 0
            context['cart_id'] = 0
        else:
            context['itemsCount'] = itemsCount
            context['cart_id'] = cart_id
        return context