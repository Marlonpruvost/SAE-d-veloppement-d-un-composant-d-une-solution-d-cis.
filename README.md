---
title: "SAE_API"
author: "Marlon Pruvost"
date: "2026-04-22"
output: html_document
---

# API REST - Gestion et classification d’écritures bancaires

##  Auteurs
- Marlon PRUVOST

---

##  Contexte du projet

Ce projet s’inscrit dans une démarche de développement d’un composant d’une chaîne décisionnelle.

L’objectif est de créer une **API REST** avec Python et Flask permettant de manipuler des écritures bancaires et de simuler leur classification.

---

##  Objectif

Développer une API REST capable de :
- afficher une liste d’écritures bancaires
- afficher une écriture spécifique
- ajouter une écriture
- modifier une écriture
- supprimer une écriture

Les données utilisées sont des **données simulées (mock data)** afin de tester l’API.

---

##  Concepts utilisés

Ce projet permet de comprendre :

- le fonctionnement d’une API REST
- le protocole HTTP
- les méthodes :
  - GET (lecture)
  - POST (création)
  - PUT (mise à jour)
  - DELETE (suppression)
- la communication client / serveur
- le format JSON

---

##  Technologies utilisées

- Python
- Flask
- API REST
- JSON
- curl (tests en ligne de commande)

---

##  Structure du projet

sae_api/
│
├── app.py # Code principal de l’API Flask
├── README.md # Documentation du projet


---

##  Installation et exécution

### 1. Cloner le projet
```bash
git clone <URL_DU_REPO>
cd sae_api
```

### 2. Installer Flask

pip install flask

### 3. Lancer l’API

python app.py

## Accès à l’API

Une fois l’API lancée, elle est accessible à l’adresse : http://127.0.0.1:5050

## Tests de l’API avec curl

🔹 Lister toutes les écritures

curl http://127.0.0.1:5050/entries

🔹 Ajouter une écriture

curl -X POST http://127.0.0.1:5050/entries

🔹 Modifier une écriture

curl -X PUT http://127.0.0.1:5050/entries/1

🔹 Supprimer une écriture

curl -X DELETE http://127.0.0.1:5050/entries/1

## Fonctionnement de l’API REST

Une API REST (Representational State Transfer) permet la communication entre un client et un serveur via HTTP.
Chaque ressource est identifiée par une URL et manipulée à l’aide de requêtes HTTP.


