# Generated by Django 2.1.7 on 2019-09-20 20:12

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ngo', '0004_auto_20190921_0035'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='inquiries',
            name='event',
        ),
        migrations.RemoveField(
            model_name='inquiries',
            name='user',
        ),
        migrations.AlterField(
            model_name='event',
            name='post_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 21, 1, 42, 54, 911200)),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='post_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 21, 1, 42, 54, 911200)),
        ),
        migrations.DeleteModel(
            name='Inquiries',
        ),
        migrations.AddField(
            model_name='volunteer',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ngo.Event'),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='ngo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ngo.NGO'),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='donation',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ngo.Event'),
        ),
        migrations.AddField(
            model_name='donation',
            name='ngo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ngo.NGO'),
        ),
        migrations.AddField(
            model_name='donation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]