from django import forms
from .models import BookHotel

class BookingForm(forms.ModelForm):
    class Meta:
        model = BookHotel
        checkin_date = forms.DateField(
            widget=forms.TextInput(     
                attrs={'type': 'date'} 
            )
        )  
        checkout_date = forms.DateField(
        widget=forms.TextInput(     
            attrs={'type': 'date'} 
        )
        )    
        fields = ['no_of_rooms', 'checkin_date', 'checkout_date', 'no_of_days']
