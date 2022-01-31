from django.db import models

# Create your models here.


class Bracket(models.Model):
    name = models.CharField(max_length=200)
    afcWildCard1 = models.CharField(max_length=200)
    afcWildCard2 = models.CharField(max_length=200)
    afcWildCard3 = models.CharField(max_length=200)
    nfcWildCard1 = models.CharField(max_length=200)
    nfcWildCard2 = models.CharField(max_length=200)
    nfcWildCard3 = models.CharField(max_length=200)
    afcDivisional1 = models.CharField(max_length=200)
    afcDivisional2 = models.CharField(max_length=200)
    nfcDivisional1 = models.CharField(max_length=200)
    nfcDivisional2 = models.CharField(max_length=200)
    afcChampions = models.CharField(max_length=200)
    nfcChampions = models.CharField(max_length=200)
    superbowl = models.CharField(max_length=200)
    superbowlTieBreaker = models.IntegerField()
    points = models.IntegerField()
    id = models.IntegerField(unique=True, primary_key=True)

    def __str__(self):
        return self.name
