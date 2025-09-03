from django.db import models
from django.contrib.auth.models import User
from luxclasses.models import FitnessClasses

# Create your models here.


DAYS_OF_WEEK = (
    (0, 'Monday'),
    (1, 'Tuesday'),
    (2, 'Wednesday'),
    (3, 'Thursday'),
    (4, 'Friday'),
    (5, 'Saturday'),
    (6, 'Sunday'),
)

CLASS_DURATION_TIME = (
    (0, '30 Minutes'),
    (1, '45 Minutes'),
    (2, '50 Minutes'),
    (3, '60 Minutes'),
)


class ScheduledClass(models.Model):
    gymclass_organiser = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="gymtimetable_organiser")
    gym_class = models.ForeignKey(
        FitnessClasses, on_delete=models.SET_NULL, null=True, related_name="gym_classes")
    day = models.IntegerField(choices=DAYS_OF_WEEK, default=0)
    gym_class_time = models.TimeField()
    teacher = models.CharField(max_length=200)
    gym_class_duration = models.IntegerField(choices=CLASS_DURATION_TIME, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['day','gym_class_time','created_on']

    def __str__(self):
        return f"{self.get_day_display()} {self.gym_class_time} - Teacher is {self.teacher}"
