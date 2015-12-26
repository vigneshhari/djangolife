# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_account_mail'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_account',
            name='vericode',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
