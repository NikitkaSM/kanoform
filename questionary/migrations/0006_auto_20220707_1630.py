# Generated by Django 2.2.18 on 2022-07-07 16:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('questionary', '0005_auto_20220707_1620'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qualificationquestion',
            name='created_time',
        ),
        migrations.AddField(
            model_name='questionary',
            name='created_time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
