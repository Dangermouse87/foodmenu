# Generated by Django 4.2.2 on 2023-07-24 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.CharField(max_length=500),
        ),
    ]
