from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, JsonResponse
from django.urls import reverse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import json
import datetime
from user_auth.models import UserProfile
# Create your views here.


def show_favorites(request):
    data = []
    user = UserProfile.objects.filter(user=request.user).first()
    for item in user.favfood.all():
        item_data = serializers.serialize('python', [item])[0]
        data.append(item_data)
    context = {
        "favorite": data,

    }
    print(context)

    return render(request, 'favorites.html', context)

