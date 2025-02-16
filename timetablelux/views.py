from django.views.generic import ListView
from .models import FitnessTimetable

# Create your views here.


class FitnessTimetableView(ListView):
    model = FitnessTimetable
    context_object_name = "fitnesstimetable"
