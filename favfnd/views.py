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
    # favorite = request.user.food.all()
    # return render(request, 'favorites.html')
    # context = {
    #     "favorite": favorite,

    # }

    return render(request, 'favorites.html', )

