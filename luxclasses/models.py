from django.db import models
from django.contrib.auth.models import User


# Create your models here.

STATUS = (("0", "Draft"), ("1", "Publish"))


class FitnessClasses(models.Model):
    gym_class_name = models.CharField(max_length=200, unique=True)
    short_bullets_gymclassname = models.SlugField(max_length=200, unique=True)
    gymclass_creator = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="fitnessclasses",
    )
    gym_class_name_extension = models.CharField(max_length=200, blank=True)
    content = models.TextField()
    filename = models.CharField(max_length=255, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS, default="0")
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.gym_class_name}"
