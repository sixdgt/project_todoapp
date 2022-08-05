# Generated by Django 4.0.6 on 2022-08-03 02:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_todoapp', '0004_alter_task_created_at_alter_task_removed_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'tbl_user',
            },
        ),
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 8, 3, 8, 26, 15, 615868), null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='removed_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 8, 3, 8, 26, 15, 615868), null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 8, 3, 8, 26, 15, 615868), null=True),
        ),
    ]