# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0002_auto_20150212_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='rack',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
