# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-27 02:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True, editable=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'My Model',
                'verbose_name_plural': 'My Models',
            },
        ),
        migrations.CreateModel(
            name='MyModelRelated',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True, editable=False)),
                ('title', models.CharField(max_length=255)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'My Model Related',
                'verbose_name_plural': 'My Models Related',
            },
        ),
        migrations.AddField(
            model_name='mymodel',
            name='related',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.MyModelRelated'),
        ),
    ]