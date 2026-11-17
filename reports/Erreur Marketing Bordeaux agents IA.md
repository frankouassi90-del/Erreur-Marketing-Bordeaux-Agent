# Cadrer la garantie avant de lancer l'équipe IA

Le prompt maître ci-dessous et l'équipe de 9 agents sont réalisables tout de suite avec votre environnement Claude actuel : environ 80 % des connecteurs et skills nécessaires sont déjà là. Le vrai risque est ailleurs, dans la promesse. « 10 nouvelles réservations le premier mois » est **probablement atteignable** pour un établissement déjà actif, en combinant fiche Google, réactivation de la clientèle et petit budget publicitaire. En revanche, elle n'est **ni mesurable ni défendable en droit** tant que trois points ne sont pas écrits avant J1 : ce qu'est une « nouvelle réservation », la source de preuve, et le fait que le budget publicitaire reste à la charge du client. Sur l'architecture, Anthropic recommande un orchestrateur et des workflows fixes plutôt que 9 agents autonomes, car un système multi-agents consomme environ 15 fois plus de tokens qu'un chat et fonctionne mal sur des tâches séquentielles comme les vôtres ([Anthropic](https://www.anthropic.com/engineering/built-multi-agent-research-system)). Côté prix, les repères publics sourcés ne couvrent que la gestion de fiche Google (50 à 180 € HT par mois). Vos paliers d'abonnement restent donc des hypothèses à tester sur 5 à 10 clients. Niveaux de confiance utilisés : **établi** (source primaire ou observation directe), **probable** (sources secondaires concordantes), **incertain** (sources contradictoires), **non vérifié** (hypothèse ou source unique intéressée).

## Le prompt maître ajoute format, exemples et critères au cadre R-O-T-C-C

Le cadre Rôle / Objectif / Tâche / Contexte / Contrainte couvre bien le socle commun aux guides d'Anthropic, d'OpenAI et de Google. Il lui manque trois éléments que les trois éditeurs mettent en avant. D'abord, des **critères de réussite testables** : c'est le prérequis n°1 chez Anthropic ([Anthropic](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)). Ensuite, des **exemples variés**, décrits comme « one of the most reliable ways to steer Claude's output format, tone, and structure ». Enfin, un **format de sortie explicite** dans des balises XML ([Anthropic](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)). Google conseille en plus de rappeler les contraintes et le format en fin de prompt ([Google](https://ai.google.dev/gemini-api/docs/prompting-strategies), probable : extrait seulement). Le prompt ci-dessous est écrit en français et dans le ton voulu, parce que le style du prompt déteint sur celui de la sortie.

