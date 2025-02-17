from django.views.generic import ListView
from .models import LuxGymTimetable

# Create your views here.


class LuxGymTimetableView(ListView):
    model = LuxGymTimetable
    context_object_name = "luxgymtimetable"

    def get_queryset(self):
        return LuxGymTimetable.objects.select_related("gym_class")
