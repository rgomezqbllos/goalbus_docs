---
title: Création d'une nouvelle itération du scénario à partir d'une solution publiée
shortTitle: Nouvelle itération
intro: Apprenez à créer une nouvelle itération d'un scénario déjà publié pour tester
  les améliorations, régler les paramètres ou introduire des modifications sans modifier
  la version qui est déjà en cours d'exploitation.
contentType: how-tos
versions:
- '*'
---
## Sur la base d'une solution publiée sans modifier la version actuelle

Après la publication d'une solution, il est normal que vous deviez continuer à travailler sur elle. Vous pourriez vouloir ajuster les règles, essayer une autre logique de rotation, intégrer des changements d'offre ou préparer une amélioration pour une période future. Dans ce cas, vous ne devriez pas modifier directement la version déjà publiée. La bonne chose à faire est de créer une **nouvelle itération** du scénario pour maintenir la traçabilité et protéger la version qui est déjà en vigueur.

Utilisez cette quick start lorsque vous avez déjà un scénario avec une solution à l'état **Publiée** et vous devez générer une nouvelle variante sans perdre la référence historique de la solution implantée.

Avant de commencer, assurez-vous que:
1. Tu as déjà publié le scénario précédent sur P16.
2. La solution du scénario que vous prendrez comme base est dans l'état **Publiée**.
3. Tu sais à quel point tu veux revoir ou améliorer l'itération suivante.
4. Il est clair que la nouvelle itération ne doit pas remplacer automatiquement la version en vigueur jusqu'à ce qu'elle revienne au calcul, à la validation et à la publication.

Pour ce quick start, utilisez ce cas de référence:

> **Je vais créer une nouvelle itération du scénario publié sur la ligne L1 pour tester les améliorations de la solution sans toucher à la version qui est déjà en cours d'exploitation.**

Pour une solution publiée en toute sécurité:
1. Sous GoalBus, ouvre le module **Scénarios de planification**.
2. Localisez le scénario dont la solution est dans l'état **Publiée**.
3. Vérifiez votre nom, description, type de jour et lignes associées.
4. Confirmez que c'est vraiment la version que vous voulez utiliser comme référence.
5. Évitez d'éditer cette version directement comme si c'était un nouveau projet.
6. Décidez quel changement vous voulez introduire dans la nouvelle itération:
   1. règles,
   2. paramètres,
   3. offre,
   4. ou des ajustements structurels autorisés.

Une fois cette section terminée, vous devriez avoir clairement identifié le scénario publié qui servira de base à votre nouvelle itération.

## Création de la nouvelle itération depuis le scénario publié

Une fois la base identifiée, l'étape suivante est de créer un **nouvelle itération**. L'objectif est de conserver la version publiée comme référence historique et d'ouvrir une nouvelle branche de travail contrôlée sur la même logique opérationnelle.

Avant de commencer cette section, assurez-vous que:
1. Tu as déjà identifié la bonne solution publiée.
2. Tu sais pourquoi tu as besoin d'une nouvelle itération.
3. Il est clair que la nouvelle itération doit être clairement différente de la version précédente.

Pour créer la nouvelle itération:
1. Dans la table des scénarios, ouvrez le menu des actions du scénario publié.
2. Sélectionnez l'option **créer une nouvelle itération** en cliquant sur **duplication** le scénario comme base de travail.
ref: P17_Imagen1.png | compact
3. Saisissez un **nouveau nom** pour l'itération.
4. Si vous appliquez, mettez à jour le **description** pour refléter l'objectif du changement.
5. Garde la nouvelle itération.
ref: P17_Imagen2.png | compact
6. Vérifiez que le nouveau scénario apparaît comme une entité distincte du scénario publié.
ref: P17_Imagen3.png | full
7. Vérifiez que la version originale publiée reste intacte et différenciée de la nouvelle.

Dans le cas de référence, une option valable pourrait être:
- **Calcul classique - L1 ouvrable - Iteration 2**
- **L1 ouvrable - amélioration des règles de rotation**

Une fois cette section terminée, vous devriez avoir une nouvelle itération créée sans perdre la traçabilité de la version publiée.

## Définir quels changements appartiennent à la nouvelle itération

Après avoir créé l'itération, vous devez décider ce que vous allez réellement changer. Toutes les itérations ne poursuivent pas le même objectif. Certaines servent à ajuster des règles, d'autres à améliorer l'efficacité, d'autres à refléter une nouvelle offre ou une variation opérationnelle future.

Avant de commencer cette section, assurez-vous que:
1. Tu as créé la nouvelle itération.
2. Tu sais quel aspect de la solution précédente tu veux revoir.
3. Vous êtes prêt à limiter le passage à un objectif spécifique afin de ne pas mélanger trop de variables.

