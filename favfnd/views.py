from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, JsonResponse
from django.urls import reverse
from django.shortcuts import render
from django.core import serializers
from user_auth.models import UserProfile
# Create your views here.

def show_favorites(request):
    data = []
    if request.user.is_authenticated:
        user = UserProfile.objects.filter(user=request.user).first()
        for item in user.favfood.all():
            item_data = serializers.serialize('python', [item])[0]
            data.append(item_data)
        for item in user.favdrink.all():
            item_data = serializers.serialize('python', [item])[0]
            data.append(item_data)
        context = {
            "favorite": data,
        }
        return render(request, 'favorites.html', context)
    else :
        return redirect(reverse("user_auth:login"))

   


