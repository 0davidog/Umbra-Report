# Generated by Django 4.2.9 on 2024-01-22 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_report_excerpt_report_updated_on'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='report',
            options={'ordering': ['-updated_on']},
        ),
    ]
