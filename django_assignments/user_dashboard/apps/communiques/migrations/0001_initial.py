# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-30 15:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_auto_20180329_1252'),
    ]

    operations = [
        migrations.CreateModel(
            name='Communique',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('msg_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='written_msgs', to='users.User')),
                ('msg_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_msgs', to='users.User')),
            ],
        ),
    ]
