#include <iostream>
using namespace std;
#include <cpr/cpr.h>

#include <nlohmann/json.hpp>
#include <string>

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
  std::cout << r.url << std::endl;
  std::cout << r.status_code << std::endl;
  std::cout << r.header["content-type"] << std::endl;
  std::cout << r.text << std::endl;

  return 0;
}
