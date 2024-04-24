from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from user_auth.forms import RegisterForm
from user_auth.models import UserProfile
from django.views.decorators.csrf import csrf_exempt
import json


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('user_auth:login')  
    context = {'form':form}
    if request.user.is_authenticated :
        return redirect("recommended:show_page")
    else :
        return render(request, 'register.html', context)
        



def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_page = request.GET.get("next")
            if next_page is None:
                response = redirect("recommended:show_page")
            else:
                response = redirect(next_page)
            response.set_cookie("user_logged_in", user)
            return response
        else:
            messages.info(
                request, "Sorry, incorrect username or password. Please try again.")
    context = {}
    if request.user.is_authenticated:
        return redirect('recommended:show_page')
    else:
        return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('recommended:show_page'))
    return response