# Generated by Django 4.2.9 on 2024-01-29 15:10

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_report_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='Related Image'),
        ),
    ]
