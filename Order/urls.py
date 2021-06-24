# Standard library import
from django.urls import path

# Local import
from . import views

app_name = 'order'

urlpatterns = [
    path('order-detail/<int:id>/', views.order_detail, name='detail'),
    path('create-order/', views.create_order, name='create'),
]