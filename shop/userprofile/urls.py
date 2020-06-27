from django.urls import path
from . import views
# from django.contrib.auth.decorators import login_required

app_name = 'userprofile'
urlpatterns = [
    path('', views.ProfileView.as_view(), name='index'),
    # path('', login_required(views.ProfileView.as_view()), name='index'),
    # path('', views.index, name='index'),
]
