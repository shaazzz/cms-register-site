# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-05 21:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False)),
                ('announce_text', models.CharField(max_length=2000)),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contest_name', models.CharField(max_length=2000)),
                ('start_time', models.DateTimeField(verbose_name='Start')),
                ('duration', models.DurationField()),
                ('cms_id', models.IntegerField(default=0)),
                ('contest_url', models.CharField(default='#', max_length=2000)),
                ('ranking_url', models.CharField(default='#', max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms_register.Contest')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
