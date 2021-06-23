# Standard library import
from django.urls import path

# Local import
from . import views

app_name = 'api_cart'

urlpatterns = [
    path('list/', views.CartListView.as_view(), name='list'),
    path('<int:pk>/', views.CartRetrieveView.as_view(), name='retrive'),
    path('create/', views.CartCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.CartUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.CartDestroyView.as_view(), name='delete'),
]
