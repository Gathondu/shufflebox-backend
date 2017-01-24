# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-24 20:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrownBag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True)),
                ('status', models.CharField(default='not done', max_length=20)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Profile')),
            ],
        ),
    ]