# Generated by Django 4.2.5 on 2023-09-17 11:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_tasks_timecreated_alter_tasks_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='timeCreated',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]