from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column
from .models import ScheduledClass


class ScheduledClassForm(forms.ModelForm):

    class Meta:
        model = ScheduledClass
        fields = [
            "gym_class",
            "day",
            "gym_class_slot",
            "teacher",
            "gym_class_duration",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Crispy form helper
        self.helper = FormHelper()
        self.helper.form_tag = False

        # Layout: 2 fields per row
        self.helper.layout = Layout(
            Row(
                Column("day", css_class="col-md-6"),
                Column("gym_class", css_class="col-md-6"),
                css_class="g-3",
            ),
            Row(
                Column("teacher", css_class="col-md-6"),
                Column("gym_class_slot", css_class="col-md-6"),
                css_class="g-3",
            ),
            Row(
                Column("gym_class_duration", css_class="col-md-6 mx-auto"),
                css_class="g-3",
            ),
        )
