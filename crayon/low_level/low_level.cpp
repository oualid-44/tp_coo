#include <cpr/cpr.h>

#include <iostream>
#include <nlohmann/json.hpp>
#include <string>
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

/*
class Local
{
        private:
                string nom;
                unique_ptr<Ville> ville;
                int surface;
        public:
                Local(string name, unique_ptr<Ville> v, int surf) : nom(name),
ville(v), surface(surf) {}; ~Local()
}


class Objet
{}

class SiegeSocial : public Local
{
}

class Machine
{
        private:
                string nom;
                int prix;
                int n_serie;

        public:
                Machine(string name, int price, int ns) : nom(name),
prix(price), n_serie(ns) {}; ~Machine();
}
class Usine
{
        private :
                Machine machines;

        public
}

class Ressource
{
        private :


        public
}

class stock
{
        private :


        public
}

class QuantiteRessource
{
        private :
                string ressource ;
                int nombre;

        public
}

class Etape
{
        private :
                string nom ;
                Machine machine;
                QuantiteRessource quantite_ressource;
                int dure;
                Etape etape_suivante;
        public
}

class Produit
{
        private :


        public
} */
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
