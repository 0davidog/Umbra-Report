# Generated by Django 4.2.9 on 2024-01-31 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0029_image_related_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='related_post',
        ),
    ]
