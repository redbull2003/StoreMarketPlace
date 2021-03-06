# Standard librarry import
from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.utils.html import format_html

# Third-party import
from tinymce import models as tinymce_models
from rest_framework.reverse import reverse as api_reverse


class Category(models.Model):
    title = models.CharField(max_length=50, blank=True)
    slug = models.SlugField(null=True, blank=True, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class TimeStamp(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.created.strftime('%Y-%m-%d')}"


class Product(TimeStamp):
    title = models.CharField(max_length=50, blank=True, null=True)
    slug = models.SlugField(null=True, blank=True, unique=True)
    description = tinymce_models.HTMLField()
    available = models.BooleanField(default=True)
    unit_price = models.PositiveIntegerField(null=True, blank=True)
    amount = models.PositiveIntegerField(null=True, blank=True)
    discount = models.PositiveIntegerField(null=True, blank=True)
    total_price = models.PositiveIntegerField(null=True, blank=True)
    image = models.FileField(upload_to='files/image_product/%Y-%m-%d', default='1.jpg')
    sell = models.PositiveIntegerField(default=0)
    category = models.ManyToManyField(Category, blank=True)

    class Meta(TimeStamp.Meta):
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('product:detail', args=[self.slug, self.id])

    def get_api_url(self, request=None):
        return api_reverse('api_product:retrieve', kwargs={'pk': self.pk}, request=request)
    
    @property
    def get_total_price(self):
        if not self.discount:
            return self.unit_price
        elif self.discount:
            total = (self.discount * self.unit_price) / 100
            return int(self.unit_price - total)
        return self.total_price

    def image_thumbnail(self):
        return format_html('<img src="{}" width=77>'.format(self.image.url))
    image_thumbnail.short_description = 'image'

    def category_to_str(self):
        return ', '.join([category.title for category in self.category.all()])
    
    category_to_str.short_description = 'Category/Categories'