# Standard librarry import
from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=50, blank=True)
    slug = models.SlugField(null=True, blank=True, unique=True)
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)
    price = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('product:detail', args=[self.slug, self.id])