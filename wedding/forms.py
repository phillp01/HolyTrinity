from django import forms
from .models import Wedding, ServiceReadings


class WeddingForm(forms.ModelForm):

    class Meta:
        model = Wedding
        fields = [
            'date',
            'time',
            'church',
            'minister',
            'service_type',
            'service_status',
            'dear',
            'mail_title',
            'banns_date',
            'by_license',
            'organ',
            'choir',
            'bells',
            'flowers',
            'video',
            'cd',
            'winter_heating',
        ]
        widgets = {
            'date': forms.DateInput(attrs={'class': 'datepicker'}),
        }

class ReadingForm(forms.ModelForm):

    class Meta:
        model = ServiceReadings
        fields = [
            'bible',
            'other',
            'reader',
            'wedding',
        ]