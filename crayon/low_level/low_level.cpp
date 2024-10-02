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
