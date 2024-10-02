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
    return out << "Nom: " << v.nom << " Code postale: " << v.code_postale
               << " Prix m2 :" << v.prix_m2 << endl;
  };
};

auto main() -> int {
  Ville v("Toulouse", 31000, 100);

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

  return 0;
}
