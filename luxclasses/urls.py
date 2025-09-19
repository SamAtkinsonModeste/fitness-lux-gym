from django.urls import path
from .views import FitnessClassesView, FitnessClassDetailView

app_name = "luxclasses"

urlpatterns = [
    path("", FitnessClassesView.as_view(), name="home"),
    path("<int:pk>/", FitnessClassDetailView.as_view(), name="class_detail"),
]
