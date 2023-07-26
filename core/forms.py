import datetime
from django import forms
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
