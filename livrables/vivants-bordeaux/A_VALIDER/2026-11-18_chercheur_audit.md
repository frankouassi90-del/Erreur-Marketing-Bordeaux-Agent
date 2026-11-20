# Audit de visibilité : Vivants (13 rue des Bahutiers, Bordeaux Saint-Pierre) [À VALIDER]

*Agent : Chercheur. Relevé du 2026-11-18. Brouillon interne, ne pas montrer au prospect avant vérification humaine des chiffres.*

> **Limite de méthode, à lire avant tout.** Le 2026-11-18, la lecture directe des pages web était bloquée dans la session : `fr.mappy.com` et `www.thefork.fr` ont renvoyé « getaddrinfo ENOTFOUND » (hôtes hors des domaines réseau autorisés), comme `www.google.com` et `www.justacote.com` lors du test précédent. Je n'ai donc pas tenté d'autres sites (ni restaurantvivants.com, ni Instagram, ni Zenchef). **Aucune fiche Google, aucune page TheFork, aucun site de restaurant n'a été lu directement.** Tous les chiffres viennent d'**extraits de résultats de recherche web** (outil WebSearch) qui citent des guides (Michelin, Gault&Millau, Le Fooding), de la presse (Gilles Pudlowski, Palate Mag, Le Bonbon) ou des agrégateurs (En Primeur Club, Sluurpy, lacarte.menu, TripAligner, Foodle, Cylex). Un chiffre « Google » est donc un **chiffre Google rapporté par un tiers, non vérifié sur la fiche**, avec une date de collecte inconnue. Pour lever ce blocage : autoriser `www.google.com`, `fr.mappy.com`, `www.thefork.fr` et `www.instagram.com` dans les réglages réseau de la session, ou faire le relevé à la main.

---

## 1. Synthèse

- Vivants (13 rue des Bahutiers, Saint-Pierre) vend un menu du soir de **45 à 75 € par personne hors boissons** (Gault&Millau), mais **aucune réservation en ligne n'a été trouvée** : le Guide Michelin indique que le restaurant « gère ses propres réservations ».
- La qualité n'est pas le problème (4,7 sur Google selon En Primeur Club, 13/20 Gault&Millau, Assiette Michelin 2025 selon En Primeur Club). Le problème est l'accès : réservation par téléphone, service du soir seulement, horaires contradictoires selon les sources, Instagram introuvable.
- Pilote possible : lien de réservation tracé (UTM) sur la fiche Google et le site. Prérequis bloquant : vérifier sur Google Maps et par un appel au standard l'absence de bouton Réserver, la capacité et les soirs creux.

---

## 2. Livrables

### 2.1 Les 3 candidats relevés (étape 1)

Relevé du 2026-11-18 par WebSearch. « Google » = note Google relayée par l'agrégateur cité, non lue sur Google.

