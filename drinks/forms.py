from django import forms
from .models import Drink

class DrinkFilterForm(forms.Form):
    category = forms.ChoiceField(choices=Drink.DRINK_CHOICES, required=False)
    merchant_area = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Merchant Area'}))

class AddDrinkForm(forms.ModelForm):
    class Meta:
        model = Drink
        fields = ['merchant_area', 'merchant_name', 'category', 'product', 'description']