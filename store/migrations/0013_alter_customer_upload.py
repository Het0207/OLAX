# Generated by Django 4.1.7 on 2023-03-05 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_alter_customer_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='upload',
            field=models.ImageField(default='mob1.png', null=True, upload_to='media/'),
        ),
    ]