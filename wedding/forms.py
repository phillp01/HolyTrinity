from django import forms
from .models import Wedding, ServiceReading, ServiceHymn


class WeddingForm(forms.ModelForm):

    class Meta:
        model = Wedding
        fields = [
            'date',
            'time',
            'bride',
            'groom',
            'church',
            'minister',
            'service_type',
            'service_status',
            'dear',
            'mail_title',
            'banns_date',
            'bible',
            'reader',
            'other',
            'other_reader',
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
            'total_paid',
            'date_amount_paid',
            'notes',
            'first_visit',
            'second_visit',
            'third_visit',
            'evidence_filed',
            'decree_abs_seen',
            'banns_no',
        ]
        widgets = {
            'date': forms.DateInput(attrs={'class': 'datepicker'}),
        }

class ReadingForm(forms.ModelForm):

    class Meta:
        model = ServiceReading
        fields = [
            'bible',
            'other',
            'reader',
            'other_reader',
            'wedding',
        ]
        widgets = {'wedding': forms.HiddenInput()}


class HymnForm(forms.ModelForm):

    class Meta:
        model = ServiceHymn
        fields = [
            'hymn',
            'wedding',
        ]
        widgets = {'wedding': forms.HiddenInput()}