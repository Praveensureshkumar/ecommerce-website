# Generated by Django 5.1.6 on 2025-04-06 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_index_product_details_product_size_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='index_product_details',
            name='product_price',
        ),
        migrations.AddField(
            model_name='index_product_details',
            name='product_offer_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='index_product_details',
            name='product_original_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