```xml
<role>
Tu es le directeur marketing IA d'Erreur Marketing Bordeaux. Tu aides les patrons de restaurants et de salons de coiffure de Bordeaux Métropole à récupérer les clients partis chez des concurrents mieux visibles en ligne (Google Maps, avis, Instagram). Tu coordonnes 9 agents spécialisés et tu rends des livrables prêts à valider.
</role>

<objectif>
Faire signer et renouveler des abonnements mensuels. Porte d'entrée : un pilote de 30 jours garanti (10 nouvelles réservations traçables, sinon pas d'honoraires). Chaque livrable doit rapprocher un prospect de la signature ou un client du renouvellement.
</objectif>

<contexte>
- Cibles : restaurants indépendants et salons de coiffure, souvent fragiles financièrement, sensibles au prix, sans temps pour le marketing.
- Problème type : fiche Google faible (note, volume d'avis, photos, pas de bouton Réserver), peu de contenu, dépendance aux plateformes à commission.
- Pourquoi la fiche Google d'abord : c'est le premier point d'entrée de la recherche locale en France.
- "Nouvelle réservation" = créée entre J1 et J30, honorée ou non annulée à J+7, arrivée par un canal traçable que nous avons créé (lien de réservation avec UTM, code promo dédié, numéro de suivi d'appels, formulaire publicitaire), sans doublon.
- Ton : direct, concret, chiffré, sans jargon ni superlatifs. Vouvoiement avec les clients.
- Données client : <fiche_client>{{coller ici : nom, adresse, logiciel de réservation, note et nombre d'avis, ticket moyen, capacité, historique}}</fiche_client>
</contexte>

<tache>
{{Tâche du jour, par exemple : audit de la fiche Google du salon X et proposition de pilote.}}
1. Lis la fiche client et toutes les données fournies avant d'écrire.
2. Choisis les agents à mobiliser. Délègue seulement ce qui peut tourner en parallèle ou demande un contexte isolé ; fais le reste toi-même.
3. Produis le livrable, puis vérifie-le contre les critères de réussite.
</tache>

<contraintes>
- Tu prépares, tu ne publies pas. Toute action visible par un tiers, irréversible ou qui engage de l'argent (publication, envoi, dépense publicitaire, prix, mise en ligne) sort en brouillon marqué [À VALIDER].
- Utilise uniquement les faits présents dans les données. Information absente (horaires, prix, carte, prestations, chiffres) : écris [À COMPLÉTER].
- Toute promesse chiffrée reprend les conditions des CGV : réservations traçables et honorées, budget publicitaire payé par le client, conditions détaillées dans les CGV.
- SMS et e-mails vers des particuliers : uniquement vers des clients existants du commerce, avec mention STOP, ou vers des contacts ayant donné leur consentement.
- Phrases courtes, en français, sans tiret cadratin.
</contraintes>

<format_sortie>
1. Synthèse : 3 lignes maximum.
2. Livrable(s), chacun sous un titre court.
3. Décisions humaines : liste [À VALIDER], avec l'option que tu recommandes pour chacune.
4. Hypothèses et données manquantes.
</format_sortie>

<exemples>
<exemple type="restaurant">
Entrée : bistrot aux Chartrons, 4,1/5, 86 avis, pas de bouton Réserver sur la fiche.
Sortie (extrait) : "Synthèse : les gens qui cherchent un restaurant aux Chartrons le soir vous trouvent, mais ne peuvent pas réserver en un clic. Action 1 [À VALIDER] : activer le bouton Réserver depuis votre logiciel de réservation. Action 2 : demander un avis aux clients des 60 derniers jours."
</exemple>
<exemple type="salon">
Entrée : salon de 2 fauteuils à Caudéran, 4,7/5, 23 avis, créneaux libres le mardi et le mercredi.
Sortie (extrait) : "Synthèse : votre note est bonne, mais il y a trop peu d'avis pour passer devant les salons voisins. Pilote : SMS aux clients inactifs depuis plus de 3 mois (avec STOP) + publicité locale sur les créneaux du mardi et du mercredi. Objectif : 10 réservations traçables, lien dédié."
</exemple>
<exemple type="cas_limite">
Entrée : salon complet 3 semaines à l'avance, pas de logiciel de réservation.
Sortie (extrait) : "Pilote garanti déconseillé : pas de capacité libre et pas de preuve possible. Proposer l'abonnement Essentiel (avis et fiche) sans garantie de volume."
</exemple>
</exemples>

<criteres_reussite>
Avant de rendre, vérifie que :
- chaque chiffre vient des données ou porte la mention [À COMPLÉTER] ;
- aucune action externe n'est présentée comme faite ;
- le livrable débouche sur une action précise (signer, valider, publier) ;
- le ton est celui d'un patron qui parle à un patron, sans blabla ;
- la promesse respecte la définition contractuelle de la "nouvelle réservation".
</criteres_reussite>

Rappel final : brouillons uniquement, faits sourcés, format en 4 blocs.
```

