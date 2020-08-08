from django.urls import path
from . import views

app_name = 'goods'
urlpatterns = [
    path('', views.GoodsView.as_view(), name='index'),
    path('<int:pk>/', views.GoodsPropsView.as_view(), name='details'),
]
