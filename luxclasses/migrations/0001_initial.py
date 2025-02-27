# Generated by Django 4.2.19 on 2025-02-16 02:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FitnessClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gym_class_name', models.CharField(max_length=200, unique=True)),
                ('short_bullets_gymclassname', models.SlugField(max_length=200, unique=True)),
                ('gym_class_name_extension', models.CharField(blank=True, max_length=200)),
                ('content', models.TextField()),
                ('filename', models.CharField(blank=True, max_length=255, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('0', 'Draft'), ('1', 'Publish')], default='0')),
                ('excerpt', models.TextField(blank=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('gymclass_creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fitnessclasses', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
