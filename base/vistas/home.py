from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import JsonResponse
from django.urls import reverse

import socket

# @login_required
def home(request): 
    ipadd = socket.gethostbyname(socket.gethostname())
    context = {

    }
    return render(request, 'home.html', context)

def signup(request): 
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form" : form})


def login(request):
    form = AuthenticationForm()
    return render(request, "registration/login.html", {"form" : form})


