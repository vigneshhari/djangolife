# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_account',
            name='mail',
            field=models.CharField(default='vichuhari100@gmail.com', max_length=100),
            preserve_default=False,
        ),
    ]
