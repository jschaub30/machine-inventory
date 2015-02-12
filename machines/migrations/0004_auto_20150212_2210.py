# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('machines', '0003_auto_20150212_2048'),
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostname', models.CharField(help_text=b'arlab101', max_length=45)),
                ('description', models.CharField(help_text=b'Power Systems S822L', max_length=45)),
                ('floor', models.IntegerField(null=True)),
                ('room', models.CharField(help_text=b'4F-8', max_length=45, null=True, blank=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True, auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NetworkSpeed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('speed', models.CharField(help_text=b'10G', max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NetworkSwitch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostname', models.CharField(help_text=b'arlab101', max_length=45)),
                ('model_number', models.CharField(help_text=b'arlab101', max_length=45, null=True)),
                ('speed', models.ForeignKey(to='machines.NetworkSpeed')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RackPosition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='position',
        ),
        migrations.DeleteModel(
            name='Equipment',
        ),
        migrations.DeleteModel(
            name='Position',
        ),
        migrations.AddField(
            model_name='machine',
            name='network_switch',
            field=models.ForeignKey(to='machines.NetworkSwitch'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='machine',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='machine',
            name='rack',
            field=models.ForeignKey(to='machines.Rack'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='machine',
            name='rack_position',
            field=models.ForeignKey(to='machines.RackPosition'),
            preserve_default=True,
        ),
    ]
