from django.urls import path
from .views import (
    ScheduledClassListView,
    UserGymTimetableListView,
    toggle_booking,
)

app_name = "gymtimetable"

urlpatterns = [
    path("admin/", ScheduledClassListView.as_view(), name="admin_timetable"),
    path("my/", UserGymTimetableListView.as_view(), name="class_list"),
    path("book/<int:pk>/", toggle_booking, name="toggle_booking"),
]
