from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import LivreForm
from . import  models
# Create your views here.
def ajout(request,id):
        form = LivreForm()
        return render(request,"bibliotheque/livre/ajout.html",{"form" : form, "id": id})

def traitement(request,id):
    categorie = models.Categorie.objects.get(pk=id)
    lform = LivreForm(request.POST)
    if lform.is_valid():
        livre = lform.save(commit=False)
        livre.categorie = categorie
        livre.categorie_id = id
        livre.save()
        return HttpResponseRedirect("/bibliotheque/indexlivre/")
    else:
        return render(request,"bibliotheque/livre/ajout.html",{"form": lform})


def index(request):
    liste = list(models.Livre.objects.all())
    return render(request, 'bibliotheque/livre/index.html', {'liste': liste})

def affiche(request, id):
    livre = models.Livre.objects.get(pk=id)
    liste = livre.editeur_set.all()
    return render(request,"bibliotheque/livre/affiche.html",{"livre" : livre, "liste" :liste})

def delete(request, id):
    livre = models.Livre.objects.get(pk=id)
    livre.delete()
    return HttpResponseRedirect("/bibliotheque/indexlivre/")

def update(request, id):
    livre = models.Livre.objects.get(pk=id)
    lform = LivreForm(livre.dico())
    return render(request, "bibliotheque/livre/update.html", {"form": lform,"id":id})

def traitementupdate(request, id):
    lform = LivreForm(request.POST)
    if lform.is_valid():
        livre = lform.save(commit=False)
        livre.id = id
        livre.save()
        return HttpResponseRedirect("/bibliotheque/indexlivre/")
    else:
        return render(request, "bibliotheque/livre/update.html", {"form": lform, "id": id})
