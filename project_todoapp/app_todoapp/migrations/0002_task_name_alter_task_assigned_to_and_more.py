# Generated by Django 4.0.6 on 2022-07-31 02:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='assigned_to',
            field=models.EmailField(default=None, max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 31, 8, 25, 3, 197882)),
        ),
        migrations.AlterField(
            model_name='task',
            name='removed_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 31, 8, 25, 3, 197882), null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 31, 8, 25, 3, 197882), null=True),
        ),
    ]
