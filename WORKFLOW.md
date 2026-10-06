# WORKFLOW — GoSite Digital Pipeline

## 10 Agents

| # | Agent | Rôle | Outils principaux | Input | Output |
|---|---|---|---|---|---|
| 1 | 🔍 Scout | Prospection | Serper.dev API | Niche + Ville | Liste brute |
| 2 | ✅ Validator | Qualification GMB | Serper.dev + logique | Liste brute | Prospects validés |
| 3 | 📧 Email Verifier | Trouver + vérifier email | — | Prospect | Email vérifié |
| 4 | 📋 Data Mapper | Remplir la fiche | LLM + Serper | Prospect + Email | Fiche complète |
| 5 | 💻 VibeCoder | Créer le site | opencode + Nadir | Fiche client | Code site |
| 6 | 🚀 Deployer | Déployer Vercel | Vercel API + GitHub | Code site | URL preview |
| 7 | 📨 Sales Agent | Envoyer l'offre | — | URL + Fiche | Email offre |
| 8 | 💳 Payment Agent | Lien paiement | Whop API | Accord client | Paiement confirmé |
| 9 | 🌐 Domain Manager | Lier domaine | Namecheap + Vercel API | Paiement OK | Site live |
| 10 | 🛠 Support Agent | Modifications | GPT-4o + GitHub + Vercel | Demande client | Modif deployée |

## Règles

- Chaque agent ne traite que son étape — pas de saut
- L'input de chaque agent vient du output du précédent
- Les données client viennent de Sofia (scraping Serper.dev)
- Les sites suivent le prompt SITE-BUILD-PROMPT.md à la lettre
- Pas d'invention de données, pas de copier-coller
- Déploiement Vercel (pas GitHub Pages)
- Email offert après validation du site, pas de prix dans le premier email

## Séparateurs d'étapes

| Étape | Agent | Validation |
|---|---|---|
| Prospection | Scout → Validator | Liste validée |
| Contact | Email Verifier → Data Mapper | Email vérifié + fiche complète |
| Création | VibeCoder → Deployer | Code + URL preview |
| Vente | Sales Agent → Payment Agent | Email envoyé + paiement OK |
| Live | Domain Manager → Support | Site live + modifications |
