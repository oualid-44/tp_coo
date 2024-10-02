#include <iostream>
using namespace std;
#include <string>

class Ville {
 private:
  string nom;
  int code_postale;
  int prix_m2;

 public:
  Ville(string name, int cp, int prix)
      : nom(name), code_postale(cp), prix_m2(prix) {};
  friend ostream& operator<<(ostream& out, const Ville& v) {
    return out << "Nom: " << v.nom << " Code postale: " << v.code_postale
               << " Prix m2 :" << v.prix_m2 << endl;
  };
};

auto main() -> int {
  Ville v("Toulouse", 31000, 100);

  cout << v;

  return 0;
}
