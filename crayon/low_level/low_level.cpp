#include <cpr/cpr.h>

#include <iostream>
#include <nlohmann/json.hpp>
#include <string>
#include <vector>
using namespace std;
using json = nlohmann::json;

class Ville {
 private:
  string nom;
  int code_postale;
  int prix_m2;

 public:
  Ville(string name, int cp, int prix)
      : nom(name), code_postale(cp), prix_m2(prix) {};
  ~Ville() {};
  friend ostream& operator<<(ostream& out, const Ville& v) {
    return out << "Nom: " << v.nom << ", Code postale: " << v.code_postale
               << ", Prix m2: " << v.prix_m2 << endl;
  };
  Ville(json data)
      : nom(data["nom"]), code_postale(data["cp"]), prix_m2(data["prix_m2"]) {};
  Ville(int id) {
    cpr::Response r =
        cpr::Get(cpr::Url{"http://localhost:8000/ville/" + to_string(id)});
    if (r.status_code == 200) {
      json data = json::parse(r.text);
      nom = data["nom"];
      code_postale = data["cp"];
      prix_m2 = data["prix_m2"];
    } else {
      cout << "Erreur avec " << id << endl;
    }
  };
};

class Objet {
 protected:
  string nom;
  int prix;

 public:
  Objet(string name, int price) : nom(name), prix(price) {};
  virtual ~Objet() = default;
};

class Local {
 protected:
  unique_ptr<Ville> ville;
  string nom;
  int surface;

 public:
  Local(unique_ptr<Ville> v, string name, int surf)
      : ville(move(v)), nom(name), surface(surf) {};
  virtual ~Local() = default;
};

class Machine {
 private:
  string nom;
  int prix;
  int n_serie;

 public:
  Machine(string name, int price, int nser)
      : nom(name), prix(price), n_serie(nser) {};
  ~Machine() {};
};

class Ressource : public Objet {
 public:
  Ressource(string name, int price) : Objet(name, price) {};
};

class QuantiteRessource {
 private:
  int quantite;
  unique_ptr<Ressource> ressource;

 public:
  QuantiteRessource(int quant, unique_ptr<Ressource> rsc)
      : quantite(quant), ressource(move(rsc)) {};
  ~QuantiteRessource() {};
};

class SiegeSocial : public Local {
 public:
  SiegeSocial(unique_ptr<Ville> v, string name, int surf)
      : Local(move(v), name, surf) {};
  ~SiegeSocial() {};
};

class Usine : public Local {
 private:
  vector<unique_ptr<Machine>> machines;

 public:
  Usine(unique_ptr<Ville> v, string name, int surf)
      : Local(move(v), name, surf) {};
  ~Usine() {};
};

class Stock {
 private:
  unique_ptr<Ressource> ressource;
  int nombre;
  unique_ptr<Usine> usine;

 public:
  Stock(unique_ptr<Ressource> rsc, int nbr, unique_ptr<Usine> usn)
      : ressource(move(rsc)), nombre(nbr), usine(move(usn)) {};
  ~Stock() {};
};

class Etape {
 private:
  string nom;
  unique_ptr<Machine> machine;
  unique_ptr<QuantiteRessource> quantite_ressource;
  int duree;
  optional<shared_ptr<Etape>> etape_suivante = nullopt;

 public:
  Etape(string name, unique_ptr<Machine> mach,
        unique_ptr<QuantiteRessource> quantress, int dur,
        optional<shared_ptr<Etape>> etp_suiv = nullopt)
      : nom(name),
        machine(move(mach)),
        quantite_ressource(move(quantress)),
        duree(dur),
        etape_suivante(etp_suiv) {};
};

class Produit : Objet {
 private:
  unique_ptr<Etape> premiere_etape;

 public:
  Produit(string name, int price, unique_ptr<Etape> prem_etp)
      : Objet(name, price), premiere_etape(move(prem_etp)) {};
};

auto main() -> int {
  Ville v("Paris", 93000, 500);
  cout << v;

  cpr::Response r = cpr::Get(cpr::Url{"http://localhost:8000/ville/1"});
  cout << r.url << std::endl;
  cout << r.status_code << std::endl;
  cout << r.header["content-type"] << std::endl;
  cout << r.text << std::endl;

  json data = json::parse(r.text);
  cout << data << endl;

  cout << data["nom"] << endl;
  cout << data["cp"] << endl;
  cout << data["prix_m2"] << endl;

  Ville t(data);
  cout << t;

  Ville q(2);
  cout << q;

  return 0;
}
