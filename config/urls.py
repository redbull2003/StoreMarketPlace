# Standard library import
from django.contrib import admin
from django.urls import path, include
from django.contrib.admin.sites import AdminSite
from django.conf import settings
from django.conf.urls.static import static

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
    path('', include('Contact.urls', namespace='contact')),
    path('', include('Cart.urls', namespace='cart')),
    path('', include('Order.urls', namespace='order')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('captcha/', include('captcha.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('api/product/', include('Product.api.urls', namespace='api_product')),
    path('api/user/', include('Account.api.urls', namespace='api_account')),
    path('api/contact/', include('Contact.api.urls', namespace='api_contact')),
    path('api/cart/', include('Cart.api.urls', namespace='api_cart')),
    path('api/order/', include('Order.api.urls', namespace='api_order')),
]

if settings.DEBUG:
    urlpatterns += [
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

AdminSite.site_header = 'Administration'
AdminSite.index_title = 'Shop App'
AdminSite.site_title = 'Admin Section'