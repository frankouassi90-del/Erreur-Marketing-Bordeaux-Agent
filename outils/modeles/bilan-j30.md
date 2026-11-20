<!--
MODÈLE : bilan de fin de pilote (Annexe 1, art. 6 et 7), suivi de la proposition d'abonnement (art. 9.2).
Copier dans livrables/{{client}}/A_VALIDER/AAAA-MM-JJ_analyste_bilan-j30.md
Calendrier : Source de Preuve reçue au plus tard à J30 + 10 jours (art. 4.7), bilan remis au plus tard à J30 + 15 jours (art. 5.5).
Source : export du logiciel de réservation + registre outils/registre-reservations-pilote.csv. Aucune donnée personnelle de client final.
Règle : en cas de doute sur une ligne, elle est exclue et le motif est écrit.
Conserver UNE seule des trois conclusions (A, B ou C) et supprimer les deux autres.
-->

# Bilan du pilote 30 jours : {{enseigne}}

## 1. Synthèse
{{X}} réservations garanties sur 10 entre le {{J1}} et le {{J30}}. Objectif {{atteint / non atteint}}. Conséquence : {{facture de 590 € HT / aucun honoraire et proposition de prolongation de 30 jours / honoraires au prorata, art. 7.3}}.

## 2. Bilan (à envoyer au client après validation)

Bonjour {{prénom du gérant}},

Voici le bilan du pilote, établi conformément à l'Annexe 1 des CGV, article 6.

**Période** : du {{J1, date}} (J1) au {{J30, date}} (J30){{, prolongée de N jours pour suspension, art. 8, si applicable}}.
**Source de preuve** : export {{Zenchef / TheFork / registre}} du {{date}}, complété par {{statistiques des liens UTM / numéro de suivi / codes saisis}}.
**Définition retenue** : une réservation = {{1 table, quel que soit le nombre de couverts}}, créée entre J1 et J30, arrivée par un canal traçable, honorée (ou, venue après J30, non annulée à J30 + 7 jours), sans doublon.

### Résultat
| | Nombre |
|---|---|
| Réservations tracées enregistrées | {{T}} |
| Exclues | {{E}} |
| **Réservations garanties** | **{{X}}** |
| Objectif | 10 |

