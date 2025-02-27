# Generated by Django 4.2.19 on 2025-02-17 03:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('luxclasses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LuxGymTimetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=50)),
                ('gym_class_time', models.DateTimeField()),
                ('teacher', models.CharField(max_length=200)),
                ('gym_class_duration', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('gym_class', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gym_classes', to='luxclasses.fitnessclasses')),
                ('gymclass_organiser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gymtimetable_organiser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
