# Generated by Django 2.0.4 on 2018-04-27 13:24

import apps.utils.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Personaje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('tipo_personaje', models.CharField(choices=[('HEROE', 'HEROE'), ('VILLANO', 'VILLANO')], max_length=200)),
                ('imagen', models.ImageField(upload_to=apps.utils.utils.user_directory_path)),
                ('imagen_url', models.URLField()),
                ('url', models.URLField()),
                ('descripcion', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='comic',
            name='personajes',
            field=models.ManyToManyField(to='personajes.Personaje'),
        ),
    ]
