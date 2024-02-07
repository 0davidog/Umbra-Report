# Generated by Django 4.2.9 on 2024-02-07 10:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0031_delete_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='likes',
            field=models.ManyToManyField(related_name='blogpost_like', to=settings.AUTH_USER_MODEL),
        ),
    ]