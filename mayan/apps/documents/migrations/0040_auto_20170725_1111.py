# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-25 11:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0039_duplicateddocument'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='documentversion',
            options={'ordering': ('timestamp',), 'verbose_name': 'Document version', 'verbose_name_plural': 'Document version'},
        ),
    ]