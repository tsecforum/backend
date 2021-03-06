# Generated by Django 2.2.5 on 2019-09-20 11:11

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('location', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('amount', models.IntegerField(default=0)),
                ('post_date', models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 20, 16, 41, 20, 116500))),
            ],
        ),
        migrations.RemoveField(
            model_name='ngo',
            name='city',
        ),
        migrations.RemoveField(
            model_name='ngo',
            name='state',
        ),
        migrations.AlterField(
            model_name='ngo',
            name='post_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 20, 16, 41, 20, 116500)),
        ),
        migrations.DeleteModel(
            name='Events',
        ),
        migrations.AddField(
            model_name='event',
            name='ngo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ngo.NGO'),
        ),
    ]
