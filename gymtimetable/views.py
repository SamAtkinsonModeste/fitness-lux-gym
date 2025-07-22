from django.shortcuts import render
from django.views.generic import ListView
from .models import ScheduledClass
from django.contrib import messages
from .forms import ScheduledClassForm

# Create your views here.

class ScheduledClassListView(ListView):
    model = ScheduledClass
    context_object_name = "scheduledClass"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_class'] = ScheduledClassForm()
        return context



# class ScheduledClassView(ListView):
#     """
#     Displays any object from two models:
#     app:gymtimetable - model:ScheduledClass
#     app: luxclasses - model:FitnessClasses
#     """
#     model = ScheduledClass
#     context_object_name = "scheduledClass"

#     def get_context_data(self, **kwargs):
#         """
#         To add my form to the context object
#         the context variable gets all the form elements
#         using **kwargs which creates a dictionary of my form elements
#         and then context adds a variable to the context dictionary.

#         """
#         context = super().get_context_data(**kwargs)
#         # Pass the form to template
#         context['create_classTime'] = ScheduledClassForm()
#         return context

#     def form_process(request):
#         if request.method == "POST":
#             form_done = ScheduledClassForm(request.POST)
#             if form_done.is_valid():
#                 form_done.save()
#                 messages.add_message(
#                     request, messages.SUCCESS,
#                     'Class was added to the timetable'
#                 )
#                 return redirect('luxgymtimetable')
