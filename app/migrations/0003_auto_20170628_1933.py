# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 19:33
from __future__ import unicode_literals

import app.current_user
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_snippet'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='snippet',
            options={'get_latest_by': 'modified_at', 'ordering': ('-modified_at', '-created_at')},
        ),
        migrations.RenameField(
            model_name='snippet',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='snippet',
            old_name='modified',
            new_name='modified_at',
        ),
        migrations.AddField(
            model_name='snippet',
            name='modified_by',
            field=models.ForeignKey(default=app.current_user.get_current_user, on_delete=django.db.models.deletion.CASCADE, related_name='modified_by', related_query_name='modified_by', to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='created_by',
            field=models.ForeignKey(default=app.current_user.get_current_user, on_delete=django.db.models.deletion.CASCADE, related_name='created_by', related_query_name='created_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
