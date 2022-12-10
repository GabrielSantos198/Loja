# Generated by Django 4.1.3 on 2022-12-09 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='editpagefields',
            name='instagram_0_post',
            field=models.ImageField(blank=True, default='no_image', upload_to='instagram/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='editpagefields',
            name='instagram_1_post',
            field=models.ImageField(blank=True, default='no_image', upload_to='instagram/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='editpagefields',
            name='instagram_2_post',
            field=models.ImageField(blank=True, default='no_image', upload_to='instagram/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='editpagefields',
            name='instagram_3_post',
            field=models.ImageField(blank=True, default='no_image', upload_to='instagram/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='editpagefields',
            name='instagram_4_post',
            field=models.ImageField(blank=True, default='no_image', upload_to='instagram/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='editpagefields',
            name='slide_0_text',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='editpagefields',
            name='slide_0_title',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='editpagefields',
            name='slide_1_text',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='editpagefields',
            name='slide_1_title',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='editpagefields',
            name='slide_2_text',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='editpagefields',
            name='slide_2_title',
            field=models.CharField(max_length=40),
        ),
    ]
