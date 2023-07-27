import datetime
from django import forms
from django.core.exceptions import ValidationError

from core.models import Task


class TaskForm(forms.ModelForm):
    deadline = forms.DateField(
        initial=datetime.date.today,
        widget=forms.widgets.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Task
        fields = (
            "title",
            "description",
            "deadline",
            "is_completed"
        )

    def clean_deadline(self):
        return validate_deadline(
            self.cleaned_data["deadline"]
        )


def validate_deadline(deadline):
    if deadline < datetime.date.today():
        raise ValidationError(
            "The deadline date can not be earlier then creation date"
        )
    return deadline
