from django.test import SimpleTestCase
from django.urls import reverse, resolve
from Account.api import views as api_views
from Account import views


class TestUrls(SimpleTestCase):
    def test_create_new_user(self):
        url = reverse('api_account:sign_up')
        self.assertEqual(resolve(url).func.view_class, api_views.SignUpUser)

    def test_sign_in_user(self):
        url = reverse('api_account:sign_in')
        self.assertEqual(resolve(url).func.view_class, api_views.UserLoginView)

    def test_black_list(self):
        url = reverse('api_account:black_list')
        self.assertEqual(
            resolve(url).func.view_class, api_views.BlacklistTokenUpdateView
        )
    
    def test_sign_up(self):
        url = reverse('account:sign_up')
        self.assertEqual(resolve(url).func.view_class, views.SignUp)

    def test_sign_in(self):
        url = reverse('account:sign_in')
        self.assertEqual(resolve(url).func.view_class, views.SignIn)

    def test_change_password(self):
        url = reverse('account:change_password')
        self.assertEqual(resolve(url).func, views.change_password)

    def test_user_profile(self):
        url = reverse('account:profile')
        self.assertEqual(resolve(url).func.view_class, views.UserProfile)
    
    def test_logout(self):
        url = reverse('account:logout')
        self.assertEqual(resolve(url).func.view_class, views.Logout)

    def test_reset_password(self):
        url = reverse('account:reset')
        self.assertEqual(resolve(url).func.view_class, views.PasswordResetView)

    def test_password_done(self):
        url = reverse('account:done')
        self.assertEqual(resolve(url).func.view_class, views.PasswordDoneView)

    def test_password_confirm(self):
        url = reverse('account:confirm')
        self.assertEqual(
            resolve(url).func.view_class, views.PasswordConfirmView
        )

    def test_password_complete(self):
        url = reverse('account:complete')
        self.assertEqual(
            resolve(url).func.view_class, views.PasswordCompleteView
        )