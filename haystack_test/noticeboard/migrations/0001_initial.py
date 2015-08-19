# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150)),
                ('body', models.TextField(blank=True)),
                ('pubdate', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('organization', models.CharField(max_length=3, choices=[(b'KIN', b'KIN'), (b'SSA', b'SUST Science Arena'), (b'DIK', b'Dik Theater')])),
            ],
            options={
                'ordering': ['-pubdate'],
                'verbose_name': 'Notice',
                'verbose_name_plural': 'Notice Board',
            },
        ),
    ]
