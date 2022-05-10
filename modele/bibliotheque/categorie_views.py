from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import CategorieForm

from . import  models

def ajout(request):
    if request.method == "POST":
        form = CategorieForm(request)
        if form.is_valid():
            categorie = form.save()
            return HttpResponseRedirect("/bibliotheque/")
        else:
            return render(request,"bibliotheque/ajoutcategorie.html",{"form": form})
    else :
        form = CategorieForm()
        return render(request,"bibliotheque/ajoutcategorie.html",{"form" : form})

def traitement(request):
    lform = CategorieForm(request.POST)
    if lform.is_valid():
        livre = lform.save()
        return HttpResponseRedirect("/bibliotheque/")
    else:
        return render(request,"bibliotheque/ajoutcategorie.html",{"form": lform})


def index(request):
    liste = list(models.Categorie.objects.all())
    return render(request, 'bibliotheque/', {'liste': liste})

def affiche(request, id):
    categorie = models.Categorie.objects.get(pk=id)
    return render(request,"bibliotheque/affichecategorie.html",{"categorie" : categorie})

def delete(request, id):
    categorie = models.Categorie.objects.get(pk=id)
    categorie.delete()
    return HttpResponseRedirect("/bibliotheque/")