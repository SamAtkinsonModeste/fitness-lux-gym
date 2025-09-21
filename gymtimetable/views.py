from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.clickjacking import xframe_options_exempt
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView
from django.urls import reverse

from .models import ScheduledClass, Booking
from .forms import ScheduledClassForm


@method_decorator(xframe_options_exempt, name="dispatch")
class ScheduledClassListView(ListView):
    """
    Displays the gym timetable for administrators.

    GET:
      - Shows a form for creating new scheduled classes.
      - Lists all scheduled classes ordered by day and time.
      - If an 'edit' query parameter is present (e.g. ?edit=5), also
        includes a pre-filled form to edit that specific class.

    POST:
      - Handles three actions: "create", "update", and "delete".
      - Only superusers may perform these actions.
      - Always redirects back to the timetable view after processing.

    Context:
      - scheduled_classes: queryset for display.
      - create_form: empty ScheduledClassForm for adding classes.
      - edit_obj: optional ScheduledClass being edited.
      - edit_form: optional pre-filled ScheduledClassForm.
    """

    model = ScheduledClass
    context_object_name = "scheduled_classes"
    ordering = ["day", "gym_class_slot", "created_on"]
    template_name = "gymtimetable/scheduledclass_list.html"

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .select_related("gym_class", "gymclass_organiser")
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["create_form"] = ScheduledClassForm()

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
            messages.error(request, "Unknown action.")
            return redirect("gymtimetable:admin_timetable")

        if not (request.user.is_authenticated and request.user.is_superuser):
            messages.error(
                request,
                "Only admins can perform timetable changes.",
            )
            return redirect("gymtimetable:class_list")

        if action == "create":
            form = ScheduledClassForm(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.gymclass_organiser = request.user
                obj.save()
                messages.success(request, "Class created.")
                return redirect("gymtimetable:admin_timetable")
            else:
                messages.error(request, form.errors.as_text())
                self.object_list = self.get_queryset()
                context = self.get_context_data()
                context["create_form"] = form
                return self.render_to_response(context)

        elif action == "update":
            pk = request.POST.get("pk")
            if not pk or not pk.isdigit():
                messages.error(request, "Invalid item.")
                return redirect("gymtimetable:admin_timetable")

            obj = get_object_or_404(ScheduledClass, pk=pk)
            form = ScheduledClassForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                messages.success(request, "Class updated.")
                return redirect("gymtimetable:admin_timetable")
            else:
                messages.error(request, form.errors.as_text())
                self.object_list = self.get_queryset()
                context = self.get_context_data()
                context["edit_obj"] = obj
                context["edit_form"] = form
                return self.render_to_response(context)

        elif action == "delete":
            pk = request.POST.get("pk")
            if not pk or not pk.isdigit():
                messages.error(request, "Invalid item.")
                return redirect("gymtimetable:admin_timetable")

            obj = get_object_or_404(ScheduledClass, pk=pk)
            obj.delete()
            messages.success(request, "Class removed.")

        return redirect("gymtimetable:admin_timetable")


@method_decorator(xframe_options_exempt, name="dispatch")
class UserGymTimetableListView(ListView):
    model = ScheduledClass
    context_object_name = "classes"
    template_name = "gymtimetable/usergymtimetable_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context["booked_ids"] = set(
                Booking.objects.filter(member=self.request.user).values_list(
                    "booked_class_id", flat=True
                )
            )
        else:
            context["booked_ids"] = set()
        return context


@login_required
def toggle_booking(request, pk):
    if request.method != "POST":
        return redirect(reverse("gymtimetable:class_list"))

    scheduled_class = get_object_or_404(ScheduledClass, pk=pk)

    existing_booking = Booking.objects.filter(
        member=request.user,
        booked_class=scheduled_class,
    )

    if existing_booking.exists():
        existing_booking.delete()
        messages.success(request, "Booking cancelled")
    else:
        Booking.objects.create(
            member=request.user,
            booked_class=scheduled_class,
        )
        messages.success(request, "Class booked!")

    return redirect(reverse("gymtimetable:class_list"))
