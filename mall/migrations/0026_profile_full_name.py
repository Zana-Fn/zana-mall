# Generated by Django 5.1.6 on 2025-04-02 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0025_remove_order_customer_remove_order_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='full_name',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]
