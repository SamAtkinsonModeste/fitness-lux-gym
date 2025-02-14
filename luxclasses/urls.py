from django.urls import path
from .views import FitnessClassesView


urlpatterns = [
    path('', FitnessClassesView.as_view(), name='home'),
]
