# Projet Crayon

Ce projet est une application web et une application bas niveau combinant Django pour la gestion des données côté serveur et C++ pour le traitement des données. L'objectif est de modéliser des entités comme des villes, des usines et des machines, tout en exploitant une API REST pour échanger les données entre les deux environnements.

---

## Dépendances

### Python
- Python 3.9 ou supérieur
- pip
- virtualenv
- Django
- pre-commit

### C++
- CMake
- CPR (HTTP requests)
- nlohmann/json (JSON parsing)

---

## Installation et Compilation

### Partie Python
1. **Création d'un environnement virtuel**
   ```bash
   mkdir tp_coo
   cd tp_coo
   git init
   python -m venv .venv
   echo .venv >> .gitignore
   source .venv/bin/activate
   pip install -U pip
   pip install django
   django-admin startproject crayon
   ```

2. **Configurer le dépôt distant**
   ```bash
   ssh-keygen -t ed25519
   cat ~/.ssh/id_ed25519.pub
   git config --global user.name "Votre Nom"
   git config --global user.email "votre.email@example.com"
   git branch -M main
   git remote add origin git@github.com:utilisateur/depot.git
   git add .
   git commit -m "Initialisation du projet"
   git push -u origin main
   ```

3. **Configurer les outils**
   ```bash
   wget https://gitlab.laas.fr/gsaurel/teach/-/raw/main/.pre-commit-config.yaml
   pip install pre-commit
   pre-commit install
   pre-commit run -a
   git add .
   git commit -m "Configuration des outils"
   git push
   ```

4. **Lancer le serveur**
   ```bash
   ./manage.py makemigrations
   ./manage.py migrate
   ./manage.py createsuperuser
   ./manage.py runserver
   ```

---

### Partie C++
1. **Configuration du projet**
   ```bash
   mkdir low_level
   cd low_level
   wget https://gitlab.laas.fr/gsaurel/teach/-/raw/main/src/CMakeLists.txt
   pip install cmake
   ```

2. **Création du fichier `low_level.cpp`**
   Implémentez une classe `Ville` avec un constructeur et une méthode d'affichage. Ajoutez une fonction principale pour créer une instance et l'afficher.

3. **Compilation**
   ```bash
   cmake -B build -S .
   cmake --build build
   ./build/low_level
   echo build >> .gitignore
   ```

4. **Intégration des bibliothèques**
   - **CPR** : Faites une requête HTTP vers l'API pour récupérer les données JSON.
   - **nlohmann/json** : Parsez et utilisez les données JSON récupérées.

5. **Construction avancée**
   - Ajoutez des constructeurs supplémentaires pour gérer les données JSON et les identifiants.
   - Implémentez les autres modèles avec `std::unique_ptr` et `std::optional` pour gérer les relations et les attributs non requis.

---

Ce projet permet de maîtriser l’interaction entre une API Django et une application C++ via un processus de développement clair et rigoureux.

