from django import forms
from .models import Donate


class DonateForm(forms.ModelForm):
    user = forms.CharField(max_length = 100)
    supermarket = forms.CharField(max_length=100)
    delivery_date = forms.DateField()
    amount = forms.DecimalField()

    class Meta:
        model = Donate
        fields = [
            'user',
            'supermarket',
            'delivery_date',
            'amount'
        ]