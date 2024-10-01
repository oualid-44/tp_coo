# Create your views here.
from django.views.generic import DetailView
from .models import (
    Ville,
    Usine,
    Machine,
    Ressource,
    Stock,
    SiegeSocial,
    QuantiteRessource,
    Etape,
    Produit,
)
from django.http import JsonResponse

# Install djangorestframework using "pip install djangorestframework"
# in order to use the following libraries
# Add the 'reset_framwork', in INSTALLED_APPS in settings.py
from rest_framework.views import APIView
from rest_framework.response import Response


class VilleDetailView(DetailView):
    model = Ville

    def render_to_response(self, *args, **kwargs):
        return JsonResponse(self.object.json())


class UsineDetailView(DetailView):
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


class VilleAPIView(APIView):
    def get(self, request, *arg, **kwags):
        villes = Ville.objects.all()
        ville_info = [ville.json_extended() for ville in villes]

        return Response(ville_info)


class UsineAPIView(APIView):
    def get(self, request, *arg, **kwargs):
        usines = Usine.objects.all()
        usines_info = [usine.json_extended() for usine in usines]

        return Response(usines_info)


class MachineAPIView(APIView):
    def get(self, request, *arg, **kwargs):
        machines = Machine.objects.all()
        machines_info = [machine.json_extended() for machine in machines]

        return Response(machines_info)


class RessourceAPIView(APIView):
    def get(self, request, *arg, **kwargs):
        ressources = Ressource.objects.all()
        ressources_info = [ressource.json_extended() for ressource in ressources]

        return Response(ressources_info)


class SiegeSocialAPIView(APIView):
    def get(self, request, *arg, **kwargs):
        siegessociaux = SiegeSocial.objects.all()
        siegessociaux_info = [
            siegesocial.json_extended() for siegesocial in siegessociaux
        ]

        return Response(siegessociaux_info)


class QuantiteRessourceAPIView(APIView):
    def get(self, request, *arg, **kwargs):
        quantitesressources = QuantiteRessource.objects.all()
        quantitesressources_info = [
            quantiteressource.json_extended()
            for quantiteressource in quantitesressources
        ]

        return Response(quantitesressources_info)


class EtapeAPIView(APIView):
    def get(self, request, *arg, **kwargs):
        etapes = Etape.objects.all()
        etapes_info = [etape.json_extended() for etape in etapes]

        return Response(etapes_info)


class ProduitAPIView(APIView):
    def get(self, request, *arg, **kwargs):
        produits = Produit.objects.all()
        produits_info = [produit.json_extended() for produit in produits]

        return Response(produits_info)


class StockAPIView(APIView):
    def get(self, request, *arg, **kwargs):
        stocks = Stock.objects.all()
        stocks_info = [stock.json_extended() for stock in stocks]

        return Response(stocks_info)
