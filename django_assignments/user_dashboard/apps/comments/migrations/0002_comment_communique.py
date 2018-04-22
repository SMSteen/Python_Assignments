# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-30 15:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comments', '0001_initial'),
        ('communiques', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='communique',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='communiques.Communique'),
        ),
    ]