# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='position',
            name='vertical',
        ),
        migrations.AddField(
            model_name='position',
            name='floor',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='position',
            name='position',
            field=models.CharField(help_text=b"'31' or '6G001'", max_length=45, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='position',
            name='room',
            field=models.CharField(help_text=b'4F-8', max_length=45, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='position',
            name='rack',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
