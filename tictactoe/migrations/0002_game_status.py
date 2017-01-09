# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-26 15:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tictactoe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='status',
            field=models.CharField(choices=[('A', 'Active'), ('F', 'First Player Wins'), ('S', 'Second Player Wins'), ('D', 'Draw')], default='A', max_length=1),
        ),
    ]