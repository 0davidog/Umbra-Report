# Generated by Django 4.2.9 on 2024-01-29 16:53

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_report_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, max_length=200, populate_from='title'),
        ),
    ]
