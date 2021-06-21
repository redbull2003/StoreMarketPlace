# Standard library import
from django.contrib.messages.api import success
from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required

# Local import
from .models import User
from .forms import (
    SignInForm,
    SignUpForm,
    UserProfileform,
)


class SignUp(View):
    form_class = SignUpForm

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        form = self.form_class()
        return render(request, '', {'form': form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                username=data['username'],
                password=data['password'],
            )
            user.save()
            messages.success(request, 'با موفقیت ثبت نام شدید')
            return redirect('account:sign-in')
        return render(request, '', {'form': form})


class SignIn(View):
    form_class = SignInForm

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        form = self.form_class()
        return render(request, '', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            human = True
            data = form.cleaned_data
            remember = form.cleaned_data.get('remember')
            user = authenticate(
                request, username=data['username'], password=data['passwrod']
            )
            if user is not None:
                login(request, user)
                if not remember:
                    request.session.set_expiry(0)
                else:
                    request.session.set_expiry(86400)
                return redirect('/')
            else:
                form.add_error('username', 'نام کاربری یا رمز عبور اشتباه است')
        else:
            messages.error(request, 'Invalid recaptcha')
        return render(request, '', {'form': form})


class Logout(LoginRequiredMixin, View):
    login_url = 'account:sign-in'

    def get(self, request):
        logout(request)
        messages.success(request, 'با موفقیت خارج شدید')
        return redirect('/')


class PasswordResetView(auth_views.PasswordResetView):
    template_name = ''
    email_template_name = ''
    success_url = reverse_lazy('account:done')

    def form_valid(self, form):
        messages.success(request, 'ایمیل بازیابی رمز عبور به شما ارسال شد', 'success')
        return super().form_valid(form)


class PasswordConfirmView(auth_views.PasswordResetConfirmView):
    template_name = ''
    success_url = reverse_lazy('account:complete')

    def form_valid(self, form):
        messages.success(request, 'رمز عبور شما با موفیقت تغییر یافت', 'success')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(request, 'دوباره تلاش کنید', 'danger')
        return super().form_invalid(form)


class UserProfile(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    login_url = 'account:sign-in'
    model = User
    form_class = UserProfileform
    success_url = reverse_lazy('account:profile')
    success_message = 'پروفایل کاربری با موفقیت بروزرسانی شد'

    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)


@login_required(login_url='account:sign-in')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'رمز عبور شما با موفقیت تغییر یافت')
            return redirect('change_password')
        else:
            messages.error(request, 'رمز عبور اشتباه است یا مطابقت ندارند')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, '', {'form': form})