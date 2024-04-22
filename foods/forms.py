from django import forms
from .models import Food

class FoodFilterForm(forms.Form):
    category = forms.ChoiceField(choices=Food.FOOD_CHOICES, required=False)

class AddFoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['merchant_area', 'merchant_name', 'category', 'product', 'description']