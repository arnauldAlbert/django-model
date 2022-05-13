from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import CategorieForm

from . import  models

def ajout(request):
        form = CategorieForm()
        return render(request,"bibliotheque/categorie/ajout.html",{"form" : form})

def traitement(request):
    cform = CategorieForm(request.POST)
    if cform.is_valid():
        categorie = cform.save()
        return HttpResponseRedirect("/bibliotheque/")
    else:
        return render(request,"bibliotheque/categorie/ajout.html",{"form": cform})


def index(request):
    liste = list(models.Categorie.objects.all())
    return render(request, 'bibliotheque/categorie/index.html', {'liste': liste})

def affiche(request, id):
    categorie = models.Categorie.objects.get(pk=id)
    return render(request,"bibliotheque/categorie/affiche.html",{"categorie" : categorie})

def delete(request, id):
    categorie = models.Categorie.objects.get(pk=id)
    categorie.delete()
    return HttpResponseRedirect("/bibliotheque/")

def update(request,id):
    categorie = models.Categorie.objects.get(pk=id)
    form = CategorieForm(categorie.dico())
    return render(request,"bibliotheque/categorie/update.html",{"form":form, "id": id})

def traitementupdate(request,id):
    cform = CategorieForm(request.POST)
    if cform.is_valid():
        categorie = cform.save(commit = False)
        categorie.id = id
        categorie.save()
        return HttpResponseRedirect("/bibliotheque/")
    else:
        return render(request,"bibliotheque/categorie/update.html",{"form": cform})
