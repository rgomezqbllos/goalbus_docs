---
title: Chargement et gestion des conducteurs
shortTitle: Conducteurs
intro: Apprenez à créer, importer et maintenir la base des conducteurs sur GoalBus,
  à revoir votre profil d'exploitation et à laisser un modèle fiable avant de passer
  à l'adscription, règles et calcul de Rostering.
contentType: how-tos
versions:
- '*'
---
## Création ou importation du modèle de conducteur

Avant de parler de règles de Rostering, d'absences ou d'attribution de tours, vous devez avoir une base fiable de conducteurs. Dans GoalBus, la gestion des conducteurs agit comme la source principale de vérité pour l'opérativité humaine: elle permet de combiner création manuelle et charge massive, et concentre l'identité, l'affiliation au dépôt et la disponibilité dans un même répertoire.

Utilisez ce quick start quand vous aurez déjà clairement la transition de Scheduling à Rostering et vous aurez besoin de préparer le collectif réel de personnes qui participeront à l'affectation.

Avant de commencer, assurez-vous que:
1. Tu as déjà fermé la transition depuis Scheduling sur P19.
2. Tu sais bien quel groupe de conducteurs participera au calcul.
3. Tu sais si tu vas sortir quelques conducteurs manuellement ou si tu as besoin d'une charge massive.
4. Vous avez accès à l'environnement avec permission de gérer le personnel.

Pour ce quick start, utilisez ce cas de référence:

> **Je vais charger et vérifier le modèle de conducteur qui pourra couvrir la solution de L1 avant d'entrer dans l'affectation, les règles et la disponibilité.**

Pour créer ou importer le modèle de conducteur:
1. Sous GoalBus, allez dans le module **Configuration** > **Personnel** > **Gestion des conducteurs**.
ref: P20_Imagen1.png | compact
2. Vérifiez si les conducteurs de l'affaire existent déjà sur la liste générale.
3. Si vous avez besoin de créer peu de conducteurs, cliquez sur **Nouveau conducteur**.
ref: P20_Imagen2.png | compact(2x)
4. Si vous avez besoin de charger de nombreux conducteurs, effectuez une importation massive par fichier CSV à partir de **Charge personnelle**.
ref: P20_Imagen3.png | compact
5. Si vous choisissez l'importation massive, préparez le fichier avec les données minimales dont votre opération a besoin pour identifier correctement chaque personne. La fenêtre d'importation vous aidera à préparer le CSV de chargement.
ref: P20_Imagen4.png
6. Exécutez la charge et vérifiez le résultat.
7. Retournez à la liste générale et vérifiez que les conducteurs apparaissent correctement.
8. Si vous détectez des doublons ou des enregistrements incomplets, corrigez-les avant de suivre.

Pour le cas de référence, terminez cette section uniquement lorsque vous pouvez affirmer:
1. Les conducteurs de L1 sont déjà sortis ou importés.
2. La liste générale reflète un modèle de référence unique.
3. Vous pouvez déjà ouvrir le profil de chaque conducteur pour vérifier son contexte opérationnel.

Lorsque vous avez terminé cette section, vous devriez avoir un modèle de conducteur chargé et visible dans le système.  &lt; &lt; Filecite &gt; &gt; , " &lt; &lt; Firecite &gt; &gt; , " &lt; &lt; Firefilecite &gt; &gt; , &lt; &lt; L1 &gt; &gt; , &lt; &lt; L2 &gt; &gt; , &lt; &lt; Firefilecite &gt; &gt; , &lt; &lt; L2 &gt; &gt; , &lt; &lt; L24 &gt; &gt; .

## Vérification du profil du conducteur et de ses données structurelles

Une fois le modèle créé, vous devez vérifier le **Profil du conducteur**. Le profil n'est pas seulement une fiche de contact: c'est le dossier numérique complet de l'employé au sein de l'opération. C'est là que cohabitent les données statiques, le contexte opérationnel et les attributs que le système utilisera plus tard pour raisonner son éligibilité.

