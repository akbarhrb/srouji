# Generated by Django 4.2.5 on 2023-09-16 11:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=500)),
                ('timeCreated', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]