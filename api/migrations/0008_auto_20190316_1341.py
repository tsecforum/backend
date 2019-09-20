# Generated by Django 2.1.7 on 2019-03-16 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20190316_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scholarship',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='physically_challenged',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=10),
        ),
    ]
