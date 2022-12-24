# Generated by Django 4.1.3 on 2022-12-24 02:49

from django.db import migrations, models
import localflavor.br.models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_alter_order_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='cep',
            field=models.CharField(default=1, max_length=8, verbose_name='CEP'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='city',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='complement',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='cpf',
            field=models.CharField(default=1, max_length=11, verbose_name='CPF'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='district',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='number',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='state',
            field=localflavor.br.models.BRStateField(default=1, max_length=2, verbose_name='State'),
            preserve_default=False,
        ),
    ]
