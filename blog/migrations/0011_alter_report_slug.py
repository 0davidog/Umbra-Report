# Generated by Django 4.2.9 on 2024-01-29 16:39

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_remove_report_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title'),
        ),
    ]