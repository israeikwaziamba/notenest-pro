from django.db import models

class Semestre(models.Model):
    nom = models.CharField(max_length=50)

    def _str_(self):
        return self.nom

class Matiere(models.Model):
    nom = models.CharField(max_length=100)
    semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE)

    def _str_(self):
        return self.nom

class Note(models.Model):
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    valeur = models.FloatField()
    coefficient = models.FloatField()

    def moyenne_pondérée(self):
        return self.valeur * self.coefficient

    def _str_(self):
        return f"{self.matiere} : {self.valeur}"