# Generated by Django 4.0.6 on 2022-08-07 02:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_todoapp', '0005_appuser_alter_task_created_at_alter_task_removed_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 8, 7, 8, 0, 29, 417265), null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='removed_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 8, 7, 8, 0, 29, 417265), null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_file',
            field=models.FileField(blank=True, default=None, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='task',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 8, 7, 8, 0, 29, 417265), null=True),
        ),
    ]
