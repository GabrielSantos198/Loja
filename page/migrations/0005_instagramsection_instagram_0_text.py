# Generated by Django 4.1.3 on 2022-12-10 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0004_remove_instagramsection_instagram_0_post_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='instagramsection',
            name='instagram_0_text',
            field=models.TextField(default=0),
        ),
    ]
