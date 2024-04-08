import json
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import Food
from authentication.models import UserProfile
from django.contrib.auth.decorators import login_required
from .forms import FoodFilterForm
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url="authentication:login")
def show_food(request):
    user = request.user
    user_profile = UserProfile.objects.get(user=user)

    if user_profile.user_type.casefold() == "writer":
        food_list = Food.objects.all()
        return render(request, 'writer_food.html', {'foods': food_list})

    foods = Food.objects.all()
    form = FoodFilterForm(request.GET)

    if form.is_valid():
        category = form.cleaned_data.get("category")
        merchant_area = form.cleaned_data.get("merchant_area")

        if category:
            foods = foods.filter(Category=category)

        if merchant_area:
            foods = foods.filter(Merchant_area__icontains=merchant_area)

    context = {
        'form': form,
        'foods': foods,
    }

    return render(request, 'food.html', context)

@login_required(login_url="authentication:login")
def food_detail(request, food_id):
    food = get_object_or_404(Food, id=food_id)
    context = {'food': food}
    if UserProfile.objects.get(user=request.user).user_type.casefold() == "writer":
        return render(request, 'writer_food_detail.html', context)
    return render(request, 'food_detail.html', context)

@csrf_exempt
def add_food(request):
    if request.method == "POST":
        merchant_area = request.POST.get('Merchant_area')
        category = request.POST.get('Category')
        product_name = request.POST.get('Product_name')
        product_description = request.POST.get('Product_description')
        image = request.POST.get('Image')

        new_food = Food(Merchant_area=merchant_area, Category=category, Product_name=product_name,
                        Product_description=product_description, Image=image)
        new_food.save()
        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

def get_food(request):
    data = Food.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_food_by_id(request, id):
    data = Food.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def create_food_flutter(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            merchant_area = data.get('Merchant_area')
            category = data.get('Category')
            product_name = data.get('Product_name')
            product_description = data.get('Product_description')
            image = data.get('Image')

            new_food = Food.objects.create(
                Merchant_area=merchant_area,
                Category=category,
                Product_name=product_name,
                Product_description=product_description,
                Image=image
            )

            new_food.save()

            return JsonResponse({"status": "success", "message": "Food added successfully"}, status=200)

        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)

    else:
        return JsonResponse({"status": "error", "message": "Invalid request"}, status=400)

@csrf_exempt
def filter_foods(request):
    category = request.GET.get('category', '')
    merchant_area = request.GET.get('merchant_area', '')

    foods = Food.objects.all()
    if category:
        foods = foods.filter(Category=category)
    if merchant_area:
        foods = foods.filter(Merchant_area__icontains=merchant_area)

    foods_json = serializers.serialize('json', foods)
    return JsonResponse(foods_json, safe=False)
