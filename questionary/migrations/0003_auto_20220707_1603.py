# Generated by Django 2.2.18 on 2022-07-07 16:03

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionary', '0002_auto_20220524_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='qualificationquestion',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 7, 16, 3, 26, 195109)),
        ),
        migrations.AlterField(
            model_name='featurequestion',
            name='questionary',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='feature_questions', to='questionary.Questionary'),
        ),
        migrations.AlterField(
            model_name='qualificationquestion',
            name='questionary',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='qualification_questions', to='questionary.Questionary'),
        ),
        migrations.AlterField(
            model_name='questionary',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
