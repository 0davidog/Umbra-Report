# Generated by Django 4.2.9 on 2024-01-29 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_alter_report_slug_alter_report_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]