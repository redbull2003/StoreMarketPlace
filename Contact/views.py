# Standard library import
from django.shortcuts import render, redirect
from django.contrib import messages

# Local import
from .models import Contact
from .forms import ContactForm


def contact_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Contact.objects.create(
                name=data['name'], email=data['email'],
                subject=data['subject'], body=data['body']
            )
            messages.success(request, 'تشکر بابت ارسال نظر شما', 'success')
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, 'خطایی رخ داده است', 'danger')
        return redirect(request, '', {'form': form})