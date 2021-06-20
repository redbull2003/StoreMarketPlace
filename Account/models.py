# Standard-library import
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
    _user_get_permissions,
    Permission
)
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save


class UserAccountManager(BaseUserManager):
    def create_user(self, username, password):

        if not username:
            raise ValueError(_('You must provide an username'))

        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_superuser(self, username, password):

        """
        Creates and saves a superuser with the given password.
        """
        user = self.create_user(
            username,
            password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=120, unique=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True)
    work_phone_number = models.CharField(max_length=15, blank=True)
    telegram_id = models.CharField(max_length=60, blank=True)
    instagram_id = models.CharField(max_length=60, blank=True)
    telegram_phone_number = models.CharField(max_length=60, blank=True)
    whatsapp_phone_number = models.CharField(max_length=60, blank=True)
    website = models.URLField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    create_account_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)
    accounting_codes = models.TextField(max_length=300, blank=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True, blank=True, null=True)
    picture = models.FileField(upload_to='media/%Y-%m-%d', blank=True)
    institution = models.CharField(max_length=70, blank=True)
    department = models.CharField(max_length=50, blank=True)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)
    skype = models.CharField(max_length=50, blank=True)
    yahoo = models.CharField(max_length=70, blank=True)
    first_access = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    last_access = models.DateTimeField(auto_now=True, null=True, blank=True)
    policy_agreed = models.BooleanField(default=True)
    permission = models.ManyToManyField(Permission, related_name='users')


    objects = UserAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('password',)

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def __str__(self):
        return f"{self.username}"

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
    def get_user_permissions(self, obj=None):
        return _user_get_permissions(self, obj, 'user')
    
    def get_all_permissions(self, obj=None):
        return _user_get_permissions(self, obj, 'all')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}'


def user_profile_save(sender, **kwargs):
    if kwargs['created']:
        user_profile = Profile(user=kwargs['instance'])
        user_profile.save()

post_save.connect(user_profile_save, sender=User)