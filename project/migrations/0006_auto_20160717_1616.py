# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-07-17 10:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_auto_20160717_1119'),
    ]

    operations = [
        migrations.CreateModel(
            name='Liker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='image',
            name='access_users',
            field=models.CharField(choices=[('Pub', 'Public'), ('Pri', 'Private')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='liker',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Image'),
        ),
        migrations.AddField(
            model_name='liker',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]