Avant de commencer cette section, assurez-vous que:
1. Vous avez déjà des conducteurs visibles sur la liste générale.
2. Tu sais quel conducteur ou quel groupe tu utiliseras comme échantillon.
3. Vous voulez valider que l'enregistrement n'est pas seulement administratif, mais opérationnel.

Pour vérifier le profil du conducteur:
1. Dans la liste générale, cliquez sur le nom d'un conducteur.
ref: P20_Imagen5.png | full
2. Vérifiez la barre latérale de données statiques.
3. Vérifiez au moins ces groupes d'information:
   1. les données de base telles que le nom et le code,
   2. les données opérationnelles, telles que la convention collective ou le type de contrat,
   3. des liens opérationnels tels que le dépôt principal, le groupe de travail, la zone ou les types de véhicules autorisés.
4. S'il manque des données structurelles essentielles, remplissez-les avant d'aller plus loin.
5. Garde tout changement nécessaire.
6. Répétez l'examen sur plusieurs conducteurs pour confirmer la cohérence du modèle.

Pour le cas de référence, vérifiez au moins:
1. Le code du conducteur.
2. Votre dépôt principal.
3. Votre groupe de travail.
4. Les propriétés opérationnelles qui conditionneront votre affectation ultérieure.

Une fois cette section terminée, il faut être clair que chaque conducteur dispose d'un dossier opérationnel cohérent et utilisable.

## Revue du contexte opérationnel et des données dynamiques du conducteur

Outre les données structurelles, le profil du conducteur comprend des données dynamiques qui influent directement sur la façon dont le système raisonne sur la personne. Dans l'onglet d'administration, vous pouvez vérifier les compteurs et les modèles de travail, qui font partie du contexte opérationnel utilisé plus tard par la logique d'attribution.

Avant de commencer cette section, assurez-vous que:
1. Tu as vérifié les données statiques du profil.
2. Vous savez si votre opération utilise des compteurs ou des modèles cycliques.
3. Vous voulez vérifier que le conducteur n'existe pas seulement, mais qu'il a un contexte opérationnel interprétatible.

Pour revoir le contexte opérationnel dynamique:
1. Dans le profil du conducteur, ouvrez l'onglet **Détails de l' administration**.
2. Vérifiez les **Compteurs** ou KPI associés au conducteur s'ils existent.
3. Vérifiez si le conducteur est lié à un **modèle de travail**.
4. Si votre opération utilise des modèles cycliques, vérifiez également l'écart ou la position actuelle du conducteur à l'intérieur du schéma.
5. Il confirme que ces données ont un sens pour le contexte réel.
6. Si l'information dynamique n'est pas correcte, ajoutez-la avant de passer à des règles ou à des calculs.

Pour le cas de référence, demandez-vous:
1. Ce conducteur a-t-il le modèle qu'il devrait avoir ?
2. Vos compteurs ou KPI sont-ils disponibles si le processus en a besoin ?
3. Le système pourrait-il raisonner correctement sur cette personne dans un calcul d'affectation?

Lorsque vous avez terminé cette section, vous devez avoir validé non seulement l'identité du conducteur, mais aussi son contexte opérationnel dynamique.

## Validation des qualifications avant utilisation du conducteur à Rostering

Avant de considérer un conducteur comme éligible, vous devez vérifier ses **Attributions**. Ces qualifications répondent à la question  &lt; &lt; Cette personne peut-elle travailler légalement ou techniquement dans ce dépôt, groupe ou unité &gt; &gt;? &lt; &lt; S &apos; &gt; &gt; . Ils sont gérés sur une ligne temporelle avec date de début et de fin, et le système affiche des états comme actif, futur, périmé ou proche d &apos; expiration pour faciliter la lecture. Si une personne n &apos; est pas autorisée dans le contexte requis, le moteur génère une erreur en essayant de l &apos; attribuer. &lt; &lt;  &gt; &gt;

