# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_auto_20151206_1835'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User_Account',
        ),
    ]
