# Prompt engineering et architecture d'équipe multi-agents IA pour Erreur Marketing Bordeaux

> Notes de recherche, 17/11/2026. Limites d'accès : dans cette session, `platform.openai.com` et `ai.google.dev` étaient bloqués au niveau réseau (échec DNS). Les recommandations d'OpenAI et de Google viennent donc des extraits de recherche web, qui reprennent les pages officielles, et non d'une lecture complète de ces pages. Elles sont signalées comme telles. Les pages Anthropic (anthropic.com, platform.claude.com, code.claude.com, claude.com/pricing) ont été lues en entier.

## 1. Ce que recommandent les guides officiels (Anthropic, OpenAI, Google) et comment R-O-T-C-C s'y rattache

### Takeaway
Les trois éditeurs convergent sur le même socle : un rôle ou une persona dans le prompt système, des instructions claires, du contexte expliqué (le « pourquoi »), des contraintes, quelques exemples variés, un format de sortie explicite et des balises (XML ou Markdown) pour séparer les blocs. Le cadre R-O-T-C-C couvre bien Rôle, Contexte et Contraintes. Il lui manque trois choses de manière explicite : le format de sortie, les exemples, et les critères de réussite avec leur moyen de vérification. Il faut les ajouter pour obtenir un « R-O-T-C-C + F-E-C » : Format, Exemples, Critères.

