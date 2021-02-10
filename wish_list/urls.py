from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_wish_list, name='view_wish_list'),
]
