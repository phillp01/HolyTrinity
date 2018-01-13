from django import forms
from .models import Wedding


class WeddingForm(forms.ModelForm):

    class Meta:
        model = Wedding
        fields = [
            'date',
            'time',
            'church',
            'minister',
        ]
        widgets = {
            'date': forms.DateInput(attrs={'class': 'datepicker'}),
        }
