# Generated by Django 2.1.7 on 2019-09-20 22:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0005_auto_20190921_0142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='post_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 21, 4, 20, 45, 46515)),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='post_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 21, 4, 20, 45, 46515)),
        ),
    ]
