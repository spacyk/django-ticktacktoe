# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-02 12:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tictactoe', '0003_invitation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='message',
            field=models.CharField(blank=True, max_length=300, verbose_name='Optional Message'),
        ),
        migrations.AlterField(
            model_name='invitation',
            name='to_user',
            field=models.ForeignKey(help_text='Please select the user you want to play with', on_delete=django.db.models.deletion.CASCADE, related_name='invitation_to', to=settings.AUTH_USER_MODEL, verbose_name='User to invite'),
        ),
    ]