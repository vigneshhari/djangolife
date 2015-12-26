# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_account_vericode'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_account',
            name='verified',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
