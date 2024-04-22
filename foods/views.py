import json
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import Food
from .forms import FoodFilterForm
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

def show_food(request):
    foods = Food.objects.all()
    form = FoodFilterForm(request.GET)

    if form.is_valid():
        category = form.cleaned_data.get("category")

        if category:
            foods = foods.filter(category=category)


    context = {
        'form': form,
        'foods': foods,
    }

    return render(request, 'foods.html', context)

def food_detail(request, food_id):
    food = get_object_or_404(Food, id=food_id)
    context = {'food': food}
    return render(request, 'food_detail.html', context)

@csrf_exempt
def add_food(request):
    if request.method == "POST":
        merchant_area = request.POST.get('Merchant_area')
        category = request.POST.get('category')
        product = request.POST.get('product')
        description = request.POST.get('description')
        image = request.POST.get('Image')

        new_food = Food(merchant_area=merchant_area, category=category, product=product,
                        description=description, Image=image)
        new_food.save()
        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

def get_food(request):
    data = Food.objects.all()
    return HttpResponse(serializers.serialize("json", data), 
    content_type="application/json")

def get_food_by_id(request, id):
    data = Food.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def filter_foods(request):
    category = request.GET.get('category', '')

    foods = Food.objects.all()
    if category:
        foods = foods.filter(category=category)

    foods_json = serializers.serialize('json', foods)
    return JsonResponse(foods_json, safe=False)
