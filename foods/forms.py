from django import forms
from .models import Food

class FoodFilterForm(forms.Form):
    category = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Category'}))

class AddFoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['merchant_area', 'merchant_name', 'category', 'product', 'description']