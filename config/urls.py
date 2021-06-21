# Standard library import
from django.contrib import admin
from django.urls import path, include
from django.contrib.admin.sites import AdminSite

# Third-party import
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    path('secret-panel/', admin.site.urls),
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('admin/defender/', include('defender.urls')),
    path('jet/', include('jet.urls', 'jet')), 
    path('account/', include('Account.urls', namespace='account')),
    path('', include('Product.urls', namespace='product')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('captcha/', include('captcha.urls')),
    path('api/user/', include('Account.api.urls', namespace='api_account')),
    path('api/product/', include('Product.api.urls', namespace='api_product')),
]

AdminSite.site_header = 'Administration'
AdminSite.index_title = 'Shop App'
AdminSite.site_title = 'Admin Section'