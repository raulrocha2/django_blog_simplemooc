# Generated by Django 3.0.8 on 2020-08-11 03:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='replay',
            name='thread',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='replies', to='forum.Thread', verbose_name='Topico'),
        ),
    ]
