# Generated by Django 2.2.5 on 2019-09-20 11:02

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NGO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('phone_number', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=300)),
                ('state', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True)),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('is_verified', models.BooleanField(default=False)),
                ('post_date', models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 20, 16, 32, 45, 349500))),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('location', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('amount', models.IntegerField(default=0)),
                ('post_date', models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 20, 16, 32, 45, 351500))),
                ('ngo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ngo.NGO')),
            ],
        ),
    ]
