from django.shortcuts import render
from foods.models import Food
from django.http import HttpResponse
from django.core import serializers
# Create your views here.

def show_page (request):
    foods = Food.objects.all()[:10]

    context = {
        'data': foods
    }
    return render(request, 'index.html', context)


def show_json (request) :
    data = Food.objects.all()[:10]
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")




