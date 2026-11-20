# Outils de pilote

## `registre-reservations-pilote.csv`
Registre unique de preuve pour un pilote garanti (Annexe 1, art. 2 et 6). À ouvrir dans un tableur, une ligne par réservation arrivée par un canal traçable.

- **Aucun nom, téléphone ni e-mail de client final** : le registre sert au comptage, pas au fichier client. Les coordonnées restent dans l'outil du commerce.
- `canal_tracable` : une seule valeur parmi la liste de l'en-tête (convention UTM `utm_source=<canal>&utm_campaign=pilote_<client>_<AAAAMM>`).
- `statut` : « comptée » seulement si les 5 critères de l'art. 2 sont remplis ; sinon « exclue » avec le motif.
- Point hebdomadaire : l'Analyste compte les lignes « comptée » et projette J30.
- À J30 + 10 jours : export définitif joint au bilan (art. 6).

## `modeles/`
Modèles de l'Analyste, à copier dans `livrables/<client>/A_VALIDER/` puis remplir (champs `{{ }}`, [À COMPLÉTER] si l'information manque).

- `point-hebdo-pilote.md` : point hebdomadaire du pilote (Annexe 1, art. 5.4), projection J30 et alerte.
- `bilan-j30.md` : bilan de fin de pilote (Annexe 1, art. 6 et 7), puis proposition d'abonnement Essentiel (art. 9.2).
- `rapport-mensuel-essentiel.md` : rapport mensuel d'un abonné (CGV art. 8.3).
