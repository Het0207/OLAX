# Generated by Django 4.1.7 on 2023-03-05 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_alter_products_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
    ]