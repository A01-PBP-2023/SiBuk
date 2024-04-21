from django import forms
from .models import Food

class FoodFilterForm(forms.Form):
    category = forms.ChoiceField(choices=Food.FOOD_CHOICES, required=False)
    merchant_area = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Merchant Area'}))

class AddFoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['merchant_area', 'merchant_name', 'category', 'product', 'description']