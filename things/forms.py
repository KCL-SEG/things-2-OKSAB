from typing import Any
from django import forms
from .models import Thing

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        labels = {
            'name': 'Name',
            'description': 'Description',
            'quantity': 'Quantity',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        error_messages = {
            'name': {
                'required': 'Name is required',
                'unique': 'Name must be unique',
                'max_length': 'Name must be less than 30 characters',
            },
            'description': {
                'max_length': 'Description must be less than 120 characters',
            },
            'quantity': {
                'required': 'Quantity is required',
                'min_value': 'Quantity must be greater than or equal to 0',
                'max_value': 'Quantity must be less than or equal to 100',
            },
        }