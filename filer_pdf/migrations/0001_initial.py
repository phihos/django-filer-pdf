# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='PDF',
            fields=[
                ('file_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='filer.File')),
            ],
            options={
                'abstract': False,
            },
            bases=('filer.file',),
        ),
    ]
