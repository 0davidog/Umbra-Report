# Generated by Django 4.2.9 on 2024-02-19 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0037_alter_report_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='excerpt',
            new_name='description',
        ),
    ]
