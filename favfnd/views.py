from django.shortcuts import render

# Create your views here.

def show_favorites(request):
    return render(request, 'favorites.html')