### Cited Findings
**Anthropic (Claude), sources primaires lues en entier**
- Avant de travailler un prompt, Anthropic demande trois prérequis : « A clear definition of the success criteria for your use case », un moyen de tester empiriquement le prompt contre ces critères, et un premier brouillon — [Anthropic, Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)
- Le même guide précise que tous les problèmes ne se règlent pas par le prompt. La latence et le coût, par exemple, s'améliorent parfois plus facilement en changeant de modèle — [Anthropic, Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)
- « Think of Claude as a brilliant but new employee who lacks context on your norms and workflows. » Le test proposé : montrer le prompt à un collègue qui ne connaît pas la tâche. S'il est perdu, Claude le sera aussi — [Anthropic, Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- Expliquer pourquoi une instruction existe (son contexte ou sa motivation) améliore les réponses — [Anthropic, Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- Les exemples (few-shot) sont « one of the most reliable ways to steer Claude's output format, tone, and structure ». Ils doivent être pertinents, variés (cas limites compris) et placés dans des balises `<example>` ou `<examples>` — [Anthropic, Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- Des balises XML comme `<instructions>`, `<context>` ou `<input>` réduisent les erreurs d'interprétation quand un prompt mélange instructions, contexte, exemples et données variables — [Anthropic, Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- Un rôle défini dans le prompt système cadre le comportement et le ton, et « even a single sentence makes a difference » — [Anthropic, Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- Sur un contexte long, il faut placer les documents en haut du prompt, au-dessus de la question, des instructions et des exemples, et entourer chaque document de balises `<document>` avec `<source>` — [Anthropic, Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- Pour le format de sortie, Anthropic conseille de dire ce qu'il faut faire plutôt que ce qu'il ne faut pas faire. Au lieu de « Do not use markdown », écrire « Your response should be composed of smoothly flowing prose paragraphs ». Le style du prompt doit aussi ressembler au style attendu en sortie — [Anthropic, Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- Des instructions générales donnent souvent un meilleur raisonnement qu'un plan détaillé étape par étape écrit à la main — [Anthropic, Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- Contre les hallucinations, Anthropic propose un bloc de prompt `<investigate_before_answering>` : lire la source avant de répondre et ne jamais spéculer sur ce qui n'a pas été vérifié — [Anthropic, Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)

**OpenAI, extraits de recherche seulement (page officielle inaccessible ici)**
- Les instructions ont des niveaux d'autorité selon le rôle du message : les messages « developer » passent avant les messages « user ». Le guide montre un message developer structuré en Markdown et XML, avec des sections distinctes et des exemples. Les stratégies listées incluent des exemples d'entrées avec la sortie voulue, ainsi que du contexte. Les balises XML délimitent les documents, et leurs attributs peuvent porter des métadonnées — [OpenAI, Prompt engineering guide](https://developers.openai.com/api/docs/guides/prompt-engineering)
- Selon une analyse tierce, l'exemple officiel suit l'ordre `# Identity` → `# Instructions` → `# Examples` → contexte. **Non vérifié** sur la page officielle — [Appendix: OpenAI prompting guide analysis](https://darioairoldi.github.io/Learn/03.00-tech/05.02-prompt-engineering/04-howto/08.01-appendix_openai_prompting_guide.html)

**Google (Gemini), extraits de recherche seulement**
- Google recommande de toujours mettre des exemples few-shot. Il conseille de préciser les contraintes, c'est-à-dire ce qu'il faut faire et ne pas faire (une longueur maximale par exemple), et de demander un format de réponse précis (tableau, liste, paragraphe). Pour un JSON complexe, Google préfère la fonction de sortie structurée de l'API à la formulation dans le prompt. Si le prompt demande une persona, elle doit figurer dans les instructions système — [Google, Prompt design strategies](https://ai.google.dev/gemini-api/docs/prompting-strategies)
- Un modèle de prompt proposé par Google suit l'ordre objectif et persona → instructions → contraintes → format de sortie → exemples few-shot. Il se termine par un rappel des contraintes et du format en fin de prompt — [Google, Prompt design strategies](https://ai.google.dev/gemini-api/docs/prompting-strategies) (extrait de recherche, formulation exacte non vérifiée)

### Inferences
- **Correspondance entre R-O-T-C-C et les guides officiels :**
  | R-O-T-C-C | Équivalent dans les guides | Couvert ? |
  |---|---|---|
  | Rôle | « Give Claude a role » / « Identity » / « persona » | Oui |
  | Objectif | Objectif (Google). Côté Anthropic, l'objectif fait partie de « clear and direct » | Oui |
  | Tâche | Instructions | Oui |
  | Contexte | « Add context / motivation », documents en `<document>` | Oui, à condition d'expliquer le *pourquoi* et pas seulement le *quoi* |
  | Contrainte | Constraints (Google), formulées de préférence positivement (Anthropic) | Oui |
  | — | **Format de sortie** | **Manquant** |
  | — | **Exemples (few-shot)** | **Manquant**. Les trois éditeurs y insistent |
  | — | **Critères de réussite + test** | **Manquant**. C'est le prérequis n°1 chez Anthropic |
  | — | Structure par balises XML ou Markdown | Manquant. C'est une question de forme, à appliquer partout |
  | — | Comportement face à l'incertitude (« je ne sais pas », vérifier avant d'affirmer) | Manquant. Indispensable pour les contenus envoyés aux clients |
- **Proposition de squelette pour le prompt maître** :
  `<role>`, `<objectif>`, `<contexte>` (entreprise, cibles restaurants et coiffeurs, offre d'abonnement, ton de marque, avec le pourquoi), `<tache>`, `<contraintes>` (formulées positivement, avec la limite humaine : « ne publie ni n'envoie rien sans validation »), `<format_sortie>`, `<exemples>` (2 à 3 exemples variés : un restaurant, un salon, un cas limite), `<criteres_reussite>` (une checklist que l'agent applique à son propre travail avant de le rendre), puis un rappel final des contraintes et du format, comme le fait Google.
- Pour les contenus en français, mieux vaut écrire le prompt lui-même en français et au registre voulu, puisque le style du prompt influence le style de la sortie (déduit du principe « match your prompt style », non testé spécifiquement pour le français).

### Gaps
- Les pages OpenAI et Google n'ont pas pu être lues en entier (réseau bloqué). Leurs citations viennent d'extraits de recherche et devraient être revérifiées en ouvrant les pages.
- Aucune source officielle ne parle du framework « R-O-T-C-C » sous ce nom. Il s'agit d'un acronyme de praticiens, et sa correspondance avec les guides est une analyse de ma part.

## 2. Bonnes pratiques des systèmes multi-agents

### Takeaway
Anthropic conseille de commencer par la solution la plus simple : un appel unique, puis des workflows fixes (chaînage, routage), et seulement ensuite un orchestrateur avec des workers. Le multi-agent apporte beaucoup sur des tâches parallélisables et à forte valeur, mais il consomme environ 15 fois plus de tokens qu'un chat. Il fonctionne mal quand les agents doivent partager beaucoup de contexte ou dépendent étroitement les uns des autres. Pour un consultant solo, la bonne cible est donc **un orchestrateur, des agents spécialisés appelés à la demande, et des workflows fixes pour les tâches répétitives**, plutôt que 9 agents autonomes qui discutent entre eux.

### Cited Findings
- Anthropic distingue deux choses. Les workflows sont des « systems where LLMs and tools are orchestrated through predefined code paths ». Les agents sont des LLM qui « dynamically direct their own processes and tool usage » — [Anthropic, Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)
- Le principe : « find the simplest solution possible, and only increasing complexity when needed ». Les agents « trade latency and cost for better task performance » — [Anthropic, Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)
- Les patterns décrits sont : le chaînage de prompts (tâche découpable en sous-tâches fixes), le routage (catégories distinctes), la parallélisation (par sections ou par vote), l'orchestrateur-workers (« a central LLM dynamically breaks down tasks, delegates them to worker LLMs, and synthesizes their results », utile quand on ne peut pas prévoir les sous-tâches à l'avance), l'évaluateur-optimiseur (critères d'évaluation clairs) et les agents autonomes — [Anthropic, Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)
- Les agents peuvent « pause for human feedback at checkpoints or when encountering blockers ». Leur autonomie entraîne des coûts plus élevés et des erreurs qui s'accumulent, d'où la recommandation de tests en environnement isolé (« sandboxed ») et de garde-fous — [Anthropic, Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)
- L'article cite trois principes : simplicité, transparence (montrer les étapes de planification de l'agent) et soin apporté à l'interface agent-outils (documentation et tests des outils). Il met aussi en garde contre les frameworks qui ajoutent des couches d'abstraction cachant les prompts — [Anthropic, Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)
- Dans le système de recherche multi-agents d'Anthropic (Opus 4 en agent principal, sous-agents Sonnet 4), le résultat dépasse de 90,2 % celui d'un agent Opus 4 seul sur l'évaluation interne — [Anthropic, How we built our multi-agent research system](https://www.anthropic.com/engineering/built-multi-agent-research-system)
- Coût : un agent consomme environ 4 fois plus de tokens qu'un chat, et un système multi-agents environ 15 fois plus. Il n'est rentable que pour des tâches à forte valeur — [Anthropic, multi-agent research system](https://www.anthropic.com/engineering/built-multi-agent-research-system)
- Le multi-agent est mal adapté dans trois cas : les domaines où les agents doivent partager du contexte ou dépendent beaucoup les uns des autres, la plupart des tâches de code, et la coordination en temps réel — [Anthropic, multi-agent research system](https://www.anthropic.com/engineering/built-multi-agent-research-system)
- Pour déléguer, chaque sous-agent doit recevoir un objectif, un format de sortie, des consignes sur les outils et des limites claires de tâche. Des instructions vagues ont conduit à du travail en double. L'effort doit être proportionné à la complexité : une recherche simple, c'est 1 agent et 3 à 10 appels d'outils — [Anthropic, multi-agent research system](https://www.anthropic.com/engineering/built-multi-agent-research-system)
- Mémoire : l'agent principal enregistre son plan en mémoire externe parce que le contexte est tronqué au-delà de 200 000 tokens. Les sous-agents écrivent leurs résultats dans des systèmes externes et ne renvoient que des références légères — [Anthropic, multi-agent research system](https://www.anthropic.com/engineering/built-multi-agent-research-system)
- Évaluation : il faut juger l'état final plutôt que le chemin suivi, et commencer avec environ 20 cas représentatifs. Un juge LLM qui note selon une grille (exactitude, sources, exhaustivité…) s'est montré cohérent avec le jugement humain. Les testeurs humains ont repéré des hallucinations et un biais en faveur des fermes de contenu SEO que l'évaluation automatique avait manqués — [Anthropic, multi-agent research system](https://www.anthropic.com/engineering/built-multi-agent-research-system)
- Pour éviter les sous-agents superflus, Anthropic donne une consigne type : « Use subagents when tasks can run in parallel, require isolated context, or involve independent workstreams that don't need to share state. For simple tasks, sequential operations […] work directly rather than delegating. » — [Anthropic, Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- Côté OpenAI Agents SDK : les **handoffs** délèguent d'un agent spécialisé à un autre, les **guardrails** vérifient les entrées et les sorties, et l'**approbation humaine** suspend l'exécution. « Use guardrails for automatic checks and human review for approval decisions. Together, they define when a run should continue, pause, or stop. » Un outil marqué `needs_approval` met l'exécution en pause jusqu'à l'approbation ou au rejet. L'état peut être sérialisé puis repris — [OpenAI, Guardrails and human review](https://developers.openai.com/api/docs/guides/agents/guardrails-approvals) (extraits de recherche, page non lue en entier)

### Inferences
- Pour Erreur Marketing Bordeaux, la plupart des tâches sont **séquentielles et dépendantes** (stratégie → contenu → visuel → vidéo → publication → analyse). C'est justement le cas où Anthropic juge le multi-agent moins utile. Architecture recommandée :
  - **Orchestrateur = l'agent Stratège** (ou le consultant lui-même au début), qui découpe la demande et appelle les spécialistes.
  - **Workflows fixes** (chaînage) pour les tâches récurrentes : posts hebdomadaires, réponses aux avis Google, rapport mensuel.
  - **Parallélisation** seulement là où elle sert, par exemple quand le Chercheur audite plusieurs concurrents en même temps.
  - **Évaluateur-optimiseur** : faire relire les productions du Rédacteur par un agent « contrôle qualité / voix de marque » avant la validation humaine.
- **Mémoire partagée** : un dossier ou une base unique par client (fiche client, charte de ton, historique de publications, KPI) que chaque agent lit, plutôt que des agents qui se transmettent de longues conversations. C'est l'application du principe « stocker en externe, passer des références ».
- Le coût d'environ 15 fois plus de tokens est absorbé par un forfait fixe (Claude Pro, Max ou Team) tant que l'usage reste dans les limites. En API, il faudrait réserver le multi-agent aux livrables à forte valeur (audit initial, stratégie trimestrielle).

### Gaps
- Aucune donnée publique trouvée sur des équipes de 9 agents dans une TPE ou une agence marketing solo. Le gain mesuré (+90,2 %) concerne la recherche documentaire, pas la production marketing.

## 3. Fiche de chaque agent et points de contrôle humains

### Takeaway
Chaque agent doit avoir une fiche standard : rôle, objectif, entrées, sorties (format), outils autorisés (le minimum nécessaire), KPI et décisions réservées à l'humain. Les sources officielles convergent sur un principe : **toute action irréversible, visible par des tiers ou engageant de l'argent passe par une confirmation humaine**. Concrètement, cela couvre la publication, l'envoi au client, la dépense publicitaire, les prix et la stratégie. Cela donne naturellement la répartition visée d'environ 80 % de travail fait par l'IA et 20 % de décisions humaines.

### Cited Findings
- Anthropic donne une consigne type : il faut évaluer la réversibilité et l'impact d'une action, et demander avant de faire tout ce qui est difficile à annuler, touche des systèmes partagés ou peut être destructeur. La liste inclut les « operations visible to others: […] sending messages » — [Anthropic, Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- Une délégation efficace précise l'objectif, le format de sortie, les outils et les limites de tâche — [Anthropic, multi-agent research system](https://www.anthropic.com/engineering/built-multi-agent-research-system)
- Dans Claude Code, un sous-agent est un fichier Markdown avec un en-tête YAML : `name`, `description` (quand déléguer), `tools` (outils autorisés), `model`, `permissionMode`, `maxTurns`, `skills`, `memory`, puis le prompt système. Les bonnes pratiques : descriptions courtes, outils limités au besoin (« A read-only researcher should not have Write or Edit »), modèle moins cher (Haiku) pour les tâches simples — [Claude Code docs, Subagents](https://code.claude.com/docs/en/sub-agents)
- Dans OpenAI Agents SDK, l'approbation humaine s'applique outil par outil avec `needs_approval` — [OpenAI, Guardrails and human review](https://developers.openai.com/api/docs/guides/agents/guardrails-approvals) (extrait)
- Le connecteur Windsor.ai (outil marketing) impose lui aussi une confirmation de l'utilisateur avant toute action d'écriture, et un jeton de confirmation pour les actions qui démarrent ou augmentent une dépense publicitaire. C'est un exemple concret de point de contrôle sur la dépense pub, observé dans les instructions du serveur MCP Windsor.ai disponibles dans cet environnement (pas d'URL publique citée).

### Inferences
**Proposition de fiches agents** (synthèse de ma part à partir des principes ci-dessus. Les KPI sont indicatifs et non issus d'une source) :

| Agent | Rôle / sorties | Outils (minimum) | KPI | Décision humaine obligatoire |
|---|---|---|---|---|
| Stratège (orchestrateur) | Plan éditorial mensuel par client, priorisation, brief aux autres agents | Lecture de la base clients, rapports de l'Analyste | Respect du calendrier, objectifs atteints | **Validation de la stratégie et de l'offre ou du prix proposé au client** |
| Chercheur | Audit fiche Google, concurrents locaux, tendances Bordeaux, avec sources | Web (lecture seule) | % d'affirmations sourcées, temps d'audit | Aucune décision. L'humain vérifie par sondage les chiffres cités au client |
| Développeur | Pages web ou landing pages, schéma LocalBusiness, petites automatisations | Éditeur de code, preview (pas de déploiement en production) | Score PageSpeed, bugs | **Mise en ligne en production** |
| Rédacteur | Posts, réponses aux avis, descriptions de fiche Google | Charte de ton, fiche client | Taux d'acceptation sans retouche, engagement | **Publication** (en lot hebdomadaire) |
| Designer | Visuels déclinés de la charte (Canva…) | Canva / génération d'image | Taux d'acceptation, cohérence de charte | Validation des visuels montrant des personnes ou des plats réels |
| Monteur vidéo | Reels et shorts à partir des rushes du client | Outil vidéo | Vues, rétention | **Publication**. Validation de tout contenu de synthèse réaliste (deepfake, art. 50(4)) |
| Automatisation | Scénarios Make/n8n (planification, rapports, relances) | Make/n8n, en lecture/écriture limitée | Heures gagnées, taux d'erreur des scénarios | **Activation d'un nouveau scénario** qui écrit chez le client ou envoie des messages |
| Service client | Brouillons de réponses aux clients, FAQ, prise de RDV | Boîte mail en mode **brouillon**, FAQ | Délai de réponse, satisfaction | **Envoi** de tout message sensible : réclamation, résiliation, facturation, litige, avis négatif |
| Analyste | Rapport mensuel (GBP, Instagram, site), alertes | Lecture analytics (GA4, GBP, Meta) | Exactitude des chiffres, ponctualité | Validation du rapport avant envoi au client. **Toute décision de budget pub** |

**Points de contrôle humains (environ 20 %)**, regroupés pour limiter la charge :
1. **Hebdomadaire, environ 1 h** : valider en lot le calendrier de la semaine (posts, visuels, vidéos) pour tous les clients.
2. **Mensuel** : valider le rapport de l'Analyste et les recommandations du Stratège avant l'envoi au client.
3. **Au cas par cas, bloquant** : prix et devis, dépense pub, mise en production, messages sensibles, toute affirmation chiffrée ou promesse (« +30 % de réservations ») dans un contenu destiné au client.
4. **Règle à inscrire dans chaque prompt** : « Tu prépares, tu ne publies pas. Toute action visible par un tiers, irréversible ou qui engage de l'argent → produis un brouillon et demande validation. »

### Gaps
- Aucune source ne donne de ratio de référence « 80/20 ». C'est un objectif de l'entreprise, sans validation empirique trouvée.
- Les KPI de chaque agent sont des propositions, non sourcées.

## 4. Options de mise en œuvre pour un entrepreneur solo non développeur, et coûts

### Takeaway
L'option la plus simple et la moins chère est **un abonnement Claude (Pro à 20 $/mois ou Max à partir de 100 $/mois)**, qui inclut Projects, Skills, connecteurs, Claude Code (sous-agents) et Cowork (agent de bureau avec tâches planifiées). On y ajoute **Make ou n8n** pour les déclenchements automatiques (planification, webhooks). Les GPT personnalisés et Zapier sont des alternatives, mais leurs prix n'ont pas pu être vérifiés ici. Zapier est réputé le plus cher à volume élevé.

### Cited Findings
- **Tarifs Claude** (page officielle, en USD hors taxes, sans prix en euros affichés) : Free 0 $ (jusqu'à 5 Projects, Claude Code non inclus) ; Pro 20 $/mois ou 17 $/mois en annuel (200 $ payés d'avance) ; Max à partir de 100 $/mois ; Team Standard 25 $/siège/mois (20 $ en annuel) et Premium 125 $/siège/mois (100 $ en annuel) ; Enterprise 20 $/siège/mois, minimum 20 sièges, plus l'usage aux tarifs API — [Claude, Pricing](https://claude.com/pricing)
- Selon des sources tierces, Max existe en deux niveaux, 5x à 100 $ et 20x à 200 $. Cowork et Claude Code seraient inclus dans Pro, Max et Team, avec un quota d'usage commun au chat, à Cowork et à Claude Code. Sources tierces, **à vérifier** — [Gradually.ai, Claude pricing](https://www.gradually.ai/en/claude-pricing/); [DEV, Claude Cowork cost](https://dev.to/nishilbhave/how-much-does-claude-cowork-cost-in-2026-free-on-every-paid-plan-3pig)
- **Cowork** est un mode de l'application Claude Desktop qui donne à Claude accès à des dossiers locaux pour enchaîner des tâches en plusieurs étapes de façon autonome, avec des sous-agents pour paralléliser. Les tâches planifiées se lancent avec `/schedule`. Les plugins regroupent skills, connecteurs et sous-agents — [Claude Support, Get started with Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork). Les sources se **contredisent** sur l'exécution des tâches planifiées : dans le cloud, ou seulement quand l'ordinateur est allumé et l'app ouverte — [The Decoder](https://the-decoder.com/claudes-cowork-desktop-app-now-runs-scheduled-tasks-so-your-ai-assistant-works-while-you-sleep/) (à vérifier)
- **Sous-agents Claude Code** : chacun a son propre contexte, son prompt système, ses outils et ses permissions. Ils peuvent tourner sur un modèle moins cher et sont stockés dans `.claude/agents/` (projet) ou `~/.claude/agents/` (utilisateur). Leurs requêtes comptent dans les mêmes limites d'usage que la conversation principale — [Claude Code docs, Subagents](https://code.claude.com/docs/en/sub-agents)
- **n8n** : la version auto-hébergée est gratuite. Le cloud démarrerait autour de 20 €/mois, ou 20 $/mois pour 5 workflows actifs et 2 500 exécutions selon une autre source (chiffres **non vérifiés**, ils divergent). **Make** facture en crédits depuis le 27 août (selon sa page tarifs, citée par une source tierce), et l'IA y est facturée en tokens. **Zapier** Professional coûterait entre 19,99 $ et 29,99 $/mois selon les sources, avec Agents en option payante. Un test tiers chiffre 100 000 actions à 599 $ sur Zapier contre 59 $ sur Make — [DEV, Zapier vs Make vs n8n vs Lindy 2026](https://dev.to/jangwook_kim_e31e7291ad98/zapier-vs-make-vs-n8n-vs-lindy-ai-automation-platform-comparison-2026-419e); [Cut the SaaS](https://cut-the-saas.com/guides/make-vs-zapier-vs-n8n) (sources tierces, chiffres contradictoires)
- **GPT personnalisés (ChatGPT)** : prix et fonctionnalités 2026 **non vérifiés**, la documentation OpenAI étant inaccessible dans cette session.

### Inferences
| Option | Pour | Contre | Coût indicatif |
|---|---|---|---|
| Claude Projects (1 projet par agent ou par client) | Aucune technique, instructions et fichiers persistants | Pas d'automatisation déclenchée, copier-coller entre agents | Inclus dans Pro (20 $) |
| Claude Skills + Cowork | Agents réutilisables, accès aux fichiers locaux, tâches planifiées, plugins | Quotas partagés, comportement des tâches planifiées à vérifier | Pro ou Max (20 à 100 $+) |
| Claude Code + sous-agents | Le plus proche d'une « équipe » : 9 fichiers `.claude/agents/*.md`, outils limités par agent | Interface terminal ou IDE, demande une courbe d'apprentissage | Pro ou Max |
| GPT personnalisés | Faciles à créer et à partager | Prix et limites non vérifiés ici, pas d'orchestration native entre GPT | Non vérifié |
| Make / n8n / Zapier | Déclencheurs (nouvel avis, date), connexions à GBP, Meta, mail | Dépense IA facturée en plus (tokens API), maintenance des scénarios | n8n auto-hébergé gratuit ; Make et Zapier entre ~10 et 70 $/mois+ (non vérifié) |
- Feuille de route suggérée : (1) un Project ou un Skill par agent avec la fiche R-O-T-C-C+F-E-C ; (2) l'orchestration manuelle par le consultant pendant 1 mois ; (3) l'automatisation des 2 ou 3 flux les plus répétitifs dans Make ou n8n, avec une étape « brouillon → validation » (par exemple Slack ou e-mail d'approbation) ; (4) le passage aux sous-agents Claude Code ou Cowork une fois les prompts stabilisés.

### Gaps
- Prix en euros TTC non disponibles sur la page Claude. Prix de ChatGPT, Make et Zapier non vérifiés auprès des éditeurs (sources tierces contradictoires).

## 5. Risques : hallucinations, dérive de la voix de marque, RGPD, AI Act (article 50)

### Takeaway
Les principaux risques sont (a) des faits inventés dans un contenu destiné au client (horaires, prix, chiffres de résultats), (b) une perte progressive de la voix de marque propre à chaque restaurant ou salon, (c) le traitement de données personnelles (avis clients, e-mails, fichiers clients des commerçants), et (d) l'obligation de signaler qu'un chatbot est une IA, **applicable depuis le 2 août 2026 (art. 50(1) AI Act), non reportée par le Digital Omnibus**. Seul le marquage lisible par machine (art. 50(2)) a été décalé, au 2 décembre 2026, d'après plusieurs cabinets d'avocats.

### Cited Findings
- **Hallucinations** : Anthropic recommande d'imposer la vérification avant toute affirmation (« investigate before answering »). Lors des tests humains de son système multi-agents, des réponses inventées et un biais vers les fermes de contenu SEO ont été repérés. Ils ont été corrigés en ajoutant des critères de qualité des sources dans les prompts — [Anthropic, Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices); [Anthropic, multi-agent research system](https://www.anthropic.com/engineering/built-multi-agent-research-system)
- **Dérive de la voix de marque** : les exemples sont « one of the most reliable ways to steer […] tone ». Des exemples variés évitent que le modèle reprenne des motifs non voulus — [Anthropic, Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- **AI Act, art. 50(1)** : les fournisseurs doivent informer les personnes qu'elles interagissent avec un système d'IA (chatbot). L'obligation s'applique depuis le 2 août 2026 et n'a pas été modifiée par le Digital Omnibus — [Jones Walker, « Yes, August 2 still matters »](https://www.joneswalker.com/en/insights/blogs/ai-law-blog/yes-august-2-still-matters-the-eu-approved-a-high-risk-ai-delay-but-most-trans.html); [Goodwin, « Not Delayed, Not Deferred »](https://www.goodwinlaw.com/en/insights/publications/2026/08/alerts-technology-dpc-eu-ai-act-transparency-obligations-now-in-force)
- **Art. 50(2)** : le marquage lisible par machine des contenus générés est reporté au 2 décembre 2026, peut-être seulement pour les systèmes déjà sur le marché avant le 2 août 2026 (le périmètre reste discuté). Les obligations « haut risque » de l'annexe III sont reportées au 2 décembre 2027. Le Digital Omnibus (Règlement (UE) 2026/1744) aurait été publié au JOUE le 24 juillet 2026, mais cette référence n'a pas été vérifiée dans le JO — [Cooley, Digital AI Omnibus](https://cdp.cooley.com/digital-ai-omnibus-delays-key-deadlines-introduces-new-rules/); [Usercentrics](https://usercentrics.com/knowledge-hub/eu-ai-act-high-risk-delay-article-50-transparency-consent/) (numéro de règlement **non vérifié**)
- **Art. 50(4)** : celui qui déploie l'IA doit signaler les deepfakes. Pour un texte généré publié afin d'informer le public sur des questions d'intérêt public, la mention est obligatoire sauf si le texte a fait l'objet d'une relecture humaine avec responsabilité éditoriale. Cette exception suppose une relecture réelle et pas un simple coup d'œil — [Stibbe, Deep fakes, real transparency](https://www.stibbe.com/publications-and-insights/deep-fakes-real-transparency-labelling-deep-fakes-and-ai-generated-public); [artificialintelligenceact.eu, guide art. 50](https://artificialintelligenceact.eu/transparency-rules-article-50/)
- La Commission européenne a adopté des lignes directrices sur l'article 50 — [Stephenson Harwood](https://perspectives.stephensonharwood.com/post/102nfqh/eu-ai-act-update-european-commission-adopts-guidelines-on-article-50-transparenc). Texte officiel de l'article : [AI Act Service Desk (Commission), art. 50](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-50)
- **CNIL / RGPD** : la CNIL a publié des fiches pratiques sur le développement de systèmes d'IA conformes au RGPD : un premier lot en avril 2024, l'intérêt légitime et le web scraping en juin 2025, puis la finalisation en juillet 2025 avec la sécurité, l'annotation et le statut des modèles. Elle y indique que les modèles peuvent relever du RGPD s'ils mémorisent des données personnelles — [CNIL, finalisation des recommandations](https://cnil.fr/fr/ia-finalisation-recommandations-developpement-des-systemes-ia); [CNIL, fiches pratiques IA](https://cnil.fr/fr/les-fiches-pratiques-ia); [CNIL, intérêt légitime](https://cnil.fr/fr/recommandations-developpement-ia-interet-legitime)

### Inferences
- **Garde-fous à inscrire dans les prompts** :
  - « N'invente jamais un fait sur le commerce (horaires, prix, plats, prestations, chiffres). Si l'information n'est pas dans `<fiche_client>`, écris [À COMPLÉTER] » ;
  - aucune promesse de résultat chiffrée dans un contenu client sans source validée ;
  - une fiche de ton de voix par client, avec 3 à 5 exemples validés (posts réels), relue chaque trimestre ;
  - un agent ou une étape « contrôle voix de marque » qui note chaque contenu de 0 à 1 selon une grille avant la validation humaine (méthode du juge LLM d'Anthropic).
- **RGPD (pratique pour un consultant solo)** : Erreur Marketing est probablement sous-traitant (art. 28 RGPD) pour les données clients de ses commerçants. Il faut donc un contrat ou un avenant de sous-traitance, la minimisation des données (ne pas coller de fichiers clients nominatifs dans les prompts), des outils IA en offre professionnelle (Team ou API, conditions de non-entraînement) et l'inscription au registre des traitements. *Qualification juridique déduite, à faire valider : non vérifié auprès de la CNIL pour ce cas précis.* Les fiches CNIL citées portent surtout sur le **développement** de systèmes d'IA, pas sur l'usage d'outils IA par une TPE. Il faudrait chercher séparément une fiche CNIL sur l'**usage** de l'IA générative.
- **AI Act pour l'agent Service client** : si un chatbot discute avec les clients des restaurants ou salons (site, Messenger), il doit afficher clairement qu'il s'agit d'une IA (art. 50(1)). C'est le fournisseur qui porte formellement l'obligation, mais un message d'accueil explicite reste une bonne pratique quel que soit le rôle de l'entreprise. Pour les vidéos ou images réalistes générées de personnes ou de lieux (Monteur vidéo, Designer), il faut prévoir un étiquetage « contenu généré par IA » (art. 50(4)). Pour les posts marketing ordinaires, l'obligation sur le texte « d'intérêt public » ne s'applique probablement pas, et la relecture humaine documentée sert de protection supplémentaire (inférence).

### Gaps
- Texte exact de l'art. 50(1) non lu dans le Journal officiel (eur-lex non testé, réseau restreint). Le numéro du règlement Omnibus (2026/1744) et le périmètre du report au 2 décembre 2026 sont à vérifier dans le JOUE.
- Pas de fiche CNIL trouvée sur l'usage de chatbots ou d'IA générative par une TPE pour ses clients. Les fiches citées visent le développement de systèmes d'IA.
- Pas de données chiffrées trouvées sur la fréquence des hallucinations dans les contenus marketing.
