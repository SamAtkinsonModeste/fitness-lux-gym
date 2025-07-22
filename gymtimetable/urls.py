from django.urls import path
from .views import ScheduledClassListView

urlpatterns = [

    path("", ScheduledClassListView.as_view(), name="timetable"),
    # path("", TimetableView.as_view(), name="usertimetable"),
]
