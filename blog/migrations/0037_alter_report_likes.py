# Generated by Django 4.2.9 on 2024-02-18 18:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0036_remove_about_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='blogpost_like', to=settings.AUTH_USER_MODEL),
        ),
    ]