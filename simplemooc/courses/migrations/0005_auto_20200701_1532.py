# Generated by Django 3.0.6 on 2020-07-01 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_course_about'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['name'], 'verbose_name': 'Curso', 'verbose_name_plural': 'Cursos'},
        ),
    ]
