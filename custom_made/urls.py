from django.urls import path
from . import views

urlpatterns = [
    path('<int:product_id>/', views.custom_made_view, name='custom_made_view'),
]
