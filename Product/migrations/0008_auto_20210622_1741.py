# Generated by Django 3.1.1 on 2021-06-22 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0007_auto_20210622_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(default='1.jpg', upload_to='files/image_product/%Y-%m-%d'),
        ),
    ]