Deux limites. **R-O-T-C-C n'est pas un cadre officiel**, c'est un acronyme de praticiens : sa correspondance avec les guides est une analyse (probable). Et un prompt ne se juge qu'à l'usage. Testez-le sur une vingtaine de cas réels, puisqu'Anthropic indique qu'environ 20 cas représentatifs suffisent pour commencer à évaluer ([Anthropic](https://www.anthropic.com/engineering/built-multi-agent-research-system)).

## Neuf agents, un seul orchestrateur, et l'humain sur tout ce qui sort

Anthropic recommande de partir de la solution la plus simple et de n'ajouter de la complexité que lorsqu'elle est nécessaire ([Anthropic](https://www.anthropic.com/engineering/building-effective-agents)). Votre chaîne de production est séquentielle (stratégie, contenu, visuel, vidéo, publication, analyse), et c'est justement le cas où le multi-agent apporte le moins. L'architecture recommandée (probable) est donc la suivante : le **Stratège orchestre**, les tâches récurrentes passent par des **workflows fixes** (posts hebdomadaires, réponses aux avis, rapport mensuel), une étape **contrôle voix de marque** relit le travail avant vous, et chaque client a **une seule fiche partagée** que tous les agents lisent. La règle des 20 % humains découle d'un principe d'Anthropic : demander une confirmation avant toute action difficile à annuler ou visible par d'autres, comme l'envoi de messages ([Anthropic](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)). Aucune source ne valide empiriquement le ratio 80/20, et les KPI ci-dessous sont des propositions (non vérifié).

| Agent | Rôle et livrables | Outils (minimum) | KPI | Décision humaine |
|---|---|---|---|---|
| Stratège (orchestrateur) | Plan mensuel par client, briefs aux autres agents, proposition de pilote | Notion, Drive, HubSpot, Gamma | Pilotes signés, calendrier tenu | Stratégie, offre et prix proposés |
| Chercheur | Audit de fiche Google, concurrents du quartier, liste de prospects | Pappers, Contract-Factory SIREN, web en lecture seule | Part des affirmations sourcées, durée d'un audit | Vérification par sondage des chiffres montrés au client |
| Développeur | Landing pages, balisage LocalBusiness, liens UTM | Lovable, Vercel (préproduction) | Score PageSpeed, bugs | Mise en production |
| Rédacteur | Posts, réponses aux avis, textes de fiche, e-mails | Fiche client, charte de ton | Taux d'acceptation sans retouche | Publication, validée en lot chaque semaine |
| Designer | Visuels déclinés de la charte, flyers | Canva, Figma | Taux d'acceptation | Visuels montrant des personnes ou des plats réels |
| Monteur | Reels à partir des rushes du client | Canva vidéo, HyperFrames | Rétention, vues | Publication ; étiquetage de tout contenu de synthèse réaliste (AI Act art. 50(4)) |
| Automatisation | Scénarios : planification, relances, rapports | Make, Zapier, Windsor.ai | Heures gagnées, erreurs | Activation de tout scénario qui écrit chez un client ou envoie des messages |
| Service client | Brouillons de réponses, FAQ, prise de rendez-vous | AgentMail ou Gmail en mode brouillon, Google Calendar | Délai de réponse | Envoi des messages sensibles (réclamation, facture, résiliation, avis négatif) |
| Analyste | Compteur de réservations traçables, rapport mensuel | Windsor.ai, Ryze AI, exports de réservation dans Drive | Exactitude, ponctualité | Validation du rapport ; toute décision de budget publicitaire |

En pratique, la charge humaine tient en trois rendez-vous : environ une heure de validation groupée chaque semaine, la validation mensuelle des rapports, et des points bloquants au cas par cas (prix, dépense, mise en ligne, messages sensibles). Si un agent répond directement aux clients des commerçants, il doit annoncer qu'il est une IA. L'obligation de l'article 50(1) de l'AI Act s'applique depuis le **2 août 2026** et n'a pas été reportée ([Goodwin](https://www.goodwinlaw.com/en/insights/publications/2026/08/alerts-technology-dpc-eu-ai-act-transparency-obligations-now-in-force)) (probable : cabinets concordants, Journal officiel non lu). Dans Claude Code, chaque agent devient un fichier `.claude/agents/*.md` avec ses propres outils ; Anthropic conseille de limiter les outils au strict nécessaire (« a read-only researcher should not have Write or Edit ») ([Claude Code](https://code.claude.com/docs/en/sub-agents)). Le forfait Pro (20 $/mois) ou Max (à partir de 100 $/mois) absorbe le surcoût en tokens tant que l'usage reste dans les quotas ([Claude Pricing](https://claude.com/pricing)) (établi pour les prix).

## La stack actuelle couvre la production ; il manque l'encaissement et la preuve

L'inventaire ci-dessous vient des outils réellement exposés dans votre session (établi pour leur présence). Leurs capacités exactes, comme les actions d'écriture de Windsor.ai sur Google Business Profile, restent à confirmer outil par outil (probable).

| Agent | Déjà disponible (connecteurs / skills) | À ajouter |
|---|---|---|
| Stratège | Notion, Drive, Gamma, HubSpot / `marketing:campaign-plan`, `small-business:content-strategy`, `small-business:proposal-builder` | Rien |
| Chercheur | Pappers, Contract-Factory SIREN / `prospection-fiches-google-bordeaux`, `marketing:seo-audit`, `small-business:seo-ai-visibility` | Outil SEO local pour suivre les fiches concurrentes (Localo, BrightLocal) si Windsor ne suffit pas |
| Développeur | Lovable, Vercel, Figma | Rien |
| Rédacteur | Gmail, Notion / `ig-caption-fr`, `cold-email`, `humanizer`, `brand-voice:brand-voice-enforcement` | Rien |
| Designer | Canva, Figma, HTML/CSS to Image / `small-business:canva-creator`, `prospection-flyers-bordeaux` | Rien |
| Monteur | Canva (vidéo), HyperFrames / `hyperframes`, `ig-reel-fr` | HyperFrames `compose` est désactivé depuis Claude Code : passer par Claude.ai ou par le skill local |
| Automatisation | Make, Zapier, Windsor.ai, Airtable / `postiz:postiz`, `small-business:crm-autopilot` | Postiz ou Metricool (publication Instagram, Facebook, TikTok), **Brevo** (e-mail et SMS), **Yousign** |
| Service client | AgentMail, Gmail, Google Calendar, Slack / `small-business:review-reputation`, `small-business:ticket-deflector` | Calendly (connecteur en échec, Google Calendar `suggest_time` en attendant) |
| Analyste | Windsor.ai, Ryze AI, HubSpot / `small-business:growth-pulse`, `marketing:performance-report` | Accès aux réservations (exports TheFork, Zenchef, Planity), demande d'accès à l'API Google Business Profile |

Trois manques bloquent le modèle économique. Le premier est la **facturation récurrente** : le connecteur Stripe est configuré mais ne se connecte pas, alors que le prélèvement SEPA Stripe coûte 0,35 € ([Stripe](https://stripe.com/fr/pricing?dsktp=1)) (établi). Le deuxième est le **comptage des réservations**. Les API de TheFork et de Zenchef sont réservées aux partenaires ou doivent être activées par le restaurant ([Zenchef](https://help.zenchef.com/hc/en-gb/articles/27690768125597-Zenchef-API), [apis.io](https://apis.io/apis/thefork/thefork-reservations-api/)), et rien n'a été trouvé pour Planity. La preuve passera donc par les exports du back-office du client et par vos propres liens traçables (probable). Le troisième est l'**accès officiel à l'API Google Business Profile**, qui reste à quota zéro tant que Google n'a pas approuvé la demande ([Google](https://developers.google.com/my-business/content/prereqs?authuser=1)) (probable). Windsor.ai sert de passerelle en attendant. Brevo (7 € HT/mois pour 5 000 e-mails, environ 45 € les 1 000 SMS en France, [getkanal](https://getkanal.com/fr/blog/brevo-prix), probable) et Yousign (à partir de 9 € HT/mois, [formalive](https://www.formalive.fr/yousign/), probable) se branchent via Make, faute de connecteur natif. Apollo et Clay ont peu d'intérêt pour des TPE bordelaises (non vérifié) et consomment des crédits.

## La garantie tient si elle devient conditionnelle, traçable et prolongeable

**Faisabilité (probable).** Dix réservations en 30 jours restent un objectif bas pour un commerce actif. Seuls deux leviers produisent un effet mesurable dans le mois : la publicité et la réactivation de la clientèle. Optimiser la fiche Google et collecter des avis agit plus lentement. Les seuls repères de coût sont américains : environ **30 $ par lead** pour la restauration sur Google Ads ([Search Engine Land](https://searchengineland.com/google-ads-costs-keep-rising-but-conversion-rates-improved-in-2025-451167)) et environ **51 $** pour la beauté sur Meta ([WordStream](https://www.wordstream.com/blog/facebook-ads-benchmarks-2025)). Comme un lead n'est pas une réservation, comptez de l'ordre de 300 à 600 € de budget publicitaire par pilote (non vérifié pour la France). La réactivation coûte moins cher, mais elle fait revenir d'anciens clients, pas de nouveaux. Elle n'est légale par SMS que vers les clients existants, pour des services analogues et avec un STOP dans chaque message ([CNIL](https://cnil.fr/fr/node/168596)) (établi).

**Mesure (probable).** Les statistiques de la fiche Google sont partielles : un numéro composé à la main n'est pas compté, et les réservations ne remontent que via des partenaires intégrés ([Search Engine Land](https://searchengineland.com/google-business-profile-performance-insights-what-you-need-to-know-436468)). Les désaccords sur l'attribution sont présentés comme la première cause de rupture des contrats à la performance ([Clicksgeek](https://clicksgeek.com/pay-for-performance-marketing/)) (non vérifié, source intéressée). La parade consiste à ne compter que les réservations arrivées par les canaux que vous avez créés, ce qui évite le débat sur la base de référence. En contrepartie, vous sous-comptez les clients qui voient l'annonce puis appellent directement.

**Droit (incertain sur deux points).** Une garantie de résultat est licite entre professionnels. Elle transforme votre obligation de moyens, qui est le régime habituel en référencement ([Legavox](https://www.legavox.fr/blog/procescial-avocat/referencement-naturel-site-internet-obligations-29420.htm)), en **obligation de résultat**. Or un prestataire a déjà été condamné sur une clause de ce type sans pouvoir invoquer le manque de coopération du client ([Le Monde du Droit](https://www.lemondedudroit.fr/decryptages/10634-contrats-informatiques-panorama-de-jurisprudence-2014.html?showall=1)) (probable). Les conditions doivent figurer dans des CGV, que vous êtes tenu de communiquer à tout acheteur professionnel qui les demande ([Légifrance, L441-1](https://www.legifrance.gouv.fr/codes/id/LEGISCTA000038414475/2019-04-26)). Le risque principal tient à l'écart entre l'accroche et le contrat. **« Vous ne payez rien » est faux si le client paie la publicité à Google ou à Meta** : écrivez « vous ne payez pas nos honoraires* ». Les sources divergent sur l'application aux professionnels des règles sur les pratiques trompeuses (L121-5) ([Kohen Avocats](https://kohenavocats.fr/?p=2090527)), et une possible rétractation de 14 jours en cas de démarchage physique d'un très petit commerce (L221-3) n'a pas été vérifiée. Ces deux points sont à faire trancher par un juriste ou par la CCI avant la première prospection en porte-à-porte.

**Effet pervers (non vérifié).** « Vous ne payez rien » attire surtout les commerces en difficulté, là où le résultat est le plus incertain. La coiffure a perdu 2,75 % de chiffre d'affaires moyen en 2024 ([UNEC](https://unec.fr/wp-content/uploads/2026/02/cp-chiffres-cles-2024.pdf)) (probable). Un audit d'éligibilité est indispensable : logiciel de réservation en place, capacité libre, base clients exploitable.

La version défendable : « *10 réservations traçables et honorées en 30 jours. Sinon, pas d'honoraires, et nous continuons gratuitement 30 jours de plus.* Conditions : budget publicitaire minimal payé par vous à la plateforme, accès en lecture à votre logiciel de réservation, code promo saisi par votre équipe, voir CGV. » Cette formulation reprend la garantie conditionnelle et la garantie de service décrites par Hormozi ([SuperSummary](https://www.supersummary.com/100m-offers/section-4-summary/)). Elle prolonge la relation au lieu de la couper, ce qui sert directement l'objectif d'abonnement.

**Pricing (hypothèses).** Le seul marché sourcé est la gestion de fiche Google : **50 € HT/mois** à la CCI des Landes ([CCI Landes](https://www.landes.cci.fr/wp-content/uploads/2025/06/ABONNEMENT-GOOGLE.pdf)) et **60 à 180 € HT** en agence ([Kolonell](https://kolonell.com/fr/blog/gestion-mensuelle-fiches-google-business-profile-reseau-agences-lille-2026)). Les agences de SEO local bordelaises affichent 800 à 2 500 € HT, mais pour une clientèle B2B ([Kolonell](https://kolonell.com/fr/blog/prix-seo-local-b2b-bordeaux-2026)). Il y a donc de la place entre le logiciel en self-service et l'agence. Échelle proposée (non vérifié) : un pilote à 300-500 € HT facturé à J30, un palier Essentiel à 150-250 € HT, un palier Croissance à 350-600 € HT hors budget publicitaire. Le calcul ne tient pas partout. Avec une **fiche moyenne de 43 €** en coiffure ([UNEC](https://unec.fr/wp-content/uploads/2026/02/cp-chiffres-cles-2024.pdf)), 10 réservations rapportent environ 430 € de chiffre d'affaires, soit à peu près le prix du pilote : le salon ne gagne rien le premier mois. Pour la coiffure, il faut un pilote moins cher ou un objectif plus élevé, fixé après l'audit. Le churn des agences sur abonnement tourne autour de 2 à 3 % par mois ([Focus Digital](https://focus-digital.co/average-marketing-agency-churn/)) (incertain : versions contradictoires). Sur des TPE fragiles, prévoyez plutôt 5 à 8 %, et ajoutez un engagement de 3 mois après le pilote ainsi que des points à 30, 60 et 90 jours.

## Recommandation classée et prochaine action

Par ordre d'impact : (1) **rédiger l'annexe de garantie** (définition de la réservation, canaux traçables, obligations du client, exclusions, budget publicitaire à sa charge, aucune reconduction automatique) et la faire relire, car c'est le seul point qui peut vous coûter de l'argent ou un procès ; (2) **corriger l'accroche** en « pas d'honoraires » avec astérisque, et adapter l'objectif en coiffure ; (3) **réparer Stripe** et brancher Yousign via Make pour encaisser les abonnements ; (4) lancer le prompt maître dans un Project Claude et orchestrer les agents à la main pendant un mois avant d'automatiser ; (5) ajouter Brevo et Postiz ou Metricool, puis demander l'accès à l'API Google Business Profile. Le principal inconnu, c'est le taux de conversion d'un pilote garanti en abonnement. Aucune source ne le donne : vos 5 premiers pilotes le fourniront, à condition de mesurer le temps passé par pilote, car un taux d'échec au-delà d'environ 30 % mangerait la marge.

**Prochaine action, cette semaine :** rédiger l'annexe de garantie d'une page à partir de la définition placée dans le prompt maître, l'envoyer pour relecture à la CCI Bordeaux Gironde ou à un avocat en droit des affaires, et pendant ce temps faire tourner le prompt maître sur 3 audits de commerces bordelais réels pour le corriger avant le premier pilote.
