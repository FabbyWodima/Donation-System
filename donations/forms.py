from django import forms
from .models import Donate

class DonateForm(forms.ModelForm):
    class Meta:
        model = Donate
        fields = ['amount', 'phone_number']
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
        }