Avant de commencer cette section, assurez-vous que:
1. Tu as vérifié le profil du conducteur.
2. Vous savez quel dépôt, groupe ou unité vous aurez besoin pour votre affaire.
3. Vous comprenez qu'une habilitation n'est pas la même qu'une cession ou un détachement temporaire.

Pour la révision et la validation des qualifications:
1. Dans le profil du conducteur, ouvrez l'onglet **Activations / Qualifications**.
2. Vérifiez s'il existe des registres en vigueur pour:
   1. dépôts,
   2. groupes de travail,
   3. unités d'affaires.
3. Vérifiez l'état visuel de chaque qualification:
   1. active,
   2. futur,
   3. à venir à expiration,
   4. Ça s'est éteint.
4. S'il manque une qualification nécessaire, ajoutez-la avec vos dates correctes.
5. Si une qualification a déjà expiré et ne devrait pas être utilisée, laissez-la comme historique sans essayer de réécrire le passé.
6. Garde les changements.
7. Confirmez que le conducteur est déjà activé dans le contexte où vous comptez l'utiliser.

Pour le cas de référence, ne continuez pas jusqu'à ce que vous puissiez affirmer:
1. Le conducteur est activé pour le bon dépôt.
2. Le groupe de travail requis est couvert.
3. Il n'y a pas de déchéances qui rompent l'éligibilité actuelle.

Lorsque vous aurez terminé cette section, vous devriez avoir des conducteurs qui n'existent pas seulement dans le personnel, mais qui sont également éligibles du point de vue opérationnel et réglementaire.  &lt; &lt; Profilecite &gt; &gt; , &lt; &lt; Turn38file0 &gt; &gt; , &lt; &lt; L17-L34 &gt; &gt; , &lt; &lt; L34 &gt; &gt;

## Confirmant que le modèle est prêt pour la prochaine couche de Rostering

La dernière étape consiste à vérifier que la base des conducteurs est déjà prête à entrer dans la couche suivante: détachement opérationnel, règles, absences et calcul. Ici, l'objectif n'est pas seulement d'avoir des noms chargés, mais un modèle cohérent, traçable et utilisable par le moteur.

Avant de finir, assurez-vous que:
1. Tu as déjà chargé ou importé le modèle.
2. Tu as vérifié les profils principaux.
3. Tu as vérifié les données structurelles et dynamiques.
4. Tu as déjà obtenu des qualifications essentielles.

Pour confirmer que le modèle est déjà prêt:
1. Retourne sur la liste générale des conducteurs.
2. Vérifiez que le collectif nécessaire pour votre affaire est présent.
3. Vérifiez que les profils critiques n'ont pas de trous d'information importants.
4. Assurez-vous que les personnes que vous espérez utiliser sont activées dans le contexte correct.
5. Demandez-vous si le système pourrait déjà utiliser cette base comme point de départ pour:
   1. l'affectation opérationnelle,
   2. règles de Rostering,
   3. et disponibilité réelle.
6. Si la réponse est oui, continuez avec le prochain quick start.
7. Si la réponse est non, corrigez la base des conducteurs avant de suivre.

Pour le cas de référence, ce quick start n'est terminé que lorsque vous pouvez affirmer:
1. Le modèle de conducteur L1 est déjà chargé.
2. Les profils clés ont déjà été révisés.
3. Les qualifications essentielles sont déjà en vigueur.
4. La base est prête à être mise en service.

Une fois cette section terminée, vous devriez avoir un modèle de conducteur suffisamment solide pour continuer avec la couche suivante de Rostering.

## Lectures supplémentaires

- [Gérer le détachement opérationnel du conducteur](P21_Gérer_Le_Détachement_Opérationnel_Du_Conducteur.md)
