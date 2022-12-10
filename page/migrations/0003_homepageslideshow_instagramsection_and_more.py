# Generated by Django 4.1.3 on 2022-12-10 00:00

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_editpagefields_instagram_0_post_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageSlideShow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('slide_0_title', models.CharField(max_length=40)),
                ('slide_1_title', models.CharField(max_length=40)),
                ('slide_2_title', models.CharField(max_length=40)),
                ('slide_0_text', models.CharField(max_length=100)),
                ('slide_1_text', models.CharField(max_length=100)),
                ('slide_2_text', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InstagramSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('instagram_0_post', models.ImageField(blank=True, default='no_image', upload_to='instagram/%Y/%m/%d')),
                ('instagram_1_post', models.ImageField(blank=True, default='no_image', upload_to='instagram/%Y/%m/%d')),
                ('instagram_2_post', models.ImageField(blank=True, default='no_image', upload_to='instagram/%Y/%m/%d')),
                ('instagram_3_post', models.ImageField(blank=True, default='no_image', upload_to='instagram/%Y/%m/%d')),
                ('instagram_4_post', models.ImageField(blank=True, default='no_image', upload_to='instagram/%Y/%m/%d')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='EditPageFields',
        ),
    ]
