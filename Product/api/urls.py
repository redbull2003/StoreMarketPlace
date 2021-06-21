# Standard-library import
from django.urls import path

# Local import
from . import views

app_name = 'api_product'

urlpatterns = [
    path('list/', views.ProductListView.as_view(), name="list"),
    path('<int:pk>/', views.ProductRetrieveView.as_view(), name='retrieve'),
    path('create/', views.ProductCreateView.as_view(), name="create"),
    path('update/<int:pk>/', views.ProductUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.ProductDestroyView.as_view(), name="delete"),
]