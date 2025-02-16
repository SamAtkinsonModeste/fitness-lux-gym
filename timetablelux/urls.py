from django.urls import path
from .views import FitnessTimetableView


urlpatterns = [
    path('', FitnessTimetableView.as_view(), name='timetable'),
    path('', FitnessTimetableView.as_view(), name='usertimetable'),
]
