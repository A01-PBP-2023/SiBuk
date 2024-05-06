import json
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import Drink
from .forms import DrinkFilterForm
from user_auth.models import UserProfile
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

def show_drink(request):
    user = request.user
    drinks = Drink.objects.all()
    user_profile = UserProfile.objects.get(user=user)
    form = DrinkFilterForm(request.GET)

    if form.is_valid():
        category = form.cleaned_data.get("category")

        if category:
            drinks = drinks.filter(category=category)


    context = {
        'form': form,
        'drinks': drinks,
    }

    return render(request, 'drinks.html', context)

def drink_detail(request, drink_id):
    drink = get_object_or_404(Drink, id=drink_id)
    context = {'drink': drink}
    return render(request, 'drink_detail.html', context)

@csrf_exempt
def add_drink(request):
    if request.method == "POST":
        merchant_area = request.POST.get('merchant_area')
        merchant_name = request.POST.get('merchant_name')
        category = request.POST.get('category')
        product = request.POST.get('product')
        description = request.POST.get('description')

        new_drink = Drink(merchant_area=merchant_area, merchant_name=merchant_name, category=category, product=product,
                        description=description)
        new_drink.save()
        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

def add_to_favorites(request, drink_id, user_id):
    user = request.user.userprofile
    drink = get_object_or_404(Katalog, id=drink_id)
    user.cart.add(drink)
    return redirect('foods:show_favorites')

def get_drink(request):
    data = Drink.objects.all()
    return HttpResponse(serializers.serialize("json", data), 
    content_type="application/json")

def get_drink_by_id(request, id):
    data = Drink.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def filter_drink(request):
    category = request.GET.get('category', '')

    drinks = Drink.objects.all()
    if category:
        drinks = drinks.filter(category=category)

    drinks_json = serializers.serialize('json', drinks)
    return JsonResponse(drinks_json, safe=False)