# Generated by Django 4.2.9 on 2024-01-31 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='related_post',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='subject', to='blog.report'),
        ),
    ]
