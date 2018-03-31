# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-30 22:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('communiques', '0001_initial'),
        ('comments', '0003_auto_20180330_1733'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='message',
        ),
        migrations.AddField(
            model_name='comment',
            name='communique',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='communiques', to='communiques.Communique'),
            preserve_default=False,
        ),
    ]
