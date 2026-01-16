# tp_churn

Un projet de prédiction du churn (taux d'abandon client) utilisant le Machine Learning et les bonnes pratiques MLOps.

## 📋 Description du Projet

Ce projet implémente une solution complète de prédiction du churn client en utilisant :
- **Modèle ML** : Régression Logistique (Logistic Regression)
- **Données** : Informations clients (Âge, Account Manager, Années d'ancienneté, Nombre de sites)
- **Interface** : Application web Flask pour les prédictions en temps réel
- **Containerisation** : Docker pour un déploiement simplifié
- **Tests** : Suite de tests automatisés pour valider le modèle

## 🚀 Démarrage Rapide

### Prérequis
- Python 3.8+
- pip ou conda
- Docker (optionnel)

### Installation

1. Cloner le repository :
```bash
git clone <repository_url>
cd tp_churn
```

2. Installer les dépendances :
```bash
pip install -r requirements.txt
```

3. Entraîner le modèle :
```bash
python train.py
```

### Lancer l'application

```bash
python app.py
```

L'application sera disponible à `http://localhost:5000`

## 📁 Structure du Projet

```
tp_churn/
├── app.py                    # Application Flask pour les prédictions
├── train.py                  # Script d'entraînement du modèle
├── testapi.py               # Tests de l'API
├── requirements.txt         # Dépendances Python
├── Dockerfile               # Configuration Docker
├── README.md               # Documentation
├── data/
│   └── train_data.csv      # Données d'entraînement
├── templates/
│   └── index.html          # Interface web
└── tests/
    ├── test_train.py       # Tests unitaires du modèle
    └── test_app.py         # Tests de l'application Flask
```

## 🧪 Tests

### Tests du Modèle

Exécuter les tests du modèle :
```bash
pytest tests/test_train.py -v
```

Les tests vérifient :
- ✅ L'existence du fichier du modèle (`churn_model_clean.pkl`)
- ✅ Le type du modèle (LogisticRegression)
- ✅ La capacité du modèle à faire des prédictions
- ✅ Les probabilités de prédiction

### Tests de l'Application Flask

Exécuter les tests de l'application :
```bash
pytest tests/test_app.py -v
```

Les tests couvrent :
- ✅ Routes et endpoints (GET `/`, POST `/predict`)
- ✅ Prédictions avec données valides
- ✅ Gestion des paramètres manquants
- ✅ Validation des données invalides
- ✅ Format JSON des réponses
- ✅ Codes HTTP corrects
- ✅ Prédictions avec valeurs limites et élevées

### Exécuter tous les tests

```bash
pytest tests/ -v
```

## 🐳 Docker

### Build et run avec Docker

```bash
docker build -t tp_churn .
docker run -p 5000:5000 tp_churn
```

## 📊 Caractéristiques du Modèle

- **Type** : Régression Logistique
- **Paramètres d'entraînement** : max_iter=1000
- **Fichier du modèle** : `data/churn_model_clean.pkl`
- **Format de sérialisation** : joblib

## 📈 Utilisation de l'API

L'API accepte des requêtes POST avec les paramètres suivants :
- `Age` (int) : Âge du client
- `Account_Manager` (int) : Indicateur Account Manager (0 ou 1)
- `Years` (int) : Nombre d'années de relation
- `Num_Sites` (int) : Nombre de sites

**Exemple de requête** :
```json
{
  "Age": 30,
  "Account_Manager": 1,
  "Years": 5,
  "Num_Sites": 2
}
```

## 👨‍💻 Développement

Pour contribuer au projet :
1. Créer une branche pour votre fonctionnalité
2. Effectuer vos modifications
3. Exécuter les tests pour vérifier
4. Soumettre une pull request

## 📝 Licence

À définir
