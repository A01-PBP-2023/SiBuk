from .models import Drink
import django_filters

class DrinkFilter(django_filters.FilterSet):
    category = django_filters.ChoiceFilter(choices=Drink.DRINK_CHOICES, label='Category')
    merchant_area = django_filters.CharFilter(lookup_expr='icontains', label='Merchant Area')

    class Meta:
        model = Drink
        fields = ['category', 'merchant_area']