# Generated by Django 4.1.3 on 2022-12-24 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0018_order_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='is_sent',
            field=models.BooleanField(default=False),
        ),
    ]
