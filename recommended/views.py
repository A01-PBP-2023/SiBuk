from django.shortcuts import render
from foods.models import Food
from foods.views import food_detail
# Create your views here.

def show_page (request):
    data = Food.objects.all()[:10]
    context = {
        'food': data
    }
    return render(request, 'index.html', context)

