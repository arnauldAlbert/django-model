from django.urls import path
from . import views, categorie_views


urlpatterns = [
    path('',views.index),
    path('ajout/',views.ajout),
    path("traitement/",views.traitement),
    path("affiche/<int:id>/",views.affiche),
    path("delete/<int:id>",views.delete),
    path("update/<int:id>",views.update),
    path("traitementupdate/<int:id>",views.traitementupdate),
    path('ajoutcategorie/',categorie_views.ajout),
    path("traitementcategorie/",categorie_views.traitement),
    path("affichecategorie/<int:id>/",categorie_views.affiche),
    path("deletecategorie/<int:id>",categorie_views.delete),

]