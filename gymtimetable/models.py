from django.db import models
from django.contrib.auth.models import User
from luxclasses.models import FitnessClasses

# Create your models here.


class LuxGymTimetable(models.Model):
    gymclass_organiser = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="gymtimetable_organiser")
    gym_class = models.ForeignKey(
        FitnessClasses, on_delete=models.SET_NULL, null=True, related_name="gym_classes")
    day = models.CharField(max_length=50)
    gym_class_time = models.DateTimeField()
    teacher = models.CharField(max_length=200)
    gym_class_duration = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"{self.day} - Teacher is {self.teacher}"
