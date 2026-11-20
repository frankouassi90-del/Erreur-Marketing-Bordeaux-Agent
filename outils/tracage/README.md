# Traçage des pilotes

Outils pour rattacher chaque réservation d'un pilote garanti à un canal que nous avons créé (Annexe 1 des CGV, art. 2). Tout se fait en local : rien n'est mis en ligne, aucun service externe n'est appelé.

> **Règle : une réservation sans canal tracé ne compte pas.** Pas de lien UTM reconnu, pas de code cité, pas de demande de formulaire avec `canal` renseigné : la ligne va dans le registre en « exclue », motif « sans canal tracé ». Même si le client dit « je vous ai trouvés sur Google ».

## Fichiers

| Fichier | Rôle |
|---|---|
| `generer_liens.py` | Génère le plan de traçage : 1 lien UTM et 1 code court par canal, dans un CSV |
| `test_generer_liens.py` | Tests unitaires du script (bibliothèque standard) |
| `modele-formulaire-reservation.html` | Formulaire de demande de réservation autonome, qui recopie les UTM dans le champ caché `canal`. Modèle sans envoi réel [À VALIDER] |

## Utilisation en 3 commandes

```bash
cd outils/tracage
python3 -m unittest test_generer_liens -v
python3 generer_liens.py vivants-bordeaux "https://[À COMPLÉTER : URL de réservation]" 202612 --sortie ../../livrables/vivants-bordeaux/A_VALIDER
```

- `client` : slug du dossier `clients/<client>`.
- `url_base` : URL de la page ou de l'outil de réservation. Ses paramètres existants (`?lang=fr`) et son ancre (`#form`) sont conservés ; d'anciens `utm_*` sont remplacés, jamais doublés.
- `mois` : mois de J1, format `AAAAMM`.
- `--prefixe` : préfixe des codes (défaut : 3 premières lettres du slug, `VIV`).
- `python3 generer_liens.py --help` pour le détail.

Sortie : `plan-tracage_<client>_<AAAAMM>.csv`, séparateur `;`, colonnes `canal ; lien ; code ; ou_placer ; preuve_attendue ; test_avant_j1`.

Convention : `utm_source=<canal>&utm_medium=<type>&utm_campaign=pilote_<client>_<AAAAMM>`.

## Où placer chaque lien

| Canal | `utm_medium` | Code | Où le placer | Preuve attendue |
|---|---|---|---|---|
| `gbp_reserver` | reservation | `XXX-GBP` | Fiche Google, champ « Lien de réservation » | Export ou demande de formulaire avec ce canal ; clics Google en appoint seulement |
| `gbp_post` | publication | `XXX-POST` | Bouton de chaque publication Google | Idem |
| `instagram_bio` | bio | `XXX-INSTA` | Lien de la bio Instagram | Idem |
| `site_bouton` | bouton | `XXX-SITE` | Bouton « Réserver » du site du commerce | Idem |
| `email_reactivation` | email | `XXX-MAIL` | Bouton de l'e-mail de réactivation (clients existants, lien de désinscription) | Stats d'envoi agrégées + export ou code cité |
| `sms_reactivation` | sms | `XXX-SMS` | Lien du SMS de réactivation (clients existants, mention STOP) | Idem |
| `gads` | cpc | `XXX-GADS` | URL finale des annonces Google Ads | Rapport de campagne + export |
| `meta_ads` | paid_social | `XXX-META` | URL de destination des publicités Meta | Rapport de campagne ou ID de formulaire pub + export |

Le canal `mot_cle_telephone` du registre n'a pas de lien : il repose sur un mot ou un code dit au téléphone, noté par l'équipe du commerce.

**Codes courts** : ce sont des identifiants, pas des réductions. Associer un avantage à un code engage le commerce et passe par une décision [À VALIDER]. Ils servent quand le lien ne garde pas la source (client qui rappelle après un e-mail ou un SMS : « citez le code VIV-MAIL »).

## Avant J1 (KPI : 100 % des liens testés)

1. Ouvrir chaque lien du CSV sur un téléphone, vérifier que la page s'affiche et que `canal` est rempli (le formulaire modèle l'affiche après un envoi test).
2. Vérifier que l'outil de réservation retenu garde la source dans son export. Sinon, repli sur le formulaire + registre.
3. Remplir la colonne `test_avant_j1` (date + capture). Un lien non testé ne part pas.
4. Placement des liens sur la fiche Google, le site, Instagram, les envois ou les pubs : **action externe, [À VALIDER] par l'humain**.

## Formulaire modèle

`modele-formulaire-reservation.html` s'ouvre directement dans un navigateur (aucune dépendance). Essai local : ouvrir le fichier puis ajouter `?utm_source=gbp_reserver&utm_medium=reservation&utm_campaign=pilote_vivants-bordeaux_202612` à l'adresse.

- Champ caché `canal` = `source|medium|campagne` si la source est un canal du registre, sinon `sans_canal`.
- L'attribut `action` est vide et l'envoi est bloqué : à brancher sur l'outil du restaurant après validation, jamais sur un outil d'IA (prénom et téléphone de clients finaux).
- Tous les `[À COMPLÉTER]` (nom, adresse, horaires, téléphone, responsable du traitement, durée de conservation, politique de confidentialité) viennent de la fiche client vérifiée.
