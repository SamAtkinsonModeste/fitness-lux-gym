from django.shortcuts import render
from django.views.generic import ListView
from .models import LuxGymTimetable
from django.contrib import messages
from .forms import LuxGymTimetableForm

# Create your views here.


class LuxGymTimetableView(ListView):
    """
    Displays any object from two models:
    app:gymtimetable - model:LuxGymTimetable 
    app: fitnesslessons - model:FitnessClasses
    """
    model = LuxGymTimetable
    context_object_name = "luxgymtimetable"

    def get_context_data(self, **kwargs):
        """
        To add my form to the context object
        the context variable gets all the form elements
        using **kwargs which creates a dictionary of my form elements 
        and then context adds a variable to the context dictionary.

        """
        context = super().get_context_data(**kwargs)
        # Pass the form to template
        context['create_classTime'] = LuxGymTimetableForm()
        return context

    def form_process(self, request):
        if request.method == "POST":
            form_done = LuxGymTimetableForm(request.POST)
            if form_done.is_valid():
                form_done.save()
                messages.add_message(
                    request, messages.SUCCESS,
                    'Class was added to the timetable'
                )
                return redirect('luxgymtimetable')
