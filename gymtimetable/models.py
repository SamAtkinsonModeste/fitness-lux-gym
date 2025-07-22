from django.db import models
from django.contrib.auth.models import User
from luxclasses.models import FitnessClasses

# Create your models here.


DAYS_OF_WEEK = [
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
]


class ScheduledClass(models.Model):
    gymclass_organiser = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="gymtimetable_organiser")
    gym_class = models.ForeignKey(
        FitnessClasses, on_delete=models.SET_NULL, null=True, related_name="gym_classes")
    day = models.CharField(choices=DAYS_OF_WEEK, default="Monday")
    gym_class_time = models.TimeField()
    teacher = models.CharField(max_length=200)
    gym_class_duration = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['day','gym_class_time','created_on']

    def __str__(self):
        return f"{self.day} - Teacher is {self.teacher}"
