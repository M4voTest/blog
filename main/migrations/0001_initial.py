# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-07 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=200)),
                ('article_text', models.TextField()),
                ('article_author', models.CharField(max_length=200)),
                ('article_pub_date', models.DateTimeField()),
            ],
        ),
    ]