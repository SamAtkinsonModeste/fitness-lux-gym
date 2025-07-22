from .models import ScheduledClass
from django import forms


class ScheduledClassForm(forms.ModelForm):
    class Meta:
        model = ScheduledClass
        fields = ["gymclass_organiser", "gym_class", "day",
                  "gym_class_time", "teacher", "gym_class_duration"]
