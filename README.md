# flask_aws

Une application web développée avec Flask, déployée automatiquement sur AWS via GitHub. Le projet montre toutes les étapes du développement d'une application web, depuis la création jusqu'au déploiement dans le cloud AWS.

---

## 🚀 Aperçu

Cette application permet de documenter les étapes de développement d’un projet. Chaque étape comporte :

- Un **titre**
- Un **sous-titre**
- Une **description**

Les utilisateurs peuvent **ajouter**, **modifier** ou **supprimer** des étapes.

---

## 🔧 Fonctionnalités

- 🛠 Création et gestion de fiches "étapes"
- ☁️ Déploiement automatique sur AWS via GitHub
- 🗃 Stockage des données dans **Amazon S3**
- 🌐 Interface web simple avec Flask

---

## 🧰 Technologies

- Python & Flask
- AWS Elastic Beanstalk
- AWS S3 (stockage de la "base de données")
- Git & GitHub

---

## 🛠️ Installation locale

```
# Cloner le dépôt
git clone https://github.com/<ton-utilisateur>/flask_aws.git
cd flask_aws

# Créer un environnement virtuel
python3 -m venv venv
source venv/bin/activate  # Windows : venv\Scripts\activate

# Installer les dépendances
pip install -r requirements.txt

# Lancer le serveur local
flask run
```

# ☁️ Déploiement via GitHub vers AWS Elastic Beanstalk
## Étapes :

Pousser le projet sur GitHub

```
    git init
    git remote add origin https://github.com/<ton-utilisateur>/flask_aws.git
    git add .
    git commit -m "Initial commit"
    git push -u origin main
```
Aller dans la console AWS → Elastic Beanstalk
Créer une nouvelle application

Choisir :

        Platform : Python

        Code source : GitHub

        Connecter ton compte GitHub si nécessaire

Sélectionner ton dépôt et ta branche main

Lancer le déploiement 🚀

# 📁 Structure du projet

```
flask_aws/
│
├── app.py              # Application Flask
├── templates/          # HTML
├── static/             # CSS, JS
├── requirements.txt    # Dépendances
└── README.md
```

# 📚 Ressources

Documentation Flask : https://flask.palletsprojects.com/en/stable/
AWS Elastic Beanstalk : https://aws.amazon.com/fr/elasticbeanstalk/
AWS S3 : https://aws.amazon.com/fr/s3/
GitHub

🧑‍💻 Auteur

👤 Riad MADANI
🔗 MadaniRiad
