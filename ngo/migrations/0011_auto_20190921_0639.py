# Generated by Django 2.1.7 on 2019-09-21 01:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0010_auto_20190921_0637'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ngo',
            old_name='url',
            new_name='pic_url',
        ),
        migrations.AlterField(
            model_name='event',
            name='post_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 21, 6, 38, 54, 539207)),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='post_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 21, 6, 38, 54, 539207)),
        ),
    ]
