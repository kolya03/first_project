# Generated by Django 3.2.9 on 2021-12-12 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PriceCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pc_value', models.CharField(max_length=50, verbose_name='Цена карты')),
                ('pc_description', models.CharField(max_length=250, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='PriceTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pt_service', models.CharField(max_length=250, verbose_name='Услуга')),
                ('pt_old_price', models.CharField(max_length=250, verbose_name='Старая цена')),
                ('pt_new_price', models.CharField(max_length=250, verbose_name='Новая цена')),
            ],
        ),
    ]
