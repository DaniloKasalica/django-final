# Generated by Django 3.1.6 on 2021-03-09 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20210309_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_image',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productimages', to='product.product'),
        ),
    ]
