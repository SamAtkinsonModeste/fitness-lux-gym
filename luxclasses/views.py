from django.views.generic import ListView
from .models import FitnessClasses

# Create your views here.


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
