# Generated by Django 4.1.3 on 2022-12-23 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_remove_item_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]