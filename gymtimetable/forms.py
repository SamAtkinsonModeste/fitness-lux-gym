from .models import LuxGymTimetable
from django import forms


class LuxGymTimetableForm(forms.ModelForm):
    class Meta:
        model = LuxGymTimetable
        fields = ["gymclass_organiser", "gym_class", "day",
                  "gym_class_time", "teacher", "gym_class_duration"]
