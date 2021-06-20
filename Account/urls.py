# Standard-library import
from django.urls import path, include

# Local import
from . import views

app_name = 'account'

urlpatterns = [
    path('sign-up/', views.SignUp.as_view(), name='sign_up'),
    path('sign-in/', views.SignIn.as_view(), name='sign_in'),
    path('log-out/', views.Logout.as_view(), name='logout'),
    path('password-reset/', views.PasswordResetView.as_view(), name='reset'),
    path('password-reset-done/', views.PasswordDoneView.as_view(), name='done'),
    path('password-reset-confirm/',
         views.PasswordConfirmView.as_view(), name='confirm'),
    path('password-reset-complete/',
         views.PasswordCompleteView.as_view(), name='complete'),
    path('user-profile/', views.UserProfile.as_view(), name='profile'),
    path('change-password/', views.change_password, name='change_password'),
]
