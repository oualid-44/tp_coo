# Create your views here.
from django.views.generic import DetailView
from .models import Ville, Usine, Machine, Ressource, Stock


class VilleDetailView(DetailView):
    model = Ville


class UsineDetailVieew(DetailView):
    model = Usine


class MachineDetailView(DetailView):
    model = Machine


class RessourceDetailView(DetailView):
    model = Ressource


class StockDetailView(DetailView):
    model = Stock
