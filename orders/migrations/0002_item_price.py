# Generated by Django 4.1.3 on 2022-12-23 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.FloatField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
