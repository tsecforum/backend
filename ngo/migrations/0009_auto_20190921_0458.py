# Generated by Django 2.1.7 on 2019-09-20 23:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0008_auto_20190921_0428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='post_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 21, 4, 58, 39, 276522)),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='post_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 21, 4, 58, 39, 276522)),
        ),
    ]
