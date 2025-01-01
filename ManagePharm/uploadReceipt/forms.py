from django import forms
from .models import Receipt

class ReceiptImageForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = ['receipt_image']