# Create your views here.
from django.views.generic import DetailView
from .models import Ville, Usine, Machine, Ressource, Stock
from django.http import JsonResponse


class VilleDetailView(DetailView):
    model = Ville

    def render_to_response(self, *args, **kwargs):
        return JsonResponse(self.object.json())


class UsineDetailVieew(DetailView):
    model = Usine

    def render_to_response(self, *args, **kwargs):
        return JsonResponse(self.object.json())


class MachineDetailView(DetailView):
    model = Machine

    def render_to_response(self, *args, **kwargs):
        return JsonResponse(self.object.json())


class RessourceDetailView(DetailView):
    model = Ressource

    def render_to_response(self, *args, **kwargs):
        return JsonResponse(self.object.json())


class StockDetailView(DetailView):
    model = Stock

    def render_to_response(self, *args, **kwargs):
        return JsonResponse(self.object.json())
