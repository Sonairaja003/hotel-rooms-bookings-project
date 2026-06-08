from django import forms
from .models import Booking
from datetime import date


class BookingForm(forms.ModelForm):

    class Meta:

        model = Booking

        fields = [
            'check_in',
            'check_out',
            'guests'
        ]

        widgets = {

            'check_in': forms.DateInput(
                attrs={'type': 'date'}
            ),

            'check_out': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }

    def clean(self):

        cleaned_data = super().clean()

        check_in = cleaned_data.get('check_in')
        check_out = cleaned_data.get('check_out')

        # Past date block
        if check_in and check_in < date.today():

            raise forms.ValidationError(
                "Check-In date cannot be in the past."
            )

        # Check-out validation
        if check_in and check_out:

            if check_out <= check_in:

                raise forms.ValidationError(
                    "Check-Out date must be after Check-In date."
                )

        return cleaned_data