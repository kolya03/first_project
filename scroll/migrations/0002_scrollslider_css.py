# Generated by Django 3.2.9 on 2021-12-11 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scroll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scrollslider',
            name='css',
            field=models.CharField(default='-', max_length=250, null=True, verbose_name='Осн. картинка'),
        ),
    ]
