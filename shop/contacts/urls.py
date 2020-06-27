from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required, permission_required


app_name = 'contacts'
urlpatterns = [
    path('',                views.IndexView.as_view(),  name='index'),
    # path('', login_required(views.IndexView.as_view()), name='index'),
]
