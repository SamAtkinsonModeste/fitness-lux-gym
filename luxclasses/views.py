from django.views.generic import ListView, DetailView
from django.utils.decorators import method_decorator
from django.views.decorators.clickjacking import xframe_options_exempt
from .models import FitnessClasses

# Create your views here.


@method_decorator(xframe_options_exempt, name="dispatch")
class FitnessClassesView(ListView):
    """
    Returns all objects of :model:luxclasses.FitnessClasses

    **Context**
    context_object_name
    - gym class name
    - extended text to the gym class name key words related to the class
    - description of class
    - image of the gym class
    - excerpt of the gym class description

    **Template:**
    :template: luxclasses/fitnessclass_list.html
    """

    model = FitnessClasses
    context_object_name = "fitnessclasses"


class FitnessClassDetailView(DetailView):
    model = FitnessClasses
    context_object_name = "fitnessclass"
