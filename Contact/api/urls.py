# Standard library import
from django.urls import path

# Local import
from . import views

app_name = 'api_contact'


urlpatterns = [
    path('list/', views.ContactListAPI.as_view(), name='list'),
    path('<int:pk>/', views.ContactRUDAPI.as_view(), name='rud'),
]