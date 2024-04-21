from django.forms import ModelForm, TextInput
from .models import Review

class ItemForm(ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        exclude = ("user",)