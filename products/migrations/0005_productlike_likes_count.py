# Generated by Django 5.0.4 on 2024-04-15 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_author_productlike_product_like_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='productlike',
            name='likes_count',
            field=models.IntegerField(default=0),
        ),
    ]
