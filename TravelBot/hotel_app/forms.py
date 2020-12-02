from django import forms
from .models import *

class BookingForm(forms.ModelForm):
    class Meta:
        model = BookHotel
        fields = ['hotel', 'no_of_rooms', 'no_of_days']
