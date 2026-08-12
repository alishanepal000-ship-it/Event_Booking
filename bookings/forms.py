from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ["quantity"]

        widgets = {
            "quantity": forms.NumberInput(
                attrs={
                    "min": 1,
                    "class": "form-control"
                }
            )
        }

    def __init__(self, *args, **kwargs):
        self.event = kwargs.pop("event", None)
        super().__init__(*args, **kwargs)

    def clean_quantity(self):
        quantity = self.cleaned_data["quantity"]

        if quantity < 1:
            raise forms.ValidationError(
                "You must book at least one ticket."
            )

        if self.event and quantity > self.event.capacity:
            raise forms.ValidationError(
                "Not enough tickets are available."
            )

        return quantity