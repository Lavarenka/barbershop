# myapp/forms.py

from django import forms

from blog.models import *


# class TGForm(forms.Form):
#     name = forms.CharField(label='Your name', max_length=100)
#     numbers = forms.CharField(label='Phone number')
#     message = forms.CharField(label='Message', widget=forms.Textarea)


class TGForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = '__all__'
        labels = {
            'date_of_birth': 'Date',
            'time_of_death': 'Time',
            'number': 'Phone number',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time_of_death': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'number': forms.NumberInput(attrs={'class': 'form-control',
                                               'placeholder': 'Phone number(+X (XXX) XXX-XX-XX)/WhatsApp',
                                               }),
            'message': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please indicate your wishes'}),
            'service': forms.Select(attrs={'class': 'form-control'}),
        }
