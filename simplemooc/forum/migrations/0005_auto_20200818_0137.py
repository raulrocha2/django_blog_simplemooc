# Generated by Django 3.0.8 on 2020-08-18 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_auto_20200818_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='slug',
            field=models.SlugField(blank=True, unique=True, verbose_name='Identificador'),
        ),
    ]
