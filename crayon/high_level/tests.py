# Create your tests here.
from django.test import TestCase
from .models import Ville, Usine, Machine, Ressource, Stock


class CalculCostsTest(TestCase):
    def test_creatoion(self):
        self.ville = Ville.objects.create(nom="Labege", code_postal=31670, prix_m2=2000)
        self.usine = Usine.objects.create(
            ville=self.ville, nom="Labege_Pen", surface=50
        )
        machine1 = Machine.objects.create(nom="machine1", prix=1000, n_serie=101010)
        machine2 = Machine.objects.create(nom="machine2", prix=2000, n_serie=202020)
        self.usine.machines.set([machine1, machine2])

        bois = Ressource.objects.create(nom="Bois", prix=10)
        mine = Ressource.objects.create(nom="Mine", prix=15)

        Stock.objects.create(ressource=bois, nombre=1000, usine=self.usine)
        Stock.objects.create(ressource=mine, nombre=50, usine=self.usine)

        tot_cst = 50 * 2000 + 1000 + 2000 + 1000 * 10 + 50 * 15
        self.assertEqual(self.usine.costs(), tot_cst)
