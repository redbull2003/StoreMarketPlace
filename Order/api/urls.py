# Standard library import
from django.urls import path

# Local import
from . import views

app_name = 'api_order'

urlpatterns = [
    path('list/', views.OrderListView.as_view(), name='list'),
    path('<int:pk>/', views.OrderRetrieveView.as_view(), name='retrive'),
    path('create/', views.OrderCreateView.as_view(), name='create'),
    path('create-item/', views.OrderItemCreateView.as_view(), name='create_item'),
    path('update/<int:pk>/', views.OrderUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.OrderDestroyView.as_view(), name='delete'),
]
