# Standard library import
from django.urls import path, include

# Local import
from . import views

app_name = 'contact'

urlpatterns = [
    path('contact-us/', views.contact_page, name='contact'),
]