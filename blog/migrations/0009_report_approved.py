# Generated by Django 4.2.9 on 2024-01-29 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_report_featured_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]