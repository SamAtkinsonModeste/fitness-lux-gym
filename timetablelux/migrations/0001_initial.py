# Generated by Django 4.2.19 on 2025-02-16 04:06

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
            name='FitnessTimetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(choices=[('2025', 'Year 2025'), ('2026', 'Year 2026'), ('2027', 'Year 2027'), ('2028', 'Year 2028'), ('2029', 'Year 2029'), ('2030', 'Year 2030')], default='2025', max_length=4, unique=True)),
                ('month', models.CharField(choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], default='1', max_length=9, unique=True)),
                ('week', models.CharField(choices=[('1', 'Week 1'), ('2', 'Week 2'), ('3', 'Week 3'), ('4', 'Week 4'), ('5', 'Week 5'), ('6', 'Week 6'), ('7', 'Week 7'), ('8', 'Week 8'), ('9', 'Week 9'), ('10', 'Week 10'), ('11', 'Week 11'), ('12', 'Week 12'), ('13', 'Week 13'), ('14', 'Week 14'), ('15', 'Week 15'), ('16', 'Week 16'), ('17', 'Week 17'), ('18', 'Week 18'), ('19', 'Week 19'), ('20', 'Week 20'), ('21', 'Week 21'), ('22', 'Week 22'), ('23', 'Week 23'), ('24', 'Week 24'), ('25', 'Week 25'), ('26', 'Week 26'), ('27', 'Week 27'), ('28', 'Week 28'), ('29', 'Week 29'), ('30', 'Week 30'), ('31', 'Week 31'), ('32', 'Week 32'), ('33', 'Week 33'), ('34', 'Week 34'), ('35', 'Week 35'), ('36', 'Week 36'), ('37', 'Week 37'), ('38', 'Week 38'), ('39', 'Week 39'), ('40', 'Week 40'), ('41', 'Week 41'), ('42', 'Week 42'), ('43', 'Week 43'), ('44', 'Week 44'), ('45', 'Week 45'), ('46', 'Week 46'), ('47', 'Week 47'), ('48', 'Week 48'), ('49', 'Week 49'), ('50', 'Week 50'), ('51', 'Week 51'), ('52', 'Week 52')], default='1', max_length=2, unique=True)),
                ('day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Firday', 'Friday'), ('Staurday', 'Saturday'), ('Sunday', 'Sunday')], default='Monday', max_length=9, unique=True)),
                ('gym_class_time', models.CharField(default='Evening | 18:30')),
                ('gym_class_date', models.DateTimeField(auto_now=True)),
                ('gym_class_duration', models.CharField(default='45 Minutes', max_length=100)),
                ('gym_timetable_schedular', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fitnesstimetable', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
