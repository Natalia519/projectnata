from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('<int:pk>/', login_required(views.CartView.as_view()), name='index'),
]
