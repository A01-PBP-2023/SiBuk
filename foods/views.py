import json
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import Food
from .forms import FoodFilterForm
from user_auth.models import UserProfile
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import permission_required


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
@permission_required("food.add_food")
def add_food(request):
    if request.method == "POST":
        merchant_area = request.POST.get('merchant_area')
        merchant_name = request.POST.get('merchant_name')
        category = request.POST.get('category')
        product = request.POST.get('product')
        description = request.POST.get('description')

        new_food = Food(merchant_area=merchant_area, merchant_name=merchant_name, category=category, product=product,
                        description=description)
        new_food.save()
        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

def add_to_favorites(request, food_id, user_id):
    user = request.user.userprofile
    food = get_object_or_404(Katalog, id=food_id)
    user.cart.add(food)
    return redirect('foods:show_favorites')

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
