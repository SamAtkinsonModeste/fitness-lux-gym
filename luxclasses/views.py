from django.views.generic import ListView
from .models import FitnessClasses

# Create your views here.


class FitnessClassesView(ListView):
    model = FitnessClasses
    context_object_name = "fitnessclasses"
