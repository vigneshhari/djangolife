# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField()),
                ('name', models.CharField(max_length=500)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('phone_no', models.IntegerField()),
            ],
        ),
    ]
