# myapp/forms.py

from django import forms

from blog.models import *
from datetime import datetime, timedelta

# class TGForm(forms.Form):
#     name = forms.CharField(label='Your name', max_length=100)
#     numbers = forms.CharField(label='Phone number')
#     message = forms.CharField(label='Message', widget=forms.Textarea)
yesterday = datetime.today()
min_date = yesterday.strftime("%Y-%m-%d")


class TGForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = 'first_name', 'last_name', 'message', 'number', 'date_of_birth', 'time_slots', 'service'
        labels = {
            'date_of_birth': 'Date',

            'number': 'Phone number',
            'time_slots': 'Time slots',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            'date_of_birth': forms.DateInput(
                attrs={'type': 'date', 'id': 'date', 'class': 'form-control', 'min': min_date, 'value': min_date}, ),

            # 'number': forms.NumberInput(attrs={'class': 'form-control',
            #                                    'placeholder': 'Phone number(+X (XXX) XXX-XX-XX)/WhatsApp',
            #                                    }),
            'number': forms.NumberInput(
                attrs={'class': 'form-control', 'type': 'tel', 'id': 'phone', 'name': 'phone', 'value': '+',
                       "pattern": "[0-9+()-]*",
                       'placeholder': 'Please provide the number with the country’s code (+1);(+3) or number Signal/What’s app'}),
            'message': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please indicate your wishes'}),
            'service': forms.Select(attrs={'class': 'form-control'}),
            'time_slots': forms.Select(attrs={'class': 'form-control'}),
        }
