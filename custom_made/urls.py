from django.urls import path
from . import views

urlpatterns = [
    path('', views.custom_made_view, name='custom_made_view'),
]
