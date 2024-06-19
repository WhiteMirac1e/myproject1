# Generated by Django 5.0.6 on 2024-06-19 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_product_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='count',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество товара'),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='products_photo/'),
        ),
    ]