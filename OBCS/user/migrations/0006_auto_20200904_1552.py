# Generated by Django 2.2.14 on 2020-09-04 10:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20200904_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationmodel',
            name='doa',
            field=models.DateField(default=datetime.date(2020, 9, 4)),
        ),
        migrations.AlterField(
            model_name='applicationmodel',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=70),
        ),
    ]
