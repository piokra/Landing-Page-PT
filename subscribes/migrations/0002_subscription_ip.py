# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscribes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='ip',
            field=models.CharField(default='2015-06-13 20:52:14.743000+00:00 changed format.', max_length=20),
            preserve_default=False,
        ),
    ]
