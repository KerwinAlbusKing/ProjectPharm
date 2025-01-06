from django import forms
from .models import InsuranceItem

class InsuranceItemForm(forms.ModelForm):
    class Meta:
        model = InsuranceItem
        fields = ['insurance_code', 'name', 'specification', 'quantity', 'unit_price', 'total_price', 'expiry_date']
