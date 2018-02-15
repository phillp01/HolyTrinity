from django import forms
from .models import Person


class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = [
            'wedding_id',
            'role',
            'first_name',
            'last_name',
            'email',
            'phone',
            'title',
            'church',
            'proof',
            'qualifying_connection',
            'dob',
            'age_at_wedding',
            'occupation',
            'status',
            'nationality',
            'details',
            'connected_by_marriage',
            'if_yes_how',
            'father_name',
            'father_occupation',
        ]
