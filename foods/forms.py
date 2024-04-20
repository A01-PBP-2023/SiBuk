from django import forms
from .models import Food

class FoodFilterForm(forms.Form):
    category = forms.ChoiceField(choices=Food.FOOD_CHOICES, required=False)
<<<<<<< HEAD
    merchant_area = forms.CharField(required=False)
=======
    merchant_area = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Merchant Area'}))
>>>>>>> origin/main

class AddFoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['Merchant_area', 'Category', 'Product_name', 'Product_description', 'Image']
        widgets = {
            'Product_name': forms.TextInput(attrs={'placeholder': 'Product Name'}),
<<<<<<< HEAD
            'Merchant_area': forms.TextInput(attrs={'placeholder': 'Merchant Area'}),
=======
>>>>>>> origin/main
            'Product_description': forms.TextInput(attrs={'placeholder': 'Product Description'}),
            'Image': forms.URLInput(attrs={'placeholder': 'Image URL'}),
        }