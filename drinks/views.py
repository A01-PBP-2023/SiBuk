import json
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import Drink
from .forms import DrinkFilterForm
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

def show_drink(request):
    drinks = Drink.objects.all()
    form = DrinkFilterForm(request.GET)

    if form.is_valid():
        category = form.cleaned_data.get("category")
        merchant_area = form.cleaned_data.get("merchant_area")

        if category:
            drinks = drinks.filter(Category=category)

        if merchant_area:
            drinks = drinks.filter(Merchant_area__icontains=merchant_area)

    context =   {
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
        merchant_area = request.POST.get('Merchant_area')
        category = request.POST.get('Category')
        product_name = request.POST.get('Product_name')
        product_description = request.POST.get('Product_description')
        image = request.POST.get('Image')

        new_drink = Drink(Merchant_area=merchant_area, Category=category, Product_name=product_name,
                        Product_description=product_description, Image=image)
        new_drink.save()
        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

def get_drink(request):
    data = Drink.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_drink_by_id(request, id):
    data = Drink.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def filter_drink(request):
    category = request.GET.get('category', '')
    merchant_area = request.GET.get('merchant_area', '')

    drinks = Drink.objects.all()
    if category:
        drinks = drinks.filter(Category=category)
    if merchant_area:
        drinks = drinks.filter(Merchant_area__icontains=merchant_area)

    drink_json = serializers.serialize('json', drinks)
    return JsonResponse(drink_json, safe=False)
