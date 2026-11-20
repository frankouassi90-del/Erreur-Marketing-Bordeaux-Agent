<!--
MODÈLE : point hebdomadaire pendant un pilote (Annexe 1, art. 5.4).
Copier dans livrables/{{client}}/A_VALIDER/AAAA-MM-JJ_analyste_point-hebdo-S{{n}}.md
Source unique : outils/registre-reservations-pilote.csv (lignes du client). Aucun nom, téléphone ni e-mail de client final.
Champ inconnu : écrire [À COMPLÉTER]. Ne jamais estimer une ligne du registre.
-->

# Point pilote semaine {{n}} : {{enseigne}}

## 1. Synthèse
{{X}} réservations comptées à J{{jour}} sur 10. Projection J30 : {{P}}. Trajectoire : {{dans l'objectif / sous l'objectif}}.

## 2. Point d'avancement (à envoyer au client après validation)

Bonjour {{prénom du gérant}},

Voici le point de la semaine {{n}} du pilote (du {{date début semaine}} au {{date fin semaine}}, J{{jour}} sur 30).

**Réservations à date (mesuré, registre au {{date d'extraction}})**

| Canal | Comptées | En attente | Exclues |
|---|---|---|---|
| Bouton Réserver Google (gbp_reserver) | {{n}} | {{n}} | {{n}} |
| Publication Google (gbp_post) | {{n}} | {{n}} | {{n}} |
| Lien Instagram (instagram_bio) | {{n}} | {{n}} | {{n}} |
| Bouton du site (site_bouton) | {{n}} | {{n}} | {{n}} |
| Réactivation e-mail / SMS | {{n}} | {{n}} | {{n}} |
| Publicité Google / Meta | {{n}} | {{n}} | {{n}} |
| Mot-clé au téléphone | {{n}} | {{n}} | {{n}} |
| **Total** | **{{X}}** | **{{A}}** | **{{E}}** |

- *Comptée* : les 5 critères de l'Annexe 1, art. 2 sont remplis.
- *En attente* : réservation tracée dont la date de venue n'est pas passée. Elle ne compte qu'une fois honorée.
- *Exclues* : {{motifs en une ligne, ex. 1 doublon, 1 non honorée}}.

**Projection J30 (estimé)** : {{X}} comptées en {{jour}} jours, soit {{X / jour × 30, arrondi à l'inférieur}} à J30 au rythme actuel. Avec les {{A}} réservations en attente si elles sont honorées : {{P max}}.

**{{Si projection < 10}} Alerte : la trajectoire est sous l'objectif.** Il manque {{10 − projection}} réservations au rythme actuel. Il faut {{(10 − X) / jours restants, 1 décimale}} réservation comptée par jour d'ici J30, contre {{X / jour}} aujourd'hui.

**De votre côté cette semaine**
- Contenus en attente de votre validation : {{n}} (délai contractuel : 48 h ouvrées).
- Saisie du code ou de l'origine par l'équipe : {{conforme / à rappeler}}.

**Prochaine étape** : {{action principale de la semaine suivante}}. Prochain point le {{date}}.

Erreur Marketing Bordeaux

## 3. Décisions humaines [À VALIDER]
- [ ] Envoyer ce point au client. Recommandé : oui, chaque semaine, c'est une obligation (art. 5.4).
- [ ] {{Si alerte}} Actions correctives, une seule ou deux au maximum :
  - [ ] {{Action 1, ex. relancer la campagne de réactivation sur un créneau creux}}. Effet attendu : {{estimé}}. Coût : {{€ ou temps}}.
  - [ ] {{Action 2, ex. publication Google avec lien UTM sur un créneau creux}}. Effet attendu : {{estimé}}.
  - [ ] {{Action 3, si budget pub prévu au contrat : ajuster le ciblage ou le budget}}. Toute dépense publicitaire reste une décision du client, payée par lui à la plateforme.
  Option recommandée : {{n° de l'action}}, parce que {{raison chiffrée}}.
- [ ] {{Si manquement du client à l'art. 4, ex. codes non saisis, validations en retard}} Notifier le manquement par écrit (art. 7.3, 3 jours ouvrés pour corriger). Recommandé : {{oui / non}}, ton factuel, sans reproche.
- [ ] {{Si fermeture, panne du logiciel > 48 h ou fiche suspendue}} Notifier la suspension de la Période (art. 8). Recommandé : {{oui / non}}.

## 4. Hypothèses et données manquantes
- La projection est linéaire : elle suppose le même rythme sur les jours restants. Elle ne tient pas compte des créneaux forts ou faibles.
- Statistiques de la fiche Google (vues, clics) : indicateur d'appoint, jamais compté comme réservation.
- Lignes à vérifier avec le client : {{n° de ligne et question, ou « aucune »}}.
- Données manquantes : {{ex. export du logiciel non reçu depuis le JJ/MM}}.
