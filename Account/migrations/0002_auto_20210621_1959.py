# Generated by Django 3.1.1 on 2021-06-21 19:59

import Account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, validators=[Account.models.phone_validate]),
        ),
    ]