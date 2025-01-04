from django.db import models


# Create your models here.
class Ville(models.Model):
    nom = models.CharField(max_length=100)
    code_postal = models.IntegerField()
    prix_m2 = models.IntegerField()

    def __str__(self):
        return f"{self.nom} {self.code_postal}"

    def json(self):
        return {"nom": self.nom, "cp": self.code_postal, "prix_m2": self.prix_m2}

    def json_extended(self):
        return self.json()


class Local(models.Model):
    ville = models.ForeignKey(Ville, on_delete=models.PROTECT)
    nom = models.CharField(max_length=100)
    surface = models.IntegerField()

    def __str__(self):
        return f"{self.nom} {self.ville} {self.surface}"

    class Meta:
        abstract = True

    def json_extended(self):
        return {
            "nom": self.nom,
            "surface": self.surface,
            "ville": self.ville.json_extended(),
        }


class Objet(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nom} {self.prix}"

    class Meta:
        abstract = True

    def json_extended(self):
        return {"nom": self.nom, "prix": self.prix}


class Machine(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.IntegerField()
    n_serie = models.IntegerField()

    def __str__(self):
        return f"{self.nom} {self.prix} {self.n_serie}"

    def costs(self):
        return self.prix

    def json(self):
        return {"nom": self.nom, "prix": self.prix, "n_serie": self.n_serie}

    def json_extended(self):
        return self.json()


class Usine(Local):
    machines = models.ManyToManyField(Machine)

    def __str__(self):
        return ", ".join(machine.nom for machine in self.machines.all())
        # return f"{self.nom} - Usine"

    def costs(self):
        somme_machine = sum(machine.prix for machine in self.machines.all())
        local_cost = self.ville.prix_m2 * self.surface
        stock_cost = sum(stock.costs() for stock in self.stock_set.all())
        return local_cost + somme_machine + stock_cost

    def json(self):
        return {"machines": [machine.nom for machine in self.machines.all()]}

    def json_extended(self):
        return {
            "nom": self.nom,
            "surface": self.surface,
            "ville": self.ville.json_extended(),
            "machines": [machine.json_extended for machine in self.machines.all()],
            "stocks": [stock.json_extended for stock in self.stock_set.all()],
            "total_cost": self.costs(),
        }


class Ressource(Objet):
    def json(self):
        return {"nom": self.nom, "prix": self.prix}

    def json_extended(self):
        return {
            "nom": self.nom,
            "prix": self.prix,
            "stock": [
                {"usine": stock.usine.nom, "nombre": stock.nombre}
                for stock in self.stock_sett.all()
            ],
        }


class SiegeSocial(Local):
    def json_extended(self):
        return super().json_extended()


class QuantiteRessource(models.Model):
    ressource = models.ForeignKey(Ressource, on_delete=models.CASCADE)
    quantite = models.IntegerField()

    def __str__(self):
        return f"{self.ressource} {self.quantite}"

    def costs(self):
        return self.ressource.prix * self.quantite

    def json(self):
        return {"ressource": self.ressource.nom, "quantite": self.quantite}

    def json_extended(self):
        return {
            "ressource": self.ressource.json_extended(),
            "quantite": self.quantite,
            "costs": self.costs(),
        }


class Etape(models.Model):
    nom = models.CharField(max_length=100)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    quantite_ressource = models.ForeignKey(QuantiteRessource, on_delete=models.CASCADE)
    duree = models.IntegerField()
    etape_suivante = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.nom} {self.machine} {self.quantite_ressource} {self.duree} {self.etape_suivante}"

    def json(self):
        return {
            "nom": self.nom,
            "quantite_ressource": self.quantite_ressource.quantite,
            "duree": self.duree,
            "etape_suivante": self.etape_suivante.nom,
        }

    def json_extended(self):
        return {
            "nom": self.nom,
            "machine": self.machine.json_extended(),
            "quantite_ressource": self.quantite_ressource.json_extended(),
            "duree": self.duree,
            "etape_suivante": self.etape_suivante.json_extended()
            if self.etape_suivante
            else None,
        }


class Produit(Objet):
    premiere_etape = models.ForeignKey(Etape, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nom} {self.premiere_etape}"

    def json(self):
        return {"premiere_etape": self.premiere_etape.nom}

    def json_extended(self):
        return {
            "nom": self.nom,
            "prix": self.prix,
            "premiere_etape": self.premiere_etape.json_extended(),
        }


class Stock(models.Model):
    ressource = models.ForeignKey(Ressource, on_delete=models.PROTECT)
    nombre = models.IntegerField()
    usine = models.ForeignKey(Usine, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.ressource} {self.nombre}"

    def costs(self):
        return self.ressource.prix * self.nombre

    def json(self):
        return {
            "ressource": self.ressource.nom,
            "nombre": self.nombre,
            "usine": self.usine.nom,
        }

    def json_extended(self):
        return {
            "ressource": self.ressource.json_extended(),
            "nombre": self.nombre,
            "usine": self.usine.json_extended(),
            "costs": self.costs(),
        }
        # Ou bien self.usine.nom si l'extentet est non necessaire
