# Generated by Django 2.2.18 on 2022-07-08 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionary', '0006_auto_20220707_1630'),
    ]

    operations = [
        migrations.RenameField(
            model_name='featureresponse',
            old_name='features_answers',
            new_name='response',
        ),
        migrations.RemoveField(
            model_name='qualificationresponse',
            name='qualification_answers',
        ),
        migrations.AddField(
            model_name='qualificationresponse',
            name='answer',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='qualificationresponse',
            name='response',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='qualification_answer', to='questionary.Response'),
        ),
    ]