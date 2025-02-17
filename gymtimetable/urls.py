from django.urls import path
from .views import LuxGymTimetableView

urlpatterns = [
    path("", LuxGymTimetableView.as_view(), name="timetable"),
    path("", LuxGymTimetableView.as_view(), name="usertimetable"),
]
