# Generated by Django 2.0.4 on 2019-07-03 12:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ccimp_permission_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permissionclass',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 3, 20, 15, 51)),
        ),
        migrations.AlterField(
            model_name='permissionclass',
            name='update_time',
            field=models.DateTimeField(default='', null=True),
        ),
    ]