from django.shortcuts import render
from django.core import serializers
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

