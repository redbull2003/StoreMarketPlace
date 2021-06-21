# Standard-library import
from django.urls import path

# Local import
from . import views

app_name = 'api_account'

urlpatterns = [
    path('sign-up/', views.UserSignUpView.as_view(), name="sign_up"),
    path('sign-in/', views.UserLoginView.as_view(), name='sign_in'),
    path('logout/blacklist/',
        views.BlacklistTokenUpdateView.as_view(), name='black_list'),
    path('list/', views.UsersListView.as_view(), name='list'),
    path('list/<int:pk>/', views.UserRetrieveView.as_view(), name='retrieve'),
    path('update/<int:pk>/', views.UserUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.UserDeleteView.as_view(), name='delete'),
    path('change-password/', views.UserChangePassword.as_view(), name='change-pass')
]