Pour définir la portée de l'itération:
1. Ouvre la nouvelle scène.
2. Vérifiez quels éléments vous voulez conserver exactement comme dans la version publiée.
3. Décide quel élément vous allez d'abord changer:
   1. **règles applicables aux véhicules**,
   2. **Règles de rotation**,
   3. **paramètres du moteur**,
   4. **Offre de service**,
   5. **matrices logistiques**.
4. Évitez de changer trop de choses à la fois dans la première itération, sauf si cela est strictement nécessaire.
5. Documente dans le nom ou dans la description l'objectif de l'itération.
6. Enregistrez les changements descriptifs avant de passer au calcul.

Pour le cas de référence, utilisez une logique comme celle-ci:
1. Conserver la même offre de L1.
2. Ajuster seulement le modèle de règles de rotation.
3. Recalculer pour comparer la nouvelle solution avec celle publiée.

Quand tu auras fini cette section, tu devrais avoir une nouvelle itération avec un objectif clair et serré.

## Récalculer l'itération et la comparer à la version précédente

Une fois la portée définie, vous devez recalculer l'itération. Ici l'avantage est que vous ne partez plus de zéro: des parties d'une solution connue et vous pouvez mieux comparer l'impact du changement.

Avant de commencer cette section, assurez-vous que:
1. Tu as créé la nouvelle itération.
2. Tu as déjà défini l'objectif du changement.
3. Tu as déjà vérifié les règles, les paramètres ou les entrées que tu vas modifier.

Pour recalculer la nouvelle itération:
1. Vérifiez la scène et confirmez que vos entrées restent cohérentes.
2. Réglez l'élément que vous voulez modifier.
3. Enregistre les paramètres.
4. Exécute le calcul du nouveau scénario.
5. Attends que le scénario termine la phase de calcul.
6. Vérifiez si l'itération passe à **Solution préparée** ou **Édition**.
7. Comparez le résultat à la version précédente en utilisant:
   1. KPI,
   2. structure générale,
   3. logique des tâches,
   4. et cohérence opérationnelle.
8. Si le changement améliore le résultat, la révision formelle se poursuit.
9. Si le changement aggrave le résultat, conservez la version publiée comme référence et décidez si vous souhaitez corriger ou écarter cette itération.

Pour le cas de référence, comparez:
1. La solution publiée de L1.
2. La nouvelle itération avec réglage des règles.
3. Ce qui a changé dans la qualité, la viabilité ou l'équilibre.

Une fois cette section terminée, vous devriez avoir une nouvelle solution calculée et une base claire pour la comparer à la version déjà publiée.

## Décider si la nouvelle itération remplacera la version en vigueur

La dernière étape est de décider si cette itération mérite de devenir la nouvelle version opérationnelle. Une itération ne remplace pas automatiquement la publication précédente. Pour arriver à la production, vous devez passer par la révision, la validation et la publication avec votre propre cycle de vie.

Avant de finir, assurez-vous que:
1. Tu as calculé la nouvelle itération.
2. Vous avez déjà comparé le résultat à la solution publiée.
3. Vous savez si le changement apporte une réelle amélioration ou seulement une variante sans valeur opérationnelle.

Pour clore la décision sur l'itération:
1. Regardez la nouvelle solution d'un point de vue technique et opérationnel.
2. Si l'itération améliore clairement la solution existante, préparez-la à:
   1. validation,
   2. et publication ultérieure.
3. Si l'itération n'a pas amélioré le résultat, elle conserve la version publiée actuelle comme référence en vigueur.
4. Ne supprimez pas la publication précédente uniquement parce qu'il y a une nouvelle itération.
5. Gardez les deux versions bien identifiées pour un audit et une comparaison historique.
6. Si vous décidez d'aller de l'avant, traitez l'itération comme un nouveau scénario qui doit parcourir son propre flux jusqu'à **Publié**.

Pour le cas de référence, terminez ce quick start seulement lorsque vous pouvez affirmer l'une de ces deux choses:
1. La nouvelle itération de L1 améliore la version publiée et mérite de poursuivre son cycle.
2. La version publiée actuelle est encore meilleure et l'itération restera uniquement en tant qu'essai ou référence.

Une fois cette section terminée, vous devriez avoir une nouvelle itération calculée, comparée et prête à devenir une nouvelle version ou à être conservée en tant que variante d'analyse.

## Lectures supplémentaires

- [Mise en œuvre et validation du premier calcul de Scheduling](P15_Mise_En_Œuvre_Et_Validation_Du_Premier_Calcul_De_Scheduling.md)
