# Generated by Django 5.0.4 on 2024-04-15 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_productlike_likes_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productlike',
            name='likes_count',
        ),
    ]
