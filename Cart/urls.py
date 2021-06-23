# Standard library import
from django.urls import path

# Local import
from . import views

app_name = 'cart'

urlpatterns = [
    path('add-cart/<int:id>/', views.add_cart, name='add'),
    path('remove-cart/<int:id>/', views.cart_remove, name='remove'),
    path('add-detail/', views.cart_detail, name='detail'),
    path('add-single/<int:id>/', views.add_single, name='add_single'),
    path('remove-single/', views.remove_single, name='remove_single'),
]
