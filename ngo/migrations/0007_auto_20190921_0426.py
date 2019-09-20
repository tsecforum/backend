# Generated by Django 2.1.7 on 2019-09-20 22:56

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0006_auto_20190921_0420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='event',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ngo.Event'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='ngo',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ngo.NGO'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='post_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 21, 4, 26, 37, 230816)),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='post_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 21, 4, 26, 37, 230816)),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='event',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ngo.Event'),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='ngo',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ngo.NGO'),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]