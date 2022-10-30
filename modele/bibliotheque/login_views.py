from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/bibliotheque/accueil/")

def accueil(request):
    return render(request, "bibliotheque/accueil.html")

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect("/bibliotheque/")
    else:
        return HttpResponseRedirect("/bibliotheque/login/", {"msg":"bad credential"})
