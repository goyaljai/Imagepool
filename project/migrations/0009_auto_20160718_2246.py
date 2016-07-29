# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-07-18 17:16
from __future__ import unicode_literals

from django.db import migrations, models
import project.models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_follow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=project.models.get_image_path2),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='profile_picture',
            field=models.FileField(blank=True, null=True, upload_to=project.models.get_image_path),
        ),
    ]