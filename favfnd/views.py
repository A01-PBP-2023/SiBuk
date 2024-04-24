from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, JsonResponse
from django.urls import reverse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import json
import datetime
# Create your views here.


def show_favorites(request):
    favfood = request.user.userprofile.favfood.all()
    context = {
        "favfood": favfood,
    }
    return render(request, 'favorites.html', context)


def show_json(request):
    data = request.user.userprofile.favfood.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_all_attributes(request):
    return HttpResponse(User.values())



