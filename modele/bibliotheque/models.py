from django.db import models

# Create your models here.

class Livre(models.Model): #déclare la classe Livre héritant de la classe Model, classe de base des modèles
    titre = models.CharField(max_length=100) # défini un champs de type texte de 100 caractères maximum
    auteur = models.CharField(max_length = 100)
    date_parution = models.DateField(blank=True, null = True) # champs de type date, pouvant être null ou ne pas être rempli
    nombre_pages = models.IntegerField(blank=False) # champs de type entier devant être obligatoirement rempli
    resume = models.TextField(null = True, blank = True) # champs de type text long
   # categorie = models.ForeignKey('categorie',on_delete=models.CASCADE, null=False)

    def __str__(self):
        chaine = f"{self.titre} écrit par {self.auteur} avec {self.nombre_pages} pages"
        return chaine

    def dico(self):
        return {"titre" : self.titre, "auteur" : self.auteur, "date_parution" : self.date_parution, "nombre_pages" : self.nombre_pages, "resume" : self.resume }

class Categorie(models.Model):
    nom = models.CharField(max_length=100, blank=False)
    description = models.TextField(null = True, blank = True)

    def listelivre(self,id):
        liste = list(Livre.objects.filter(categorie = id))
        return liste

    def __str__(self):
        chaine = f"la catégorie {self.nom} contient {len(self.listelivre(self.id))} \n"
        for li in self.listelivre(self.id):
            chaine += f"{li.name} écrit par {li.auteur} et paru le {li.date_parution} \n"
        return chaine