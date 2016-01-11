# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nombre', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Comentario', models.TextField()),
                ('Estado', models.CharField(max_length=1, choices=[(b'0', b'Desactivado'), (b'1', b'Activado')])),
                ('Nombre', models.CharField(max_length=200, null=True, blank=True)),
                ('Email', models.EmailField(max_length=254)),
                ('Fecha', models.DateTimeField(auto_now_add=True)),
                ('Apellidos', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Titulo', models.CharField(max_length=200)),
                ('SubTitulo', models.CharField(max_length=500, null=True, blank=True)),
                ('Contenido', models.TextField()),
                ('Etiquetas', models.CharField(max_length=100, null=True, blank=True)),
                ('Imagen', models.ImageField(null=True, upload_to=b'img', blank=True)),
                ('Fecha', models.DateTimeField(auto_now_add=True)),
                ('Estado', models.CharField(max_length=1, choices=[(b'0', b'Desactivado'), (b'1', b'Activado')])),
                ('Autor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('Categoria', models.ManyToManyField(to='blog.Categoria', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='comentarios',
            name='Noticia',
            field=models.ForeignKey(to='blog.Noticia'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='comentarios',
            unique_together=set([('Email', 'Fecha')]),
        ),
    ]
