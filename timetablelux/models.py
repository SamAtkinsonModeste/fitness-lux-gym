from django.db import models
from django.contrib.auth.models import User
from luxclasses.models import FitnessClasses

# Create your models here.


class FitnessTimetable(models.Model):

    YEAR_CHOICES = [(str(i), f"Year {i}") for i in range(2025, 2031)]
    MONTH_CHOICES = [("January", "January"), ("February", "February"), ("March", "March"), ("April", "April"), ("May", "May"), ("June", "June"), (
        "July", "July"), ("August", "August"), ("September", "September"), ("October", "October"), ("November", "November"), ("December", "December"),]
    WEEK_CHOICES = [(str(i), f"Week {i}") for i in range(1, 53)]
    DAY_CHOICES = [("Monday", "Monday"), ("Tuesday", "Tuesday"), ("Wednesday", "Wednesday"),
                   ("Thursday", "Thursday"), ("Firday", "Friday"), ("Staurday", "Saturday"), ("Sunday", "Sunday")]

    gym_timetable_schedular = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True,  related_name="fitnesstimetable")
    user_books = models.ForeignKey(
        User, on_delete=models.CASCADE, default="1", related_name="booked_classes")
    year = models.CharField(
        max_length=4, choices=YEAR_CHOICES, default="2025", unique=True)
    month = models.CharField(
        max_length=9, choices=MONTH_CHOICES, default="1", unique=True)
    week = models.CharField(
        max_length=2, choices=WEEK_CHOICES, default="1", unique=True)
    day = models.CharField(max_length=9, choices=DAY_CHOICES,
                           default="Monday", unique=True)
    gym_class = models.ForeignKey(
        FitnessClasses, on_delete=models.SET_NULL, null=True,  related_name="fitnessclasses")
    gym_class_time = models.CharField(default="Evening | 18:30")
    gym_class_date = models.DateTimeField(auto_now=True)
    gym_class_duration = models.CharField(
        max_length=100, default="45 Minutes")

    def __str__(self):
        return f"{self.year} | {self.month} | {self.week} | {self.day} | {self.gym_class_time}"
