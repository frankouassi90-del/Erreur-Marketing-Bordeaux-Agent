# Décisions en attente de validation

*État au 2026-11-18. Coche `[x]` ou corrige la recommandation. Ordre = ce qui bloque le plus en premier.*

## A. Bloquant avant le premier contact client (VALIDÉ le 2026-11-18)

| # | Décision | Recommandation | Source |
|---|---|---|---|
| A1 | Taux horaire plancher | 30 € HT/h | `strategie/chiffrage-abonnement-essentiel.md` |
| A2 | Objectif de revenu net mensuel | 3 000 €, soit 21 abonnés à 199 € | idem |
| A3 | Prix Essentiel restaurant | 199 € HT/mois | idem |
| A4 | Prix Essentiel coiffure | Test 149 contre 199 € HT/mois | idem |
| A5 | Prix du pilote restaurant | 590 € HT, temps plafonné à 20 h | `livrables/vivants-bordeaux/.../stratege_proposition-pilote.md` |
| A6 | Frais de mise en place sans pilote | 149 € HT | chiffrage |
| A7 | Règle d'éligibilité au pilote | Restaurants seulement, au moins 8 tables libres par semaine ; sinon Essentiel sans garantie | `CLAUDE.md` |
| A8 | Engagement initial Essentiel | 3 mois | `docs/cgv.md` art. 5 |
| A9 | Kit de vente | Valider, puis tester sur 5 appels avant retouche | `livrables/_interne/A_VALIDER/..._kit-de-vente.md` |
| A10 | Promesse au premier contact | Aucune (ni prix ni garantie) tant que l'éligibilité n'est pas connue | kit de vente |

## B. Bloquant avant la première signature

| # | Décision | Recommandation |
|---|---|---|
| B1 | Relecture juridique des CGV et des 3 annexes | Obligatoire, CCI Bordeaux Gironde ou avocat |
| B2 | Questions au juriste | (1) Rétractation de 14 jours pour un commerce de 5 salariés ou moins démarché sur place ; (2) clause du tribunal de commerce selon ton statut ; (3) prorata de 50 % en cas de manquement du client ; (4) rétractation à 0 € pendant le pilote face à la règle du prorata (L221-25) ; (5) calendrier de la facturation électronique ; (6) cession de droits sur des contenus produits en partie par IA ; (7) engagement de 3 mois face à des TPE fragiles ; (8) interdiction de paiement pendant 7 jours après une signature sur place face au prélèvement d'avance de l'Essentiel, et Annexe 3 à étendre à l'Essentiel ; (9) demander les accès du client pendant le délai de rétractation ; (10) mention des visuels de synthèse IA à ajouter à l'art. 12.3 |
| B3 | Remplir les champs `{{...}}` des CGV | Identité, statut, TVA, prix (A3 à A6), seuils |
| B4 | Seuils de l'Annexe 1 | Réservation restaurant = 1 table, groupes de plus de 8 exclus ; seuil coiffure 25 € TTC (si un jour pilote coiffure) ; capacité minimale de 8 tables libres par semaine |
| B5 | Budget publicitaire client par défaut | 0 €, option Google Search de 200 € TTC décidée à J10 si moins de 3 réservations |
| B6 | Outil de preuve des réservations | Registre (`outils/`) + formulaire tracé ; Zenchef seulement si le restaurant le veut ; TheFork déconseillé |
| B7 | Encaissement | Réparer le connecteur Stripe (prélèvement SEPA) |
| B8 | Signature électronique | Yousign (environ 9 € HT/mois, non vérifié) |
| B9 | Bon de commande (`docs/bon-de-commande.md`) | À joindre à la relecture juridique |

## C. Prospects (avant chaque appel)

| # | Décision | Recommandation |
|---|---|---|
| C1 | Vivants | Vérifier 5 min sur Google Maps, puis appeler avec la grille de qualification, sans prix |
| C2 | Salon L'Essentiel | Le passer en Essentiel sans garantie, ou l'abandonner : adresse contradictoire, données à confirmer |
| C3 | Liste de 20 restaurants (`livrables/_interne/A_VALIDER/..._prospects-restaurants.md`) | Vérifier sur Google Maps le top 5 : Baud et Millet, Bistrot La Rémoulade, La Table de Bécassine, Le Bistro du Musée, Le Cinq ; puis appels de qualification |
| C5 | Restaurants déjà sur TheFork (Bécassine, Bistro du Musée) | Confirmer qu'on peut distinguer nos réservations des leurs ; sinon, Essentiel sans garantie |
| C4 | Chaque message de prospection | Relire le constat chiffré et sa source avant envoi |

## D. Confort (non bloquant)

| # | Décision | Recommandation |
|---|---|---|
| D1 | Autoriser google.com, thefork.fr, fr.mappy.com, instagram.com, sluurpy.fr, restoranking.fr dans le réseau de la session cloud | Oui, pour des audits fiables (proposition à approuver) |
| D2 | Outil de publication | Postiz (skill déjà installé) ou Metricool |
| D3 | E-mail et SMS | Brevo via Make |
| D4 | Accès à l'API Google Business Profile | Demander dès le premier abonné |
| D5 | Fusion de la branche de travail dans `main` | Après tes validations A et B |

## Journal
| Date | Décision | Choix |
|---|---|---|
| 2026-11-18 | A1 à A10 | Validées telles que recommandées (fondateur). Reportées dans les CGV, l'Annexe 1 et `CLAUDE.md`. |