### Décompte ligne à ligne (mesuré)
| N° | Créée le | Venue le | Canal | Preuve | Couverts | Statut |
|---|---|---|---|---|---|---|
| 1 | {{AAAA-MM-JJ}} | {{AAAA-MM-JJ}} | {{canal}} | {{ligne d'export n° / code / ID formulaire / appel du JJ/MM}} | {{n}} | Comptée |
| … | | | | | | |

### Lignes exclues et motifs
| N° | Canal | Motif |
|---|---|---|
| {{n}} | {{canal}} | {{doublon / non honorée / hors période / groupe au-delà de la limite / sans canal tracé / personnel ou proche}} |

### Conclusion

**[A] Objectif atteint ({{X}} réservations garanties, 10 ou plus).**
Conformément à l'article 7.1, nous vous adressons la facture des honoraires du pilote : **590 € HT**, payable à 30 jours à compter de la date de facture.

**[B] Objectif non atteint ({{X}} réservations garanties sur 10), vos obligations ayant été respectées.**
Conformément à l'article 7.2, **aucun honoraire n'est dû** pour le pilote. Nous vous proposons une **prolongation gratuite de 30 jours**, du {{date}} au {{date}}, que vous êtes libre d'accepter ou de refuser. Si l'objectif cumulé de 10 réservations garanties est atteint à la fin de la prolongation, les honoraires de 590 € HT seront dus. Sinon, le pilote prend fin sans aucun frais d'honoraires. Merci de nous indiquer votre choix par écrit avant le {{date}}.

**[C] Objectif non atteint, manquement notifié et non corrigé.**
Le {{date}}, nous vous avons notifié par écrit {{le manquement, ex. codes non saisis}} (art. 4.{{n}}), non corrigé dans les 3 jours ouvrés. Conformément à l'article 7.3, la garantie ne s'applique pas. Les honoraires sont dus au prorata des prestations réalisées : {{montant}} € HT, soit {{%}} du prix du pilote, dans la limite de {{50}} %. Détail des prestations réalisées : {{liste}}.

Dans tous les cas, le budget publicitaire payé directement aux plateformes ({{montant}} € TTC constaté) reste à votre charge (art. 7.4).

**Contestation** : vous disposez de **8 jours ouvrés** à compter de la réception de ce bilan, soit jusqu'au {{date}}, pour contester par écrit une ou plusieurs lignes en précisant le motif. Les lignes non contestées sont réputées acceptées (art. 6.2). En cas de désaccord persistant, nous nous rencontrons dans les 15 jours pour un examen contradictoire (art. 6.3).

### Et maintenant

**Ce que les réservations tracées vous ont apporté (estimation)**

| | Valeur | Nature |
|---|---|---|
| Réservations garanties | {{X}} | Mesuré |
| Couverts sur ces réservations | {{C}} | Mesuré (export) |
| Ticket moyen par couvert | {{€ TTC}} | Déclaré par vous |
| Chiffre d'affaires TTC | {{C × ticket}} € | Estimé |
| Chiffre d'affaires HT | {{C × ticket / (1 + taux de TVA)}} € | Estimé |

{{X}} réservations tracées représentent environ **{{CA HT}} € HT** de chiffre d'affaires sur 30 jours, soit environ **{{CA HT / X}} € HT par réservation**.

L'abonnement Essentiel coûte **199 € HT par mois**. Au panier constaté, **{{arrondi supérieur de 199 / (CA HT / X)}} réservations tracées par mois** suffisent à le couvrir. Pendant le pilote, vous en avez eu {{X}}.

Ce chiffre est une estimation : il ne mesure pas votre marge et nous ne garantissons pas de chiffre d'affaires (art. 10). Certaines réservations tracées viennent peut-être de clients qui seraient venus autrement.

**Notre proposition** : poursuivre avec l'abonnement Essentiel, 199 € HT par mois, engagement de 3 mois puis résiliable avec 30 jours de préavis. Il comprend la gestion de votre fiche Google, les réponses à tous vos avis, {{4}} publications par mois et un rapport mensuel qui garde le même compteur de réservations tracées. Les liens et codes du pilote restent actifs.

Le pilote ne se transforme jamais automatiquement en abonnement : si vous souhaitez continuer, nous vous envoyons un bon de commande à signer (art. 9.2). Pouvons-nous en parler {{jour proposé}} à {{heure}}, 15 minutes ?

Erreur Marketing Bordeaux

## 3. Décisions humaines [À VALIDER]
- [ ] Valider le décompte ligne à ligne avant envoi. Recommandé : relire chaque ligne exclue et chaque ligne au statut douteux.
- [ ] Conclusion retenue : {{A / B / C}}. Recommandé : {{A ou B}} ; n'utiliser C que si la notification écrite du manquement existe et est datée.
- [ ] {{Si A}} Émettre la facture de 590 € HT. Recommandé : le jour de l'envoi du bilan.
- [ ] {{Si B}} Proposer la prolongation de 30 jours avec un plan d'action révisé. Recommandé : {{oui, si projection réaliste / à discuter}}.
- [ ] Proposition d'abonnement Essentiel à 199 € HT/mois jointe au bilan. Recommandé : oui (art. 9.2).
- [ ] Rentabilité consultant (interne, ne pas envoyer) : {{heures passées sur le pilote}} h pour {{590 / 0}} € HT, soit {{€/h}} contre un plancher de 30 €/h. Abonnement estimé à 3 h par mois, soit environ 62 €/h (strategie/chiffrage-abonnement-essentiel.md).

## 4. Hypothèses et données manquantes
- Ticket moyen : déclaré par le client le {{date}}, non vérifié sur sa caisse.
- Taux de TVA : {{10 % restauration sur place ; à ajuster si une part de boissons alcoolisées à 20 % est significative}}.
- Réservations venues après J30 : retenues seulement si non annulées à J30 + 7 jours ({{date}}).
- Statistiques de la fiche Google : non utilisées comme preuve.
- Données manquantes : {{liste ou « aucune »}}.
