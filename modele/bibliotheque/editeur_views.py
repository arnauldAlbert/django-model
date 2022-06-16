from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import EditeurForm
from . import  models
# Create your views here.

def ajout(request):
    form = EditeurForm()
    return render(request, "bibliotheque/editeur/ajout.html", {"form": form})

def traitement(request):
    listeli = list(models.Livre.objects.all())
    lform = EditeurForm(request.POST)
    if lform.is_valid():
        editeur = lform.save()
        return render(request,"bibliotheque/editeur/affiche.html",{"editeur": editeur, "listeedi": editeur.livreEdite, "listeli": listeli})
    else:
        return render(request, "bibliotheque/editeur/ajout.html", {"form": lform})

def affiche(request, id):
    editeur = models.Editeur.objects.get(pk=id)
    listeli = list(models.Livre.objects.all())
    return render(request, "bibliotheque/editeur/affiche.html", {"editeur": editeur, "listeedi": editeur.livreEdite.all(), "listeli": listeli})

def ajoutlivre(request,id):
    editeur = models.Editeur.objects.get(pk=id)
    editeur.save()
    for idl in request.POST.getlist("livres"):
        livre = models.Livre.objects.get(pk=idl)
        editeur.livreEdite.add(livre)
    editeur.save()
    listeli = list(models.Livre.objects.all())
    return render(request, "bibliotheque/editeur/affiche.html", {"editeur": editeur, "listeedi": editeur.livreEdite.all(), "listeli": listeli})