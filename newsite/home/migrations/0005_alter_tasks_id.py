# Generated by Django 4.2.5 on 2023-09-18 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_tasks_done'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]