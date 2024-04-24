from django.shortcuts import render
from foods.models import Food
from drinks.models import Drink
from foods.views import food_detail
from django.http import HttpResponse
from django.core import serializers
import random
# Create your views here.

def show_page (request):
    food_items = list((Food.objects.all()))
    drink_items = list((Drink.objects.all()))

    random_food_items = random.sample(food_items, 6)
    random_drink_items = random.sample(drink_items, 6)

    data_for_food = []
    data_for_drink = []

    for food in random_food_items:
        food_data = serializers.serialize('python', [food])[0]
        data_for_food.append(food_data)

    for drink in random_drink_items:
        drink_data = serializers.serialize('python', [drink])[0]
        data_for_drink.append(drink_data)


    context = {
        'food': data_for_food,
        'drink': data_for_drink
    }
    print(context)
    return render(request, 'index.html', context)


def show_json(request):
    data = Food.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")