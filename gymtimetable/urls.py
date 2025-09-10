from django.urls import path
from .views import ScheduledClassListView

urlpatterns = [

    path("", ScheduledClassListView.as_view(), name="gymtimetable"),
]
