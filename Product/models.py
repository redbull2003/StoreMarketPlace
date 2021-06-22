# Standard librarry import
from django.db import models
from django.db.models import fields
from django.utils.text import slugify
from django.urls import reverse
from django.utils.html import format_html


class TimeStamp(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.created.strftime('%Y-%m-%d')}"


class Product(TimeStamp):
    title = models.CharField(max_length=50, blank=True)
    slug = models.SlugField(null=True, blank=True, unique=True)
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)
    unit_price = models.PositiveIntegerField(null=True, blank=True)
    amount = models.PositiveIntegerField(null=True, blank=True)
    discount = models.PositiveIntegerField(null=True, blank=True)
    total_price = models.PositiveIntegerField(null=True, blank=True)
    image = models.FileField(upload_to='files/image_product', null=True, blank=True)
    sell = models.PositiveIntegerField(default=0)

    class Meta(TimeStamp.Meta):
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('product:detail', args=[self.slug, self.id])
    
    @property
    def get_total_price(self):
        if not self.discount:
            return self.unit_price
        elif self.discount:
            total = (self.discount * self.unit_price) / 100
            return int(self.unit_price - total)
        return self.total_price

    def image_thumbnail(self):
        return format_html("<img src='{}' width=77>".format(self.image.url))
    image_thumbnail.short_description = 'image'