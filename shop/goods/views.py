import logging
from django.views.generic import ListView, DetailView

from .models import Goods

logger = logging.getLogger(__name__)


class GoodsView(ListView):
    template_name = 'product_list.html'
    model = Goods


class GoodsPropsView(DetailView):
    template_name = 'single-product.html'
    model = Goods
