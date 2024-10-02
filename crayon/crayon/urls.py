"""
URL configuration for crayon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from high_level.views import (
    VilleDetailView,
    UsineDetailView,
    MachineDetailView,
    RessourceDetailView,
    QuantiteRessourceDetailView,
    EtapeDetailView,
    ProduitDetailView,
    StockDetailView,
    VilleAPIView,
    UsineAPIView,
    MachineAPIView,
    RessourceAPIView,
    SiegeSocialAPIView,
    QuantiteRessourceAPIView,
    EtapeAPIView,
    ProduitAPIView,
    StockAPIView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("ville/<int:pk>/", VilleDetailView.as_view(), name="ville-detail"),
    path("usine/<int:pk>/", UsineDetailView.as_view(), name="usine-detail"),
    path("machine/<int:pk>/", MachineDetailView.as_view(), name="machine-detail"),
    path("ressource/<int:pk>/", RessourceDetailView.as_view(), name="ressource-detail"),
    path(
        "quantiteressource/<int:pk>",
        QuantiteRessourceDetailView.as_view(),
        name="quantiteressource-detail",
    ),
    path("etape/<int:pk>/", EtapeDetailView.as_view(), name="etape-detail"),
    path("produit/<int:pk/>", ProduitDetailView.as_view(), name="produit-detail"),
    path("stock/<int:pk>/", StockDetailView.as_view(), name="stock-detail"),
    path("api/villes/", VilleAPIView.as_view(), name="ville-api"),
    path("api/usines/", UsineAPIView.as_view(), name="usine-api"),
    path("api/machines/", MachineAPIView.as_view(), name="machine-api"),
    path("api/ressources/", RessourceAPIView.as_view(), name="ressource-api"),
    path("api/siegessociaux/", SiegeSocialAPIView.as_view(), name="siegesocial-api"),
    path(
        "api/quantiteressources/",
        QuantiteRessourceAPIView.as_view(),
        name="quantiteressource-api",
    ),
    path("api/etatpes/", EtapeAPIView.as_view(), name="etape-api"),
    path("api/produits/", ProduitAPIView.as_view(), name="produit-api"),
    path("api/stocks/", StockAPIView.as_view(), name="stock-api"),
]
