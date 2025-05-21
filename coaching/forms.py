# forms.py
from django import forms

from .models import Session


class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['title', 'date', 'description', 'location']
        widgets = {
            'date': forms.DateTimeInput(
                attrs={
                    'class': 'datetimepicker',  # Required for Flatpickr to target it
                    'placeholder': 'Select date and time',
                    'type': 'text'  # Important for Flatpickr compatibility
                }
            )
        }
