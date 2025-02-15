# Generated by Django 4.2.19 on 2025-02-15 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luxtimetable', '0002_remove_fitnesstimetable_name_of_day_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fitnesstimetable',
            name='gym_class_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='fitnesstimetable',
            name='gym_class_duration',
            field=models.CharField(default='45 Minutes', max_length=100),
        ),
        migrations.AddField(
            model_name='fitnesstimetable',
            name='gym_class_time',
            field=models.CharField(default='Evening | 18:30'),
        ),
    ]
