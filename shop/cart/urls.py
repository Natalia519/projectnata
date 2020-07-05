from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('<int:pk>/', login_required(views.CartView.as_view()), name='index'),
    # path('<int:pk>/', login_required(views.CartViews.as_view()), name='index'),
    path('item/add/<int:goods_id>/', views.cart_item_add, name='cartItemAdd'),
    path('<int:cartId>/item/inc/<int:goodsId>/', views.cart_item_inc, name='cartItemInc'),
    path('<int:cartId>/item/dec/<int:goodsId>/', views.cart_item_dec, name='cartItemDec'),
    # path('<slug:slug>/', views.GoodsPropsView.as_view(), name='props'),
]
