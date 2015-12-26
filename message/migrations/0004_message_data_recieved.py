# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0003_delete_user_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='message_data',
            name='recieved',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
