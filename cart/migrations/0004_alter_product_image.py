# Generated by Django 4.1.5 on 2023-01-26 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0003_alter_product_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="products/"),
        ),
    ]
