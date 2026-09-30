from django import forms
from .models import Reminder

class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['item_name', 'category', 'date', 'time', 'status', 'notes']
        widgets = {
            'item_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter item name'}),
            'category': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter category'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Select date'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time', 'placeholder': 'Select time'}),
            'status': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter status'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter notes'}),
        }
