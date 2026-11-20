# Feuille de route : du test au premier abonné

*Version du 2026-11-18. « IA » = l'équipe d'agents ; « Toi » = décision ou action humaine.*

## Phase 0. Verrouiller (semaine 1)
| Action | Qui | Statut |
|---|---|---|
| Relecture juridique CGV + 3 annexes (7 questions listées) | Toi + juriste/CCI | À faire |
| Valider prix : pilote 590 € HT, Essentiel 199 € HT, mise en place 149 € HT, plancher 30 €/h | Toi | Fait (2026-11-18) |
| Remplir les champs `{{...}}` des CGV (identité, statut, TVA, prix) | Toi, puis IA régénère le .docx | À faire |
| Réparer le connecteur Stripe (SEPA) et choisir l'outil de signature (Yousign) | Toi | À faire |
| Autoriser google.com, thefork.fr, fr.mappy.com, instagram.com dans le réseau de la session (audits fiables) | Toi (proposition prête à approuver) | Optionnel |

## Phase 1. Prospecter (semaines 1 à 3)
| Action | Qui | Statut |
|---|---|---|
| Kit de vente : script d'appel, qualification, message de premier contact, objections, relances | IA | Fait (brouillon validé pour test) |
| Vérifier Vivants sur Google Maps (5 min) puis appeler avec les questions de qualification | Toi | À faire |
| Liste de 20 restaurants à soirs creux (salons : plus tard) | IA (Chercheur) + vérification par toi | Fait, à vérifier |
| Fiches d'appel des 6 premiers restaurants | IA (Rédacteur) | Fait |
| Audits des 5 meilleurs prospects | IA (Chercheur, Stratège) | À lancer |
| 10 rendez-vous de 20 min | Toi | À faire |

## Phase 2. Livrer le premier pilote (semaines 3 à 8)
| Action | Qui | Statut |
|---|---|---|
| Bon de commande (`docs/bon-de-commande.md`) | IA | Fait (projet) |
| Signature : bon de commande + Annexes 1, 2 (et 3 si signé sur place) | Toi + client | |
| Mise en place des canaux traçables + registre (`outils/`) | IA (Développeur) + validation | |
| Production hebdomadaire : avis, publications, réactivation | IA (Rédacteur, Designer) + validation en lot | |
| Point hebdomadaire de comptage | IA (Analyste) | |
| Bilan J30 + proposition Essentiel | IA (Analyste, Stratège) + envoi par toi | |

## Phase 3. Industrialiser (à partir de 3 abonnés)
- Mesurer les heures réelles par client et corriger le chiffrage.
- Automatiser : rappel de validation hebdomadaire, programmation des publications validées, export mensuel, alerte avis négatif (IA Automatisation, scénarios désactivés jusqu'à ton feu vert).
- Demander l'accès à l'API Google Business Profile.

## Indicateurs à suivre dès le premier prospect
Rendez-vous obtenus / appels ; pilotes signés / rendez-vous ; objectif atteint / pilotes ; abonnés / pilotes ; heures par client par mois ; churn mensuel.
