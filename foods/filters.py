from .models import Food
import django_filters

class FoodFilter(django_filters.FilterSet):
    category = django_filters.ChoiceFilter(choices=Food.FOOD_CHOICES, label='Category')
    merchant_area = django_filters.CharFilter(lookup_expr='icontains', label='Merchant Area')

    class Meta:
        model = Food
        fields = ['category', 'merchant_area']