| Enseigne | Type de cuisine | Quartier | Note et avis (plateforme) | Réservation en ligne | Prix moyen visible | Signal faible | Source | Date du relevé |
|---|---|---|---|---|---|---|---|---|
| **Vivants**, 13 rue des Bahutiers, 33000 | Cuisine moderne, menus « à l'aveugle », cave de plus de 800 références | Saint-Pierre (Gault&Millau : « à quelques minutes de la place de la Bourse » ; TableJourney et Le Bonbon placent la rue des Bahutiers à Saint-Pierre) | Google 4,7 sur 237 avis, ou 4,7 sur 371 avis (deux pages En Primeur Club, chiffres contradictoires) | **Non trouvée.** Michelin : « this establishment manages its own bookings. Please contact the restaurant directly » ; version française : « réservation n'est pas disponible sur notre site » | Soir : 45 € (3 plats) à 75 € (5 plats) hors boissons (Gault&Millau). Avril 2024 : menus 45 et 60 €, carte 70 à 75 € (Pudlowski). Midi 25 à 30 € (Le Fooding, date non affichée) | Pas de réservation en ligne visible ; horaires contradictoires (Cylex, Foodle, Michelin) ; Instagram non trouvé ; service du soir seulement, fermé le week-end | [Gault&Millau](https://fr.gaultmillau.com/fr/restaurants/vivants-33000) ; [Michelin](https://guide.michelin.com/us/en/nouvelle-aquitaine/bordeaux/restaurant/vivants) ; [En Primeur Club](https://www.enprimeurclub.com/restaurants/vivants-bordeaux-restaurant) ; [Pudlowski](https://www.gillespudlowski.com/?p=370039) ; [Le Fooding](https://lefooding.com/restaurants/vivants) | 2026-11-18 |
| **Le Millésime**, 4 rue du Puits des Cujols, 33000 | Française, européenne ; restaurant et bar à vins, tapas, grands crus au verre | [À COMPLÉTER] (hypercentre ; quartier exact non donné par une source) | Google 4,1 sur 116 avis (Sluurpy) | [À COMPLÉTER] : aucune page de réservation trouvée | [À COMPLÉTER] (Sluurpy : « €€ », sans montant) | Note < 4,3 ; < 150 avis ; horaires très réduits selon Sluurpy (midi en semaine, soir le vendredi seulement, samedi fermé) ; activité actuelle non confirmée | [Sluurpy](https://www.sluurpy.fr/bordeaux/restaurant/1983702/le-mill%C3%A9sime-bordeaux) ; [Wanderlog](https://extensionembed.wanderlog.com/place/details/6740559) | 2026-11-18 |
| **Le Cinq**, 5 allées de Tourny, 33000 | Bistronomique ou traditionnelle selon les sources ; viandes (onglet, tartare), planches, rhums, terrasse | [À COMPLÉTER] (allées de Tourny, hypercentre ; quartier exact non donné par une source) | Google 4,1 sur 499 avis (Sluurpy) ; lacarte.menu 4,0 sur 203 avis (page mise à jour le 31.03.2026) | [À COMPLÉTER] : aucune page de réservation trouvée ; tarifs « à consulter par téléphone » (koifaire) | Partiel : un plat à 16 € visible sur lacarte.menu ; prix moyen [À COMPLÉTER] | Note < 4,3 ; avis mitigés (lenteur, prix des vins) ; deux numéros de téléphone différents selon les annuaires | [Sluurpy](https://www.sluurpy.fr/bordeaux/restaurant/1991087/le-cinq) ; [lacarte.menu](https://lacarte.menu/restaurants/bordeaux/le-cinq-13/menu) ; [koifaire](https://www.koifaire.com/aquitaine/le,cinq-7105.html) | 2026-11-18 |

**Écartés** (relevés le 2026-11-18) : Bistrot Le Charabia, 26 rue du Maréchal Joffre (Mappy 8,6/10 sur 72 avis, budget à partir de 30,50 €, pas de page de réservation trouvée) : ticket trop bas pour le pilote ([Mappy, extrait de recherche](https://fr.mappy.com/activite/restaurant/33150-bordeaux)). Saint Seurin Le Bistrot (Google 4,1 sur 63 avis selon [Sluurpy](https://www.sluurpy.fr/bordeaux/restaurant/1998342/saint-seurin-le-bistrot)) : prix et activité non confirmés. La Table de Burdigala (Google 3,8 sur 29 avis selon Sluurpy) : restaurant d'hôtel, pas indépendant. La Fine Bouche (30 rue du Hâ, pas de réservation en ligne selon Michelin) : 846 à 953 avis Google à 4,9, visibilité déjà forte.

**Choix pour l'audit : Vivants.** Raisons :
1. **Réservation en ligne absente** : c'est le seul des trois où l'absence est attestée par une source tierce (Michelin), et pas seulement déduite.
2. **Ticket visible et élevé** : 45 à 75 € par personne hors boissons (Gault&Millau), contre un ticket inconnu (Le Millésime) ou partiel (Le Cinq). Le test précédent a montré qu'un ticket bas rend le pilote non rentable.
3. **Commerce actif** : fiche Gault&Millau 2026 (13/20), Cylex mis à jour en février 2026, Assiette Michelin 2025 (selon En Primeur Club). Pour Le Millésime et Le Cinq, l'activité actuelle n'est pas démontrée.
4. **Limite à garder en tête** : les signaux faibles de Vivants portent sur l'accès (réservation, horaires, réseaux), pas sur la note. Le restaurant n'a ni note < 4,3 ni moins de 150 avis. Le Millésime et Le Cinq ont des notes plus faibles mais des données économiques trop lacunaires pour un pilote.

### 2.2 Audit de visibilité : Vivants

| Indicateur | Constat | Source | Date du relevé |
|---|---|---|---|
| Adresse | 13 rue des Bahutiers, 33000 Bordeaux (Michelin, Gault&Millau, Pudlowski, Cylex concordent) | [Michelin](https://guide.michelin.com/gb/en/nouvelle-aquitaine/bordeaux/restaurant/vivants) ; [Gault&Millau](https://fr.gaultmillau.com/fr/restaurants/vivants-33000) | 2026-11-18 |
| Chef, équipe | Tanguy Laviale (ex-Garopapilles, tient aussi Ressources) ; Maxime Courvoisier, sommelier | [Gault&Millau](https://fr.gaultmillau.com/fr/restaurants/vivants-33000) ; [Le Fooding](https://lefooding.com/en/restaurants/vivants) | 2026-11-18 |
| Ancienneté | Article d'avril 2024 qui présente le lieu ; date d'ouverture exacte [À COMPLÉTER] | [Pudlowski](https://www.gillespudlowski.com/?p=370039) | 2026-11-18 |
| Catégorie Google | [À COMPLÉTER] : fiche Google non lisible. Guides : « cuisine moderne » (Michelin, €€), « Table de Chef » (Gault&Millau) | [Michelin](https://guide.michelin.com/gb/en/nouvelle-aquitaine/bordeaux/restaurant/vivants) ; [Gault&Millau](https://fr.gaultmillau.com/fr/restaurants/vivants-33000) | 2026-11-18 |
| Note Google | 4,7/5 | [En Primeur Club](https://www.enprimeurclub.com/restaurants/vivants-bordeaux-restaurant) | 2026-11-18 |
| Nombre d'avis Google | 237 ou 371 selon deux pages du même agrégateur : contradiction à lever sur la fiche | [En Primeur Club](https://www.enprimeurclub.com/restaurants/vivants-bordeaux-restaurant) | 2026-11-18 |
| Rythme des avis récents | [À COMPLÉTER] : dates des avis Google non lisibles ; aucun avis daté de 2026 trouvé dans les extraits | Recherches WebSearch du jour | 2026-11-18 |
| Réponses aux avis | [À COMPLÉTER] | n/a | 2026-11-18 |
| Ce que disent les critiques | Cuisine jugée « l'une des meilleures tables récemment apparues à Bordeaux » (Palate Mag, 14/20, novembre 2024), avec un reproche : manque de transparence sur la carte et les vins. Service lent au début (Jane Anson). Prix de l'amuse-bouche au champagne critiqué (blog 2024) | [Palate Mag](https://www.palatemag.co.uk/vivants/) ; [Jane Anson](https://janeanson.com/restaurant-review-vivants) | 2026-11-18 |
| Bouton Réserver Google | [À COMPLÉTER] sur la fiche. Indice fort d'absence : Michelin indique que le restaurant gère ses propres réservations, sans module en ligne | [Michelin](https://guide.michelin.com/us/en/nouvelle-aquitaine/bordeaux/restaurant/vivants) | 2026-11-18 |
| Logiciel de réservation | Aucun trouvé (ni TheFork, ni Zenchef dans les extraits). Réservation par téléphone : 09 78 81 13 55 (standard cité par Pudlowski en 2024 et Foodle) | [Pudlowski](https://www.gillespudlowski.com/?p=370039) ; [Foodle](https://foodle.pro/restaurants/bordeaux/restaurant-vivants) | 2026-11-18 |
| Carte et prix | Soir : menu à l'aveugle 45 € (3 plats), aménageable jusqu'à 75 € (5 plats), hors boissons (Gault&Millau 2026). Avril 2024 : menus 45 et 60 €, carte 70 à 75 € (Pudlowski). Midi : formules 25 à 30 € (Le Fooding, date non affichée, peut-être caduc si le midi n'est plus servi) | [Gault&Millau](https://fr.gaultmillau.com/fr/restaurants/vivants-33000) ; [Pudlowski](https://www.gillespudlowski.com/?p=370039) ; [Le Fooding](https://lefooding.com/restaurants/vivants) | 2026-11-18 |
| **Prix moyen par couvert** | **45 € minimum hors boissons au dîner** (menu le moins cher). Haut de fourchette 75 € hors boissons. Panier moyen réel avec vin : [À COMPLÉTER] (à demander au gérant) | [Gault&Millau](https://fr.gaultmillau.com/fr/restaurants/vivants-33000) | 2026-11-18 |
| **Capacité** | Nombre de couverts : [À COMPLÉTER] (aucune source trouvée). Services : dîner du mardi au vendredi, 19 h 30 à 21 h 30 (Foodle, Cylex) ; Cylex ajoute le lundi soir ; Michelin indique fermé le lundi ; fermé samedi et dimanche (Pudlowski, Jane Anson). Soit 4 ou 5 services par semaine selon la source | [Foodle](https://foodle.pro/restaurants/bordeaux/restaurant-vivants) ; [Cylex](https://www.cylex-locale.fr/entreprises/vivants-14885847.html) ; [Pudlowski](https://www.gillespudlowski.com/?p=370039) | 2026-11-18 |
| Horaires sur la fiche Google | [À COMPLÉTER] ; les annuaires se contredisent (lundi ouvert ou fermé), ce qui suggère des horaires à fiabiliser | voir ligne Capacité | 2026-11-18 |
| Photos Google | [À COMPLÉTER] | n/a | 2026-11-18 |
| Dernière publication Google | [À COMPLÉTER] | n/a | 2026-11-18 |
| Site web | restaurantvivants.com (cité par Pudlowski, En Primeur Club, Foodle). Contenu, présence d'un module de réservation, vitesse : [À COMPLÉTER] (site non lu, voir limite de méthode) | [Pudlowski](https://www.gillespudlowski.com/?p=370039) ; [En Primeur Club](https://www.enprimeurclub.com/restaurants/vivants-bordeaux-restaurant) | 2026-11-18 |
| Instagram | Aucun compte trouvé dans les extraits de recherche. Identifiant, abonnés, fréquence : [À COMPLÉTER] (instagram.com non consulté) | Recherches WebSearch du jour | 2026-11-18 |
| Facebook, TikTok | Aucun compte trouvé : [À COMPLÉTER] | Recherches WebSearch du jour | 2026-11-18 |
| Distinctions | Gault&Millau 13/20, « Table de Chef » ; Assiette Michelin 2025 selon En Primeur Club (la page Michelin lue en extrait ne le mentionne pas) | [Gault&Millau](https://fr.gaultmillau.com/fr/restaurants/vivants-33000) ; [En Primeur Club](https://www.enprimeurclub.com/restaurants/vivants-bordeaux-restaurant) | 2026-11-18 |
| SIREN, dirigeant, effectif | [À COMPLÉTER] : connecteurs Pappers et Contract-Factory SIREN non exposés à cet agent | n/a | 2026-11-18 |

### 2.3 Concurrents proches

Distances à pied : [À COMPLÉTER] (pas d'accès à une carte). Berthus est dans la même rue, au numéro 15. Le Chien de Pavlov (rue de la Devise) et Bô-tannique (place Saint-Projet) sont rattachés au quartier Saint-Pierre ou au centre historique par les sources, sans distance mesurée.

| Indicateur | Vivants (audité) | Berthus, 15 rue des Bahutiers | Le Chien de Pavlov, 45-47 rue de la Devise | Bô-tannique, 2 rue Tustal (place Saint-Projet) |
|---|---|---|---|---|
| Type | Cuisine moderne, menus à l'aveugle, cave nature | Bistronomie, menu unique du Sud-Ouest | Néo-bistrot, menu dégustation du marché | Cuisine moderne de saison, vins bio et nature |
| Note Google | 4,7 (En Primeur Club) | [À COMPLÉTER] | [À COMPLÉTER] | [À COMPLÉTER] |
| Avis Google | 237 ou 371 (En Primeur Club) | [À COMPLÉTER] | [À COMPLÉTER] | [À COMPLÉTER] |
| Autres notes | Gault&Millau 13/20 ; Palate Mag 14/20 | TripAligner 4,7 sur 2 627 avis ; lacarte.menu 4,2 sur 9 013 avis (plateforme d'origine non précisée) | TripAligner 4,3 sur 903 avis ; Petit Futé 4,3 sur 38 ; Groupon 4,5 sur 36 ; Gault&Millau 12,5/20 | Naboo 4,7 sur 818 avis ; Gault&Millau 13,5/20 |
| Réservation en ligne | Non trouvée (Michelin : réservation gérée en direct) | Non trouvée ; réservation par téléphone, conseillée une semaine à l'avance pour le dîner | Non trouvée ; « call to book » ; présence Groupon | **Oui** : bouton « Réserver une table » sur la fiche Michelin ; outil [À COMPLÉTER] |
| Prix moyen par couvert | 45 à 75 € hors boissons, dîner | 28 € le menu entrée-plat-dessert (novembre 2024) | Dîner 48 à 49 € ; déjeuner 21 à 28 € (sources d'âges variés) | 25 à 45 € hors boissons ; midi dès 21 € (article 2021) |
| Services | Dîner seulement, mardi à vendredi | Midi et soir (horaires contradictoires selon les sources) | Mardi soir, mercredi à samedi midi et soir ; brunch le dimanche | Fermé le lundi ; midi et soir en semaine (horaires exacts [À COMPLÉTER]) |
| Site / réseaux | restaurantvivants.com ; Instagram non trouvé | Site et réseaux [À COMPLÉTER] | lechiendepavlov.com ; e-mail générique de contact publié | bo-tannique.com ; réseaux [À COMPLÉTER] |
| Atout visible | Qualité reconnue par les guides, prix élevé assumé | Prix bas et menu unique : capte le dîner « bon rapport qualité-prix » de la rue | Ouvert le samedi et le dimanche (brunch), présence sur Groupon | Réservation en ligne, terrasse sur place piétonne, volume d'avis (818 sur Naboo) |
| Sources | voir 2.2 | [Le Bonbon](https://www.lebonbon.fr/bordeaux/actu/berthus-restaurant-mieux-note-bordeaux-menu-unique/) ; [TripAligner](https://tripaligner.com/countries/france-18/destinations/bordeaux-11735/places/restaurant-berthus-16868749) ; [lacarte.menu](https://lacarte.menu/restaurants/bordeaux/berthus) ; [Bordeaux Tourism](https://www.bordeaux-tourism.co.uk/restaurant/berthus.html) | [Petit Futé](https://www.petitfute.com/v1524-bordeaux-33000/c1165-restaurants/c4-cuisine-francaise/1544076-le-chien-de-pavlov/tous-les-avis.html) ; [TripAligner](https://tripaligner.com/countries/france-18/destinations/bordeaux-11735/places/le-chien-de-pavlov-6754355) ; [Groupon](https://www.groupon.fr/biz/bordeaux/le-chien-de-pavlov-rue-de-la-devise) ; [TableJourney](https://tablejourney.com/france/bordeaux/restaurants/le-chien-de-pavlov/) | [Michelin](https://guide.michelin.com/ca/fr/nouvelle-aquitaine/bordeaux/restaurant/bo-tannique) ; [Gault&Millau](https://fr.gaultmillau.com/en/restaurants/bo-tannique) ; [Naboo](https://www.naboo.app/en-us/explorer/restaurants/bo-tannique) ; [Barnes](https://www.barnes-bordeaux.com/en/news/living-in-bordeaux-7/bo-tannique-gastronomic-restaurant-place-saint-projet-555-555) |
| Date du relevé | 2026-11-18 | 2026-11-18 | 2026-11-18 | 2026-11-18 |

Remarque : Berthus et Le Chien de Pavlov ne prennent pas non plus de réservation en ligne visible. Le seul concurrent proche qui en affiche une est Bô-tannique. Vivants n'est donc pas en retard sur toute la rue, mais il peut prendre l'avance.

### 2.4 Les 3 écarts qui coûtent le plus de clients

1. **Pas de réservation en ligne, avec un service du soir seulement.** Vivants n'ouvre que 4 ou 5 soirs par semaine, de 19 h 30 à 21 h 30 (Foodle, Cylex). Une personne qui cherche une table le midi ou en soirée, quand personne ne décroche, ne peut pas réserver. Bô-tannique, dans le même secteur, affiche un bouton de réservation sur sa fiche Michelin. À 45 € minimum par couvert hors boissons, chaque appel manqué coûte cher. C'est aussi le levier le plus direct du pilote : un lien de réservation tracé (UTM) sur la fiche Google et le site.
2. **Informations pratiques contradictoires.** Selon les annuaires, le restaurant est ouvert ou fermé le lundi, et le midi est mentionné par Le Fooding mais pas par les autres. Un client qui voit des horaires faux ou un midi qui n'existe plus se déplace pour rien ou renonce. Fiabiliser les horaires sur Google et sur les annuaires est l'écart le moins cher à corriger.
3. **Une réputation de guide, mais peu visible pour le grand public.** Instagram introuvable, aucun avis Google daté de 2026 trouvé, et un volume d'avis Google incertain (237 ou 371) face aux 818 avis de Bô-tannique sur Naboo. Les critiques reprochent aussi le manque de transparence de la carte : un menu « à l'aveugle » sans contenu visible en ligne freine la réservation d'un client qui découvre l'adresse. Montrer les plats (photos, publications Google, Instagram) et demander un avis à chaque client satisfait, sans contrepartie, réduirait ce frein.

### 2.5 Action précise proposée

Faire vérifier par un humain, sur Google Maps et par un appel au 09 78 81 13 55 (standard du restaurant) : (a) l'absence de bouton Réserver et de module sur restaurantvivants.com, (b) le nombre d'avis Google et la date des 5 derniers, (c) les soirs d'ouverture, le nombre de couverts et les soirs les moins remplis. Si (a) est confirmé et qu'il existe des soirs creux, le Stratège prépare une proposition de pilote 30 jours : lien de réservation UTM sur la fiche Google et le site, horaires fiabilisés, publications Google montrant les plats. Promesse à reprendre mot pour mot : « 10 nouvelles réservations traçables en 30 jours. Sinon, vous ne payez pas nos honoraires\*. »

Ordre de grandeur, à confirmer : 10 réservations au menu le moins cher (45 € hors boissons, Gault&Millau) représentent au moins 450 € de repas hors boissons si chaque réservation compte un seul couvert. Le nombre de couverts par réservation et le panier avec vin sont [À COMPLÉTER].

---

## 3. Décisions humaines [À VALIDER]

- [À VALIDER] **Choix du prospect** : Vivants (recommandé : ticket élevé et réservation en ligne absente attestée), ou Le Cinq (note 4,0 à 4,1, mais ticket et activité à confirmer). Le Millésime n'est pas recommandé tant que son activité n'est pas confirmée.
- [À VALIDER] **Vérifier si Vivants a besoin de clients.** Le chef tient aussi Ressources et Vivants est reconnu par les guides : le restaurant peut être déjà complet. Option recommandée : appel au standard avant toute prise de contact commerciale, pour savoir s'il reste des soirs creux. Sans soirs creux, pas de pilote.
- [À VALIDER] **Vérifier par sondage les chiffres Google** (note, nombre d'avis 237 ou 371, bouton Réserver, horaires, photos, dernière publication). Option recommandée : relevé manuel de 10 minutes, ou autoriser `www.google.com` dans les réglages réseau de la session pour un relevé ciblé.
- [À VALIDER] **Lancer l'enrichissement SIREN, dirigeant, effectif** via Pappers ou Contract-Factory SIREN depuis la session principale. Option recommandée : oui, avant la proposition (effectif nécessaire pour l'Annexe 3 si 5 salariés ou moins).
- [À VALIDER] **Choix de l'outil de réservation à proposer** (Zenchef, TheFork, autre). Option recommandée : vérifier la compatibilité « Réserver avec Google » et la possibilité d'un lien tracé par canal avant de recommander un outil. Ne pas présumer que le chef veut une plateforme à commission.

---

## 4. Hypothèses et données manquantes

**Blocages précis**
- `fr.mappy.com` et `www.thefork.fr` : « getaddrinfo ENOTFOUND », hôtes hors des domaines autorisés de la session (2026-11-18). `www.google.com` et `www.justacote.com` étaient déjà bloqués au test précédent. Conséquence : aucune lecture directe de fiche Google, de page TheFork, de site de restaurant ou d'Instagram. Toutes les données viennent d'extraits de recherche web.
- Connecteurs Pappers et Contract-Factory SIREN : non exposés à cet agent.

**Données manquantes [À COMPLÉTER]**
- Vivants : nombre exact d'avis Google, dates des avis récents, réponses aux avis, catégorie Google, bouton Réserver (lecture directe), photos, dernière publication, horaires affichés sur Google.
- Vivants : nombre de couverts, soirs creux, panier moyen avec boissons, existence actuelle d'un service du midi, date d'ouverture.
- Vivants : site (contenu, module de réservation, vitesse), Instagram, Facebook, TikTok.
- Vivants : SIREN, dirigeant, effectif.
- Concurrents : notes et avis Google de Berthus, Le Chien de Pavlov et Bô-tannique ; outil de réservation de Bô-tannique ; distances à pied.
- Candidats : quartier exact, ticket et activité du Millésime et du Cinq.

**Hypothèses**
- Les notes « Google » viennent d'agrégateurs (En Primeur Club, Sluurpy) qui disent relayer Google, à une date de collecte inconnue.
- L'absence de réservation en ligne de Vivants vient de la mention Michelin « gère ses propres réservations » et de l'absence de résultat TheFork ou Zenchef dans les recherches. Ce n'est pas une observation directe de la fiche Google ni du site.
- Le rattachement de la rue des Bahutiers au quartier Saint-Pierre vient de TableJourney et du Bonbon (à propos de Berthus, au numéro 15).
- Les prix des concurrents ont des âges variés (2021 à 2026) et peuvent avoir changé.
- Aucune donnée personnelle de client final n'a été collectée ; aucun nom d'auteur d'avis n'est recopié. Les seuls contacts relevés sont le standard du restaurant et, pour un concurrent, une adresse e-mail générique de contact publiée par un annuaire (non recopiée ici). Les noms cités (chef, sommelier, critiques) sont des professionnels nommés publiquement par les guides et la presse.
