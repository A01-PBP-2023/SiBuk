from .models import Food
import django_filters

class FoodFilter(django_filters.FilterSet):
    category = django_filters.ChoiceFilter(choices=Food.FOOD_CHOICES, label='Category')

    class Meta:
        model = Food
        fields = ['category']
