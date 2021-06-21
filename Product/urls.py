# Standard library import
from django.urls import path

# Local import
from . import views

app_name = 'product'

urlpatterns = [
    path('products/list/', views.product_list, name='list'),
    path('product/<slug:slug>/<int:id>/', views.product_detail, name='detail'),
]