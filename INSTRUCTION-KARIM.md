# INSTRUCTION KARIM — Construction sites pro

## Objectif
Créer les sites professionnels selon le prompt SITE-BUILD-PROMPT.md.

## Prérequis
- Fichier `client_data.json` de Sofia (24 prospects)
- Prompt SITE-BUILD-PROMPT.md (structure obligatoire)

## Étapes
1. Lire client_data.json pour chaque prospect
2. Construire le site selon le prompt :
   - Hero (nom + tagline + CTA)
   - Services (icônes + descriptions)
   - À propos (histoire + valeurs)
   - Stats (chiffres clés)
   - Galerie (photos client)
   - Localisation (Google Maps embed)
   - Témoignages (avis clients)
   - FAQ (4-5 questions)
   - Contact (formulaire + téléphone)
   - Footer (coordonnées + liens)
3. Design : couleurs pros, 120px entre sections, mobile responsive, pas de doublons
4. Images : placehold.co 1200x800, alt text descriptif
5. Animations : AOS fade-up, max 3/section
6. SEO : title unique, meta description, canonical, Schema.org LocalBusiness

## INTERDIT
- Ne pas inventer de données client
- Ne pas ajouter de sections non demandées
- Ne pas copier-coller d'un autre site
- Pas de lorem ipsum
- Ne pas oublier Google Maps

## Déploiement
Déployer chaque site sur Vercel après construction.
URL format : `demo-[nom-prospect].vercel.app`

## Livraison
Liste des URLs Vercel déployées.
