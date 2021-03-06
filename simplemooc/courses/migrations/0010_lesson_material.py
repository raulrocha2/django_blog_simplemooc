# Generated by Django 3.0.7 on 2020-07-19 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_auto_20200716_0246'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('description', models.TextField(blank=True, verbose_name='Descricao')),
                ('number', models.IntegerField(blank=True, default=0, verbose_name='Numerdo Ordem')),
                ('release_date', models.DateField(blank=True, null=True, verbose_name='Data Liberacao')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em ')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em ')),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lessons', to='courses.Course', verbose_name='Curso')),
            ],
            options={
                'verbose_name': 'Aula',
                'verbose_name_plural': 'Aulas',
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('embedded', models.TextField(blank=True, verbose_name='Video embedded')),
                ('fiel', models.FileField(blank=True, null=True, upload_to='lessons/materials')),
                ('lesson', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='materials', to='courses.Lesson', verbose_name='Aula')),
            ],
            options={
                'verbose_name': 'Material',
                'verbose_name_plural': 'Materiais',
            },
        ),
    ]
