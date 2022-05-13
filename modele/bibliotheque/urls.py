from django.urls import path
from . import views, categorie_views


urlpatterns = [
    # page pour les livres
    path('indexlivre/',views.index),
    path('ajout/',views.ajout),
    path("traitement/",views.traitement),
    path("affiche/<int:id>/",views.affiche),
    path("delete/<int:id>/",views.delete),
    path("update/<int:id>/",views.update),
    path("traitementupdate/<int:id>/",views.traitementupdate),
    #pages pour les catégories
    path('',categorie_views.index),
    path('ajoutcategorie/',categorie_views.ajout),
    path("traitementcategorie/",categorie_views.traitement),
    path("affichecategorie/<int:id>/",categorie_views.affiche),
    path("deletecategorie/<int:id>/",categorie_views.delete),
    path("updatecategorie/<int:id>/",categorie_views.update),
    path("traitementupdatecategorie/<int:id>/",categorie_views.traitementupdate),
]