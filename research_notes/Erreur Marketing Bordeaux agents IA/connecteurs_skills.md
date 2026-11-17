# Stack d'outils (connecteurs, API, skills) pour Erreur Marketing Bordeaux — équipe de 9 agents IA

> Note de méthode (à lire par le rédacteur) : pendant cette recherche (17/11/2026), le réseau de la session **bloquait l'accès direct** aux pages officielles (developers.google.com, cnil.fr, make.com, n8n.io, zapier.com, brevo.com : erreur DNS « host not allowed »). Les faits ci-dessous viennent donc de **résultats de recherche web** qui citent souvent les pages officielles (extraits), complétés par des comparatifs tiers. Chaque prix tiré d'un comparatif tiers est à re-vérifier sur la page officielle avant publication ; ceux pour lesquels les sources se contredisent sont marqués « non vérifié ». L'évaluation des connecteurs déjà présents dans Claude repose sur la **liste des outils réellement exposés dans la session** (noms des fonctions MCP et instructions des serveurs), observée directement — pas sur une source web.

---

## 1. Google Business Profile (GBP) : que peut-on automatiser via l'API officielle, conditions d'accès, outils tiers et prix ?

### Takeaway
L'API GBP officielle permet de gérer fiches, avis/réponses, posts et statistiques (Performance API v1), mais l'accès est soumis à une **demande d'approbation** (quota = 0 tant que Google n'a pas validé) et à une structure « Organization account ». Pour un solo, le chemin le plus court est de passer par un intermédiaire déjà approuvé : **Windsor.ai (déjà connecté dans Claude, avec actions d'écriture « posts, reviews, listing edits » sur `google_my_business`)**, ou un outil local SEO (Localo ~39 $/mois, BrightLocal ~41 $/mois — non vérifié).

### Cited Findings
- Prérequis officiels : compte Google, projet Google Cloud (Project ID + numéro), « Organization account » Business Profile, puis demande via le formulaire de contact GBP API en choisissant « Application for Basic API Access » — [developers.google.com/my-business/content/prereqs](https://developers.google.com/my-business/content/prereqs?authuser=1) (extrait via recherche)
- Critères d'éligibilité : « valid business reason », projet Google Cloud valide et URL de site web d'entreprise valide — [developers.google.cn – overview](https://developers.google.cn/my-business/content/overview)
- Le seuil « fiche active depuis 60 jours » circule uniquement dans des guides tiers ; aucune page Google ne le confirme → **non vérifié** — [unified.to](https://unified.to/blog/how_to_set_up_google_business_profile_api_access_and_get_oauth_2_credentials) ; [slashpost.ai](https://slashpost.ai/blogs/google-business-profile/google-business-profile-api-documentation-2026)
- Tant que l'accès n'est pas approuvé : quota 0 QPM, tous les appels échouent ; délai de revue de quelques jours à quelques semaines, approbation non garantie (sources tierces) — [slashpost.ai](https://slashpost.ai/blogs/google-business-profile/google-business-profile-api-documentation-2026) ; [singhamandeep.com](https://singhamandeep.com/?p=1592)
- Statistiques : l'ancien `reportInsights` (v4.9) est remplacé par `locations.fetchMultiDailyMetricsTimeSeries` de la **Business Profile Performance API v1** ; `localPosts.reportInsights` a été supprimé et certaines métriques (ex. LOCAL_POST_VIEWS_SEARCH) ont disparu — [Google – sunset dates](https://developers.google.com/my-business/content/sunset-dates) ; [Performance API change log](https://developers.google.com/my-business/content/performance/change-log) ; [localsearchforum](https://localsearchforum.com/threads/api-endpoint-update-from-google.59655/post-184099)
- Avis & réponses et posts (localPosts) : toujours décrits comme opérationnels sur les endpoints v4 par des guides tiers ; notes de version 2025 mentionnant l'accès aux médias des avis et au statut de réponse. Statut 2026 non confirmé sur une page officielle accessible → **à vérifier** — [upload-post.com](https://www.upload-post.com/google-business-profile-api/) ; [postproxy.dev](https://postproxy.dev/blog/google-business-profile-api-full-suite/)
- L'API Q&A aurait été fermée le 3 novembre 2025 (source tierce unique) — [slashpost.ai](https://slashpost.ai/blogs/google-business-profile/google-business-profile-api-documentation-2026)
- Localo : Single Business 39 $/mois (mensuel), Pro 149 $/mois, Enterprise sur devis (relevé du 9/11/2026) ; G2 affiche un départ à 69 $ (avril 2026) → contradiction — [dupple.com](https://dupple.com/learn/best-local-seo-tools) ; [G2 Localo](https://www.g2.com/products/localo/pricing)
- Localo propose génération IA de Google Posts et gestion des avis — [dupple.com](https://dupple.com/learn/best-local-seo-tools)
- BrightLocal : Track 41 $/mois, Grow 65 $/mois (nov. 2026), ailleurs « 29 $ » ou « sur demande » → **non vérifié** ; la gestion GBP (sync fiches, posts planifiés) est dans le palier « Manage » ; outils Local Rank Tracker, Local Search Grid, Citation Tracker — [dupple.com](https://dupple.com/learn/best-local-seo-tools) ; [toolradar BrightLocal](https://toolradar.com/tools/brightlocal) ; [toolradar comparatif](https://toolradar.com/compare/brightlocal-vs-localo)
- Windsor.ai (connecteur MCP présent) : le serveur déclare couvrir `google_my_business` en lecture et des actions d'écriture « posts, reviews, and listing edits on business listings » ; chaque écriture nécessite une confirmation utilisateur — observé dans les instructions du serveur MCP Windsor.ai de la session (pas d'URL)

### Inferences
- Pour démarrer vite, l'agent **automatisation/service client** peut répondre aux avis et publier des posts GBP via Windsor.ai (à valider avec `list_actions` sur `google_my_business`) sans attendre l'approbation Google. En parallèle, déposer une demande d'accès API officielle (gratuite) pour réduire la dépendance.
- La Performance API v1 fournit les KPI clés à rapporter aux clients (appels, itinéraires, clics site, vues) : c'est le cœur du reporting de l'abonnement « visibilité ».
- Partoo et Semrush Local : pas de prix trouvés ; Partoo vise plutôt les réseaux multi-établissements (inférence, non sourcée), donc probablement surdimensionné pour des restaurants indépendants.

### Gaps
- Prix Partoo et Semrush Local 2026 : aucune source trouvée.
- Liste exacte des métriques Performance API v1 et confirmation officielle 2026 des endpoints avis/posts : page Google inaccessible depuis la session.
- Exigence « 60 jours » : non confirmée officiellement.

---

## 2. Plateformes de réservation (restaurants / salons) : API ou rapports pour compter les réservations ? « Réserver avec Google » ?

### Takeaway
Aucune des plateformes n'offre à un consultant un accès API « libre » : TheFork et Zenchef ont des API **réservées aux partenaires approuvés** (ou activées par le restaurant), et rien n'a été trouvé pour Planity. Le comptage fiable des réservations passera donc surtout par **les exports/rapports du back-office du client** (accès délégué) et par les **métriques GBP** (clics « Réserver », itinéraires, appels).

### Cited Findings
- Zenchef dispose d'une API permettant aux restaurants de connecter leurs données à des outils tiers non encore partenaires ; partenariat officiel via la page intégrations ; Zenchef surveille les appels et peut couper une intégration unilatéralement — [help.zenchef.com – Zenchef API](https://help.zenchef.com/hc/en-gb/articles/27690768125597-Zenchef-API)
- TheFork : API B2B (TheFork Manager) avec réservations, clients, commandes, avis ; identifiants délivrés seulement après approbation d'un partenariat (demande par e-mail à integrations@thefork.com selon une source tierce) ; authentification « client credentials » sans délégation par restaurant — [apis.io TheFork](https://apis.io/apis/thefork/thefork-reservations-api/) ; [ainora.lt audit 2026](https://ainora.lt/blog/restaurant-booking-api-for-ai-agents-2026) ; [apitracker.io](https://apitracker.io/a/thefork)
- Lightspeed (caisse) s'intègre à Zenchef, TheFork, OpenTable ; les réservations Zenchef remontent automatiquement dans Lightspeed — [lightspeedhq.com intégrations](https://www.lightspeedhq.com/fr/pos/restaurant/integrations/) ; [Lightspeed x Zenchef](https://www.lightspeedhq.com/fr/partenaires/zenchef/)
- Treatwell figure dans la liste officielle des partenaires « Réserver avec Google » — [google.com/maps/reserve/partners](https://www.google.com/maps/reserve/partners)
- Booksy propose « Réserver avec Google » depuis la fiche GBP, avec synchro agenda (selon formules) ; chiffres « +20 % de réservations » et « −25 % d'absences » = marketing éditeur, **non vérifiés** — [blog Booksy](https://biz.booksy.com/fr-fr/blog/comment-google-reserve-va-vous-apporter-plus-de-clients) ; [Booksy témoignages](https://biz.booksy.com/fr-fr/blog/temoignages-jai-de-nouveaux-clients-grace-a-google-reserve)
- Côté Google, « Réserver avec Google » repose sur une intégration serveur de réservation implémentée par le **fournisseur** (pas par le commerçant), avec inventaire temps réel et UpdateBooking — [Google Actions Center](https://developers.google.com/actions-center/verticals/reservations/e2e/integration-steps/booking-server-ready?hl=fr) ; [politiques plate-forme](https://developers.google.com/actions-center/verticals/appointments/redirect/policies/platform-policies?hl=fr)
- Square note des restrictions sectorielles côté Google (cours, frais de no-show non compatibles) — [Square aide](https://squareup.com/help/fr/fr/article/6567-reserve-with-google)

### Inferences
- Méthode de mesure recommandée pour l'agent **analyste** : (1) métriques GBP (clics réservation/site/appels/itinéraires via Performance API ou Windsor.ai), (2) export mensuel CSV du back-office TheFork/Zenchef/Planity/Treatwell fourni par le client (ou accès lecteur), déposé dans Google Drive et lu par l'agent, (3) liens UTM sur le bouton « Réserver » du site/Instagram.
- Ne pas promettre contractuellement un « nombre de réservations » mesuré automatiquement : dépendance aux accès client.
- Vérifier pour chaque client que son outil de réservation est bien partenaire « Réserver avec Google » (gain rapide à vendre dans l'audit).

### Gaps
- Planity : aucune documentation API ni confirmation de partenariat « Réserver avec Google » trouvée.
- Guestonline : non couvert par la recherche.
- Contenu exact des exports/rapports disponibles dans chaque back-office : non trouvé.

---

## 3. Social & contenu : Meta Graph API, TikTok, outils de planification, Canva, vidéo

### Takeaway
Instagram autorise la publication via API pour les comptes professionnels (posts, carrousels, reels) avec un plafond quotidien (100 posts/24 h selon la page actuelle de Meta, 50 selon d'anciennes pages) ; TikTok impose un **audit** avant toute publication publique. Pour un solo, un planificateur (Postiz auto-hébergé/hébergé, Buffer, Metricool) évite de gérer ces API soi-même. Le skill `postiz:postiz` est déjà installé.

### Cited Findings
- Instagram : limite de 100 posts publiés via API par période glissante de 24 h, un carrousel compte pour un post (page actuelle) ; d'anciennes pages et l'endpoint de quota indiquent 50 ; certains tiers citent 25 → vérifier via `GET /{ig-user-id}/content_publishing_limit` — [Meta – Content Publishing](https://developers.facebook.com/docs/instagram-platform/content-publishing/) ; [Meta – content_publishing_limit](https://developers.facebook.com/documentation/instagram-platform/instagram-graph-api/reference/ig-user/content_publishing_limit.md) ; [ayrshare](https://www.ayrshare.com/?p=16475)
- Depuis le 1/07/2023, toute vidéo simple publiée via l'API est publiée en reel ; les conteneurs expirent après 24 h — [Meta – Content Publishing](https://developers.facebook.com/docs/instagram-platform/content-publishing/)
- TikTok Content Posting API : apps non auditées limitées à la visibilité SELF_ONLY (privée) et ~5 utilisateurs/jour ; audit exigeant (maquettes UX, sélecteur de confidentialité, mention contenu commercial), 2 à 4 semaines (sources tierces, non confirmées officiellement) — [bundle.social / guide API](https://website-apn.pages.dev/blog/instagram-reels-vs-tiktok-vs-youtube-shorts-publishing-via-api/) ; [postproxy.dev](https://postproxy.dev/blog/social-media-api-for-publishing-developer-guide/)
- Metricool : tarification par « marque » ; gratuit, Starter dès 22 $/mois, Advanced dès 54 $/mois (un guide cite Starter dès 16 €/mois en annuel) ; X payant en plus → **non vérifié** — [socialk.it Metricool](https://socialk.it/en/pricing/metricool) ; [Buffer vs Metricool](https://buffer.com/resources/buffer-vs-metricool/)
- Postiz : open source AGPL-3.0, auto-hébergeable ; offres hébergées dès 29 $/mois (source tierce) — [postfa.st](https://postfa.st/blog/best-social-media-schedulers)
- Buffer : par canal ; gratuit puis Essentials 6 $/canal, Team 12 $/canal — [costbench](https://costbench.com/compare/buffer-vs-metricool/) ; [postfa.st](https://postfa.st/blog/metricool-vs-buffer-vs-postfast-2025-pricing-and-features)
- Metricool documente ses propres limites quotidiennes de publication par réseau — [help.metricool.com](https://help.metricool.com/de/daily-posting-limits-on-social-media-sh58j)
- Connecteurs observés dans la session : Canva (create-design, generate-design, create-video, brand templates, export, resize), HyperFrames by HeyGen (vidéos HTML programmables ; `compose`/`render_video` **désactivés depuis un client CLI** comme Claude Code, disponibles depuis Claude.ai web/desktop), HTML/CSS to Image (images et enregistrements vidéo/GIF à partir de HTML), HubSpot (`manage_social_posts`, `get_social_post_analytics`) — observé dans la session (pas d'URL)

### Inferences
- Planification : pour 10-30 clients × 2 réseaux, Metricool (par marque) ou Postiz auto-hébergé (coût serveur seulement) sont plus adaptés que Buffer (par canal). Postiz a l'avantage d'un skill Claude déjà installé.
- Le modèle « agence » implique que chaque client connecte son compte Instagram pro/Facebook à l'outil de planification (OAuth) : à intégrer à l'onboarding.
- Vidéo : Canva `create-video` + HyperFrames pour reels/templates ; CapCut n'a pas d'API publique connue (non sourcé) → montage manuel ou via templates Canva.
- TikTok : passer par un planificateur déjà audité plutôt que développer sa propre intégration.

### Gaps
- Prix officiels Canva Pro/Teams 2026, HeyGen, CapCut Pro : non recherchés faute de budget (à vérifier).
- Prix Postiz hébergé sur page officielle : non vérifié.

---

## 4. Publicité : API/connecteurs Google Ads et Meta Ads ; agrégateurs de reporting

### Takeaway
Deux connecteurs déjà présents couvrent l'essentiel : **Ryze AI** (lecture + écriture Meta Ads, Google Ads, LinkedIn Ads, SEO/GEO, Meta Ad Library) pour piloter les campagnes, et **Windsor.ai** (350+ sources, lecture + écriture, Basic ~19-23 $/mois pour 3 sources, Standard ~99-118 $/mois pour 7 sources — non vérifié) pour le reporting multi-clients vers Looker Studio/Sheets.

### Cited Findings
- Windsor.ai : Basic 19 $ (annuel) / 23 $ (mensuel) pour 3 sources ; Standard 99 $ (7 sources) ou 118 $/mois (mensuel) ; prix aussi fonction des « monthly active rows » ; tous connecteurs et destinations inclus ; essai 14 jours — [coefficient.io](https://coefficient.io/windsor-ai-pricing) ; [PricingSaaS](https://pricingsaas.com/companies/windsor) ; [blog.coupler.io](https://blog.coupler.io/windsor-ai-pricing-overview/amp/) (Coupler est concurrent)
- Le serveur Windsor.ai déclare couvrir Meta Ads, Google Ads, TikTok Ads, Instagram/Facebook organiques, Google My Business, Search Console, GA4, HubSpot, Stripe, PayPal, Google Sheets, BigQuery, avec actions d'écriture (budgets, campagnes, posts, avis) — observé dans les instructions du serveur MCP (pas d'URL)
- Ryze AI expose dans la session des outils `meta_ads__*` (insights, créas, lead forms, Graph read/write), `linkedin_ads__*`, `native__search_ad_library`, connexions Google Ads/SEO via `native__create_connection_link` ; certaines fonctions renvoient « subscription_required » (abonnement payant) — observé dans la session (pas d'URL)

### Inferences
- Agent **analyste** : Windsor.ai → Looker Studio (gratuit) ou Google Sheets pour un tableau de bord mensuel par client ; le palier dépend du nombre de **sources**, donc vérifier si un compte multi-clients d'une même source (ex. plusieurs fiches GBP) compte pour une seule source (non vérifié).
- Agent **stratège/automatisation (ads)** : Ryze AI pour créer/ajuster des campagnes locales Meta/Google ; Windsor.ai en lecture pour éviter les doublons de coût.
- Budget pub des restaurants/salons généralement faible : les ads seront plutôt une option premium.

### Gaps
- Tarif Ryze AI : non trouvé.
- Conditions d'accès Google Ads API (developer token) et Meta Marketing API : non recherchées (contournées via connecteurs).

---

## 5. Automatisation, CRM, e-mail/SMS, facturation/abonnements, signature électronique

### Takeaway
Pour un solo : **Make** (Core ~9-12 $/mois pour ~10 000 crédits — non vérifié, possible refonte tarifaire 2026) ou **n8n** (Starter ~20-24 €/mois pour 2 500 exécutions, ou auto-hébergé gratuit) sont nettement moins chers que **Zapier** (Professional ~19,99 $/mois pour 750 tâches). Make et Zapier sont déjà connectés à Claude. Brevo (français) : Starter 7 € HT/mois pour 5 000 e-mails, SMS France ~45 €/1 000. Stripe : SEPA 0,35 €/prélèvement (page officielle) ; GoCardless 1 % + 0,20 € plafonné (2 € ou 4 € selon sources). Yousign (renommé Youtrust) : application dès 9 € HT/mois, API Plus 104 €/mois HT.

### Cited Findings
- Make Core : prix rapportés de ~9 $/mois (annuel) à 10,59 $, 12 $ ou 16 $ (mensuel) ; 10 000 crédits/mois ; Free = 1 000 crédits ; Core = scénarios actifs illimités + API Make — [latenode](https://latenode.com/blog/make-com-pricing) ; [jetadmin](https://www.jetadmin.io/blog/make-pricing/) ; [zapier blog](https://zapier.com/blog/make-com-pricing/) ; [lindy](https://www.lindy.ai/blog/make-com-pricing)
- Possible passage de Make à un plan unique (9 $/mois annuel, 5 000 crédits) en juin 2026 → **non vérifié**, contredit par d'autres sources — [usagepricing.com](https://usagepricing.com/blueprint/activity/make-2026-08-11-single-make-plan-confirmed)
- n8n Starter : ~20 $/mois (annuel) / 24 € ou 24 $ (mensuel) pour 2 500 exécutions ; facturation par exécution de workflow entier (vs Zapier par étape) — [dupple n8n](https://dupple.com/learn/n8n-pricing) ; [toolradar n8n](https://toolradar.com/blog/n8n-pricing-2026) ; [dupple zapier vs n8n](https://dupple.com/learn/zapier-vs-n8n)
- Zapier : Free 100 tâches/mois, Professional 19,99 $/mois (annuel) ~750 tâches, Team 103,50 $/mois — [toolradar Zapier](https://toolradar.com/blog/zapier-pricing-2026) ; [lowcode.agency](https://www.lowcode.agency/blog/zapier-pricing-plans)
- Brevo : Starter 7 € HT/mois pour 5 000 e-mails (−10 % en annuel) ; Standard 15 €, Pro 499 €, Entreprise sur devis ; SMS France 45 €/1 000 (4,5 crédits/SMS) ; WhatsApp sur Pro/Entreprise uniquement (guide daté 24/10/2026) — [getkanal.com](https://getkanal.com/fr/blog/brevo-prix) ; Business ~18 $/mois (source en dollars, non vérifié) — [tajo.io](https://tajo.io/blog/brevo-pricing-guide)
- Stripe : prélèvement SEPA 0,35 € (page tarifaire officielle) — [stripe.com/fr/pricing](https://stripe.com/fr/pricing?dsktp=1)
- Stripe Billing : 0,7 % du volume facturé (sources tierces, non affiché sur la page consultée) → **non vérifié** — [kolonell.com](https://kolonell.com/fr/blog/facturation-paiement-recurrent-saas-b2b-stripe-gocardless-2026)
- GoCardless : 1 % + 0,20 €, plafond 2 € (hackceleration) ou 4 € (kolonell) en France → **non vérifié** ; intégration GoCardless ↔ Stripe disponible — [hackceleration](https://hackceleration.com/fr/labs/changer/gocardless) ; [kolonell](https://kolonell.com/fr/blog/gocardless-stripe-prelevement-sepa-abonnements-b2b-nantes-2026) ; [gocardless.com](https://gocardless.com/fr-fr/g/gocardless-stripe)
- Yousign : application dès 9 € HT/mois, essai 14 jours ; API Plus dès 104 €/mois HT, API Pro dès 129 €/mois HT (facturation annuelle) ; renommage en Youtrust annoncé nov. 2025, migration jusqu'en 2027, tarifs inchangés selon Formalive — [verdocs](https://verdocs.com/?p=13994) ; [formalive.fr](https://www.formalive.fr/yousign/) ; [tool-advisor.fr](https://tool-advisor.fr/signature-electronique/comparatif/yousign/)
- Connecteurs observés : HubSpot (CRM objets, segments, campagnes, social, landing pages, AEO), Airtable (bases, interfaces, formulaires, automatisations), Notion (pages, bases, calendrier), PayPal (factures, liens de paiement, transactions), AgentMail (boîtes mail propres aux agents), Slack, Gmail, Google Calendar (dont `suggest_time`), Google Drive — observé dans la session

### Inferences
- Choix recommandé solo : **Make** (connecteur Claude déjà actif, interface visuelle, coût bas) pour les flux principaux ; n8n auto-hébergé si volume élevé ; Zapier en appoint pour une app non couverte (connecteur déjà présent, 9 000+ apps).
- Facturation : abonnements mensuels à faible ticket (ex. 100-300 €) → Stripe SEPA (0,35 €/prélèvement) est très compétitif ; GoCardless n'a d'intérêt qu'au-delà (inférence à partir des grilles). Stripe ne se connecte pas actuellement dans Claude → à réparer ; PayPal (connecté) en secours pour factures ponctuelles mais peu adapté au prélèvement SEPA récurrent.
- CRM : HubSpot (connecté, version gratuite) ou Airtable ; éviter de multiplier — un seul « système de vérité » (HubSpot recommandé pour pipeline + e-mails, Airtable pour la base de livrables/calendrier éditorial).
- E-signature : Yousign app à 9 €/mois suffit (volume faible) ; l'API (104 €/mois) n'est pas justifiée au début. Pas de connecteur Yousign dans Claude → passer par Make/Zapier.
- Brevo (français, RGPD-friendly) est le chaînon manquant pour e-mail marketing/SMS ; non présent dans les connecteurs Claude (Klaviyo/Mailchimp configurés mais en échec) → via Make/Zapier.

### Gaps
- Prix officiels HubSpot Free/Starter, Airtable, Notion 2026 : non recherchés.
- Obligations de facturation électronique (réforme française 2026-2027) et outil conforme (PDP) : non recherchées — à traiter (impact sur le choix Stripe/PayPal pour l'émission de factures).
- Pages officielles Make/n8n/Zapier/Brevo inaccessibles depuis la session.

---

## 6. Données de prospection en France et cadre légal (Pappers, SIRENE, scraping Google Maps, RGPD/CNIL)

### Takeaway
En B2B, l'e-mail de prospection vers une adresse professionnelle est possible **sans consentement préalable** si le message est en rapport avec la profession du destinataire, avec information et opt-out simple ; la reconstitution d'adresses pro est encadrée par la CNIL (intérêt légitime réel). Le téléphone B2B reste a priori sous RGPD/intérêt légitime, mais la loi n° 2025-594 (opt-in téléphonique en vigueur depuis le 11/08/2026) fait l'objet de lectures divergentes pour le B2B ; le **SMS** de prospection est par défaut soumis à l'opt-in (L34-5 CPCE) — prudence. Pappers et Contract-Factory SIREN sont déjà connectés pour l'enrichissement légal.

### Cited Findings
- B2B e-mail : régime d'opt-out ; adresse générique → simple opposition ; adresse nominative → opposition si l'objet est professionnel ; information + désinscription toujours obligatoires ; base légale usuelle = intérêt légitime (considérant 47) — [CNIL – communications électroniques](https://www.cnil.fr/fr/communication-electronique-quelles-regles) ; [legiscope](https://www.legiscope.com/blog/rgpd-marketing-direct-prospection.html) ; [kohenavocats](https://kohenavocats.fr/?p=2153986)
- B2C : opt-in préalable, exception « soft opt-in » pour clients existants — [CNIL – communications électroniques](https://www.cnil.fr/fr/communication-electronique-quelles-regles)
- Reconstitution d'adresses pro (prenom.nom@) : admise seulement avec un intérêt légitime réel à contacter la personne ; « ni automatique ni systématique » ; n'exonère pas des obligations d'information et d'opposition (publication CNIL d'octobre 2026 selon presse) — [CNIL – reconstitution d'adresses](https://www.cnil.fr/fr/reconstitution-adresses-professionnelles-quel-cadre) ; [siecledigital](https://siecledigital.fr/2026/10/20/peut-on-deviner-ladresse-e-mail-professionnelle-dun-prospect-pour-le-contacter-la-cnil-clarifie-les-regles/) ; [leptidigital](https://www.leptidigital.fr/growth-hacking/appels-a-froid-e-mails-pro-devines-cnil-encadre-deux-pratiques-courantes-prospection-commerciale-92263/)
- Loi n° 2025-594 du 30/06/2025 : remplace Bloctel par un opt-in pour le démarchage téléphonique, effectif au 11/08/2026 ; Bloctel cesse à cette date — [CMS](https://cms.law/fr/fra/legal-updates/prospection-commerciale-et-rgpd-vers-un-durcissement-du-cadre-juridique) ; [economie.gouv.fr Bloctel pros](https://www.economie.gouv.fr/entreprises/bloctel-professionnels-reglementation)
- B2B téléphone : non soumis au consentement de l'art. L223-1 selon donneespersonnelles.fr, mais un autre guide estime que la loi s'applique aussi au B2B → **contradiction** — [donneespersonnelles.fr](https://donneespersonnelles.fr/demarchage-telephonique) ; [swim.legal](https://www.swim.legal/blog/demarchage-telephonique-2026-loi)
- Règles CNIL téléphone (hors automate) — [CNIL – prospection téléphonique](https://cnil.fr/fr/prospection-commerciale-par-telephone-hors-automate-dappel-quelles-sont-les-regles)
- SMS/e-mail : opt-in de principe (art. L34-5 CPCE) selon CMS ; traitement clair du SMS B2B non trouvé — [CMS](https://cms.law/fr/fra/legal-updates/prospection-commerciale-et-rgpd-vers-un-durcissement-du-cadre-juridique)
- Connecteurs présents : Pappers France (recherche entreprises, dirigeants, comptes, bénéficiaires, `sirenisateur`, `recherche-lieux`) ; Contract-Factory SIREN (données RNE/INPI publiques : search_company, get_company, get_etablissements, dirigeants) ; Apollo.io (recherche/enrichissement, séquences e-mail, crédits) ; Clay (recherche/enrichissement) — observé dans la session

### Inferences
- Workflow **chercheur** conforme : source primaire = SIRENE/RNE (codes NAF 56.10A restauration traditionnelle, 96.02A coiffure — codes cités de mémoire, à vérifier) via Pappers/Contract-Factory, filtrés sur Bordeaux Métropole ; enrichissement avec la fiche GBP (note, nb d'avis, photos) pour personnaliser l'audit. Apollo/Clay sont peu pertinents pour des TPE locales (bases orientées entreprises tech/US — inférence) et consomment des crédits.
- Scraping Google Maps : les CGU Google l'interdisent (non sourcé ici) et les données collectées restent des données personnelles quand elles identifient un gérant ; privilégier la consultation manuelle/semi-automatique et l'API Places officielle (non recherchée).
- Canal recommandé : e-mail à l'adresse publique du commerce (souvent générique) avec objet lié à leur activité + opt-out, visite physique / flyer (skills existants), appel téléphonique seulement après vérification juridique de la loi 2025-594 pour le B2B. **Éviter le SMS à froid.**
- Tenir un registre des traitements et une liste d'opposition (dans HubSpot/Airtable).

### Gaps
- API Recherche d'entreprises (annuaire-entreprises.data.gouv.fr) : gratuité/limites non confirmées par une source trouvée.
- Prix API Pappers : non trouvé.
- Position CNIL explicite sur le SMS B2B et sur le scraping Google Maps : non trouvée (cnil.fr inaccessible directement).

---

## 7. Évaluation des connecteurs et skills déjà disponibles : pertinence par agent, par workflow, et manques

### Takeaway
La stack existante couvre déjà ~80 % des besoins : prospection (Pappers, Contract-Factory, skills prospection Bordeaux), production de contenu (Canva, HyperFrames, skills IG FR, Postiz), reporting (Windsor.ai, growth-pulse, performance-report), ads (Ryze AI), CRM (HubSpot/Airtable/Notion), automatisation (Make/Zapier). **Manques critiques** : facturation récurrente SEPA (Stripe ne se connecte pas), e-mail/SMS marketing français (Brevo), signature électronique (Yousign), accès aux plateformes de réservation, prise de RDV (Calendly en échec), publication Instagram/TikTok directe (à faire via Postiz/Windsor).

### Cited Findings
- Capacités observées des connecteurs (noms d'outils MCP de la session, pas d'URL) :
  - Windsor.ai : lecture 350+ sources + écriture (GBP posts/avis, social posts/commentaires, ads) avec confirmation.
  - Ryze AI : Meta Ads, Google Ads, LinkedIn Ads, SEO/GEO, Ad Library ; certaines fonctions payantes.
  - HubSpot : CRM, segments, campagnes, social posts + analytics, landing pages, blog, AEO.
  - Canva : création/édition/redimensionnement/export, brand templates, génération vidéo.
  - HyperFrames (HeyGen) : `compose`/`render_video` désactivés depuis un client CLI (Claude Code) — utilisables depuis Claude.ai web/desktop ; sinon skill local `anthropic-skills:hyperframes`.
  - Gamma : présentations/docs (propositions, rapports).
  - Lovable / Vercel : création et déploiement de sites/landing pages ; Vercel expose analytics de pages vues.
  - AgentMail : boîtes e-mail dédiées aux agents (utile pour service client/inbound).
  - Apollo.io : séquences e-mail, enrichissement, crédits consommés.
  - PayPal : factures, liens de paiement, litiges.
  - Pappers / Contract-Factory SIREN : données légales d'entreprises françaises.
- Connecteurs configurés mais en échec : Stripe, Square, Calendly, Klaviyo, Mailchimp, Wix, Shopify, Zoho CRM, Trello (énoncé de la mission).

### Inferences

**Mapping par agent (connecteurs → skills)**

| Agent | Connecteurs pertinents | Skills pertinents | Manques |
|---|---|---|---|
| Stratège | Notion, Google Drive, Gamma, HubSpot | marketing:campaign-plan, small-business:content-strategy, marketing:competitive-brief, small-business:proposal-builder | — |
| Chercheur | Pappers France, Contract-Factory SIREN, (Clay, Apollo : faible pertinence TPE locales), Airtable | anthropic-skills:prospection-fiches-google-bordeaux, small-business:lead-finder, vpai:vibe-prospecting, apollo:prospect, marketing:seo-audit, small-business:seo-ai-visibility | Données GBP concurrentes en masse (API Places / outil local SEO type Localo) |
| Développeur | Lovable, Vercel, Figma, Make (webhooks) | anthropic-skills:skill-creator | Hébergement/maintenance de sites clients si Wix (connecteur en échec) |
| Rédacteur | Notion, Google Drive, Gmail | anthropic-skills:ig-caption-fr, anthropic-skills:cold-email, small-business:outreach-composer, marketing:email-sequence, anthropic-skills:humanizer, brand-voice:brand-voice-enforcement | — |
| Designer | Canva, Figma, HTML/CSS to Image, Gamma | small-business:canva-creator, image-generation:image-generation, anthropic-skills:prospection-flyers-bordeaux | — |
| Monteur vidéo | HyperFrames by HeyGen, Canva (create-video), HTML/CSS to Image (recordings) | anthropic-skills:hyperframes, anthropic-skills:ig-reel-fr, anthropic-skills:ig-viral-fr | Outil d'avatar/sous-titres (HeyGen complet, CapCut) non connecté |
| Automatisation | Make, Zapier, Windsor.ai (écriture), Airtable automations, Slack | postiz:postiz, small-business:social-content-engine, small-business:crm-autopilot, small-business:speed-to-lead | Postiz (connecteur absent, skill seul), Brevo, Yousign, Stripe |
| Service client | AgentMail, Gmail, Slack, Windsor.ai (réponses avis GBP), Google Calendar | small-business:review-reputation, small-business:ticket-deflector, small-business:reactivate | Calendly (en échec → Google Calendar `suggest_time`), WhatsApp Business |
| Analyste | Windsor.ai, Ryze AI, HubSpot analytics, Vercel analytics, Google Drive (exports réservation) | small-business:growth-pulse, marketing:performance-report, small-business:ad-manager | Accès réservations (TheFork/Zenchef/Planity), Looker Studio (pas de connecteur, mais Windsor → Sheets/Looker) |

**Mapping par workflow**
- Prospection : Pappers/Contract-Factory → Airtable/HubSpot → skills prospection-fiches-google-bordeaux, prospection-flyers-bordeaux, cold-email, outreach-composer → envoi Gmail (volume faible) ou Brevo (à ajouter) ; respecter les règles CNIL (section 6).
- Audit : marketing:seo-audit, small-business:seo-ai-visibility, review-reputation, competitive-brief → livrable Gamma ou Canva ; données GBP via Windsor.ai.
- Delivery : content-strategy → ig-caption-fr / ig-reel-fr / canva-creator / hyperframes → humanizer + brand-voice-enforcement → planification postiz (ou Metricool) ; posts/avis GBP via Windsor.ai ; ads via Ryze AI.
- Reporting : Windsor.ai (GBP, Instagram, Meta Ads, GA4, Search Console) → growth-pulse / performance-report → PDF Gamma/Canva envoyé par Gmail.
- Facturation : **Stripe (à réparer)** pour abonnements SEPA ; PayPal en secours ; proposal-builder pour devis ; e-signature Yousign via Make (à ajouter).
- Support : AgentMail (boîte support@), ticket-deflector, Slack pour alertes internes, Google Calendar pour RDV.

**Skills peu ou pas pertinents** : apollo:prospect et Clay (bases peu fournies en TPE bordelaises — inférence), small-business:speed-to-lead (utile seulement si leads inbound).

**Priorités d'ajout** : (1) réparer Stripe ; (2) Brevo via Make ; (3) Yousign via Make ; (4) Postiz ou Metricool pour publication IG/FB/TikTok ; (5) demande d'accès officielle API GBP ; (6) outil local SEO (Localo) si Windsor.ai ne couvre pas suffisamment GBP.

### Gaps
- Contenu réel des skills (non inspectable) : la pertinence est jugée sur les noms.
- Couverture exacte des actions d'écriture Windsor.ai pour `google_my_business` et `instagram_public` : à vérifier avec `list_actions` (non appelé, conformément à la consigne).
- Tarifs des abonnements Windsor.ai/Ryze AI/HeyGen/Canva déjà souscrits par l'utilisateur : inconnus.
