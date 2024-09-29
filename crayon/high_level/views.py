# Create your views here.
from django.views.generic import DetailView
from .models import Ville, Usine, Machine, Ressource, Stock
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


class UsineAPIView(APIView):
    def get(self, request, *arg, **kwargs):
        usines = Usine.objects.all()
        usines_info = [usine.json_extended() for usine in usines]

        return Response(usines_info)
