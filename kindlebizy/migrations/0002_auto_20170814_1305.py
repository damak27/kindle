# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-14 07:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kindlebizy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200, null=True)),
                ('Activity', models.TextField(max_length=200, null=True)),
                ('DateOfEvent', models.DateField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='text',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]