from django.db import models
from django.contrib.auth.models import User
from luxclasses.models import FitnessClasses

# Create your models here.


DAYS_OF_WEEK = (
    (0, "Monday"),
    (1, "Tuesday"),
    (2, "Wednesday"),
    (3, "Thursday"),
    (4, "Friday"),
    (5, "Saturday"),
    (6, "Sunday"),
)

CLASS_DURATION_TIME = (
    (0, "30 Minutes"),
    (1, "45 Minutes"),
    (2, "50 Minutes"),
    (3, "60 Minutes"),
)

CLASS_TIMES = (
    (0, "09:00 AM"),
    (1, "09:30 AM"),
    (2, "10:00 AM"),
    (3, "10:30 AM"),
    (4, "11:00 AM"),
    (5, "11:30 AM"),
    (6, "12:00 PM"),
    (7, "12:30 PM"),
    (8, "01:00 PM"),
    (9, "01:30 PM"),
    (10, "02:00 PM"),
    (11, "02:30 PM"),
    (12, "03:00 PM"),
    (13, "03:30 PM"),
    (14, "04:00 PM"),
    (15, "04:30 PM"),
    (16, "05:00 PM"),
    (17, "05:30 PM"),
    (18, "06:00 PM"),
    (19, "06:30 PM"),
    (20, "07:00 PM"),
    (21, "07:30 PM"),
    (22, "08:00 PM"),
    (23, "08:30 PM"),
    (24, "09:00 PM"),
)

TEACHERS = (
    (0, "Dan Rogers"),
    (1, "Emily Carter"),
    (2, "James Lee"),
    (3, "Sophia Martinez"),
    (4, "Michael Brown"),
    (5, "Olivia Johnson"),
    (6, "David Smith"),
    (7, "Isabella Clark"),
)


class ScheduledClass(models.Model):
    gymclass_organiser = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="gymtimetable_organiser",
    )
    gym_class = models.ForeignKey(
        FitnessClasses,
        on_delete=models.SET_NULL,
        null=True,
        related_name="gym_classes",
    )
    day = models.IntegerField(choices=DAYS_OF_WEEK, default=0)
    gym_class_time = models.IntegerField(choices=CLASS_TIMES, default=0)
    teacher = models.IntegerField(choices=TEACHERS, default=0)
    gym_class_duration = models.IntegerField(
        choices=CLASS_DURATION_TIME, default=0
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["day", "gym_class_time", "created_on"]

    def __str__(self):
        day_label = self.get_day_display() if self.day is not None else "—"
        time_label = (
            self.get_gym_class_time_display()
            if self.gym_class_time is not None
            else "—"
        )
        teacher_label = (
            self.get_teacher_display() if self.teacher is not None else "—"
        )

        # Avoid triggering FitnessClasses.__str__ by using a concrete field:
        class_label = (
            getattr(self.gym_class, "gym_class_name", None)
            or "No class selected"
        )

        return (
            f"{day_label} {time_label} - {class_label}"
            f" - Teacher: {teacher_label}"
        )


class Booking(models.Model):
    member = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="class_bookings"
    )
    booked_class = models.ForeignKey(
        ScheduledClass,
        on_delete=models.CASCADE,
        related_name="member_bookings",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("member", "booked_class")

    def __str__(self):
        return f"{self.member} booked {self.booked_class}"
