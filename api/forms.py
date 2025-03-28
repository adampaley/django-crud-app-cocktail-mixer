from django import forms 
from .models import Serving

class ServingForm(forms.ModelForm):
    class Meta:
        model = Serving
        fields = ['date', 'jigger']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            )
        }