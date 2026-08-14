from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            "title",
            "description",
            "category",
            "organizer",
            "date",
            "start_time",
            "end_time",
            "location",
            "price",
            "capacity",
            "image",
        ]