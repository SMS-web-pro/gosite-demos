# INSTRUCTION SOFIA — Scraping données client

## Objectif
Préparer les fichiers de données pour chaque prospect (24 avec email).

## Données à scraper (Serper.dev)
Pour CHAQUE prospect :
1. **Nom entreprise**
2. **Téléphone**
3. **Email** (déjà connu)
4. **Adresse / Ville / État**
5. **Services proposés** (liste précise)
6. **Horaires d'ouverture**
7. **Site web** (URL propre)
8. **Photos** (3-5 images du travail)
9. **Avis clients** (3 minimum, note + texte)
10. **Logo** (URL ou fichier)

## Format de sortie
Fichier JSON par prospect :
```json
{
  "id": 1,
  "name": "Entreprise",
  "email": "info@entreprise.com",
  "phone": "+1 xxx xxx xxxx",
  "address": "123 Main St, Ville, State",
  "services": ["service1", "service2"],
  "hours": "Mon-Fri 8-6",
  "website": "https://entreprise.com",
  "photos": ["url1", "url2"],
  "reviews": [{"rating": 5, "text": "..."}],
  "logo": "url"
}
```

## Livraison
Fichier `client_data.json` avec les 24 prospects.

## DÉLAI : Avant de commencer la construction des sites
