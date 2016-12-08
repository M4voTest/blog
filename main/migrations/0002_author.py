# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-08 07:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Author_name', models.CharField(max_length=200)),
                ('Author_description', models.TextField()),
                ('Author_photo', models.ImageField(upload_to='authors')),
            ],
        ),
    ]
