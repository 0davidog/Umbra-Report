# Generated by Django 4.2.9 on 2024-01-29 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_report_approved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='approved',
        ),
    ]