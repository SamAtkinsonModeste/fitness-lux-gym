from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView

from .models import ScheduledClass
from .forms import ScheduledClassForm



class ScheduledClassListView(ListView):
    """
    Displays the gym timetable for administrators.

    - GET request:
      * Shows a form for creating new scheduled classes.
      * Lists all scheduled classes ordered by day and time.
      * If an 'edit' query parameter is present in the URL (e.g. ?edit=5),
        includes a pre-filled form to edit that specific class.

    - POST request:
      * Handles three possible actions:
        - "create": Add a new class to the timetable.
        - "update": Edit an existing class (identified by its primary key).
        - "delete": Remove an existing class (identified by its primary key).
      * Only superusers are allowed to perform these actions.
      * Always redirects back to the timetable view after processing (PRG pattern).

    Context:
      - scheduled_classes: All ScheduledClass objects for display.
      - create_form: Empty ScheduledClassForm for adding new classes.
      - edit_obj: (optional) The ScheduledClass being edited.
      - edit_form: (optional) A pre-filled ScheduledClassForm for editing.
    """
    model = ScheduledClass
    context_object_name = "scheduled_classes"
    ordering = ["day", "gym_class_time", "created_on"]

    def get_queryset(self):
        return super().get_queryset().select_related("gym_class", "gymclass_organiser")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_form'] = ScheduledClassForm()

        edit_pk = self.request.GET.get("edit")
        if edit_pk and edit_pk.isdigit():
            obj = ScheduledClass.objects.filter(pk=edit_pk).first()
            if obj:
                context["edit_obj"] = obj
                context["edit_form"] = ScheduledClassForm(instance=obj)

        return context

    def post(self, request, *args, **kwargs):
        action = request.POST.get("action")
        if action not in {"create", "update", "delete"}:
            messages.error(request, "Unknown action")
            return redirect("gymtimetable")

        if not (request.user.is_authenticated and request.user.is_superuser):
               messages.error(request, "Only admins can perform timetable changes.")
               return redirect("gymtimetable")

        if action == "create":
            form = ScheduledClassForm(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.gymclass_organiser = request.user
                obj.save()
                messages.success(request, "Class created.")
            else:
                messages.error(request, "Please fix the errors in the create form.")

        elif action == "update":
            pk = request.POST.get("pk")
            if not pk or not pk.isdigit():
                messages.error(request, "Invalid item.")
                return redirect("gymtimetable")

            obj = get_object_or_404(ScheduledClass, pk=pk)
            form = ScheduledClassForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                messages.success(request, "Class updated.")
            else:
                messages.error(request, "Please fix the errors in the edit form.")

        elif action == "delete":
            pk = request.POST.get("pk")
            if not pk or not pk.isdigit():
                messages.error(request, "Invalid item.")
                return redirect("gymtimetable")

            obj = get_object_or_404(ScheduledClass, pk=pk)
            obj.delete()
            messages.success(request, "Class removed.")

        return redirect("gymtimetable")



