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
            'verger',
            'car_park_attendant',
            'marches',
            'singing',
            'organist',
            'flowers_details',
            'flowers_contact',
            'no_of_guests',
            'wheelchair_access',
            'rehearsal_date',
            'rehearsal_time',
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
        widgets = {'wedding': forms.HiddenInput()}

