---
title: Examen des conflits, de la couverture et de la viabilité du personnel
shortTitle: Conflits et couverture
intro: Apprenez à revoir la solution de Rostering après le calcul, identifier les
  conflits de couverture, distinguer si le problème vient de règles, disponibilité
  ou détachement, et décider quoi corriger avant de valider l'attribution.
contentType: how-tos
versions:
- '*'
---
## Comprendre ce que vous devez vérifier après le calcul de Rostering

Après l'exécution du premier calcul de Rostering, l'étape suivante n'est pas de valider immédiatement la solution. Vous devez d'abord vérifier si l'allocation est réellement réalisable. À ce stade, l'objectif est de vérifier si le système a réussi à couvrir le travail avec des personnes réelles dans le respect des contraintes de travail, disponibilité et contexte opérationnel.

Utilisez cette quick start lorsque vous avez déjà exécuté le calcul de Rostering et vous devez vérifier si la solution peut être considérée comme complète, partielle ou conflictuelle.

Avant de commencer, assurez-vous que:
1. Tu as déjà fait le premier calcul de Rostering sur P25.
2. Tu sais quelle solution Scheduling a joué comme entrée.
3. Tu as déjà compris quel groupe de conducteurs a participé au calcul.
4. Vous êtes prêt à analyser la solution avant de la valider.

Pour ce quick start, utilisez ce cas de référence:

> **Je vais vérifier la solution de Rostering sur la ligne L1 pour vérifier si le travail a été couvert, s'il y a des conflits d'affectation et si le résultat est viable avant de le valider.**

Pour comprendre ce qu'il faut réviser après le calcul:
1. Il traite la révision comme une phase de diagnostic, pas comme une approbation automatique.
2. Vérifiez toujours trois dimensions:
   1. **couverture**,
   2. **conflits**,
   3. **faisabilité générale**.
3. Ne donnez pas une bonne solution juste parce que le moteur a terminé le calcul.
4. Considère qu'une solution peut:
   1. couvrir tout le travail,
   2. couvrir partiellement,
   3. ou de créer des conflits qui obligent à revenir à des règles, à la disponibilité ou à l'affectation.

Quand vous aurez terminé cette section, vous devriez savoir ce que signifie revoir une solution de personnel et quelles questions vous devez répondre avant de la valider.

## Révision de la couverture du travail assigné

La première question à laquelle vous devez répondre est simple: **Est-ce que tout le travail a été couvert ?**. Ici, il ne s'agit pas encore de savoir pourquoi quelque chose a échoué, mais de mesurer si le système a réussi à affecter des personnes au travail hérité de Scheduling.

Avant de commencer cette section, assurez-vous que:
1. Vous avez déjà visible la solution calculée.
2. Tu sais à quel point tu t'attendais à ce que je te couvre.
3. Vous pouvez déjà vérifier le résultat par ligne, groupe ou collectif.

Pour vérifier la couverture:
1. Ouvre la solution de Rostering calculée.
2. Vérifiez la vue d'ensemble du résultat.
3. Identification & #160;:
   1. les tâches couvertes,
   2. les tâches non couvertes,
   3. et affectations partielles, le cas échéant.
4. Pour cela, aidez les KPI visibles dans la solution.
ref: P26_Imagen1.png | compact
4. Vérifiez si la couverture est complète ou s'il y a des trous grâce aux KPI quotidiens visibles.
ref: P26_Imagen2.png | full
5. Si le système affiche des compteurs ou des résumés de couverture (KPIs des conducteurs), vérifiez-les.
ref: P26_Imagen3.png | compact
6. Si la couverture n'est pas complète, ne validez pas encore la solution.
7. Marquez mentalement où sont les trous pour les analyser plus tard.

Pour le cas de référence, demandez-vous:
1. Le travail de L1 a-t-il été entièrement couvert ?
2. Y a-t-il des jours ou des bandes avec des trous ?
3. Le problème affecte-t-il toute la ligne ou seulement une partie du service ?

Une fois cette section terminée, vous devriez savoir si la solution couvre l'ensemble du travail ou s'il y a des tâches non assignées.

## Détecter les conflits et lire leur cause probable

Après avoir examiné la couverture, vous devez identifier les conflits. Un conflit ne signifie pas automatiquement qu'il manque du personnel. Il peut signifier qu'une règle est trop restrictive, qu'une personne est mal rattachée ou qu'une absence ou une cession a été mal modelée.

Avant de commencer cette section, assurez-vous que:
1. Tu as déjà identifié les tâches non couvertes.
2. Vous êtes déjà prêt à différencier les causes plutôt que de corriger par intuition.
3. Tu sais quelle partie de la solution vérifier d'abord.

Pour examiner les conflits de manière utile:
1. Vérifiez les tâches qui n'ont pas été assignées ou qui ont posé problème.
2. Regardez si le système affiche des messages, des indicateurs ou des conflits associés.
3. Essayez de classer la cause probable dans l'un de ces groupes:
   1. **des règles trop restrictives**,
   2. **insuffisance de disponibilité**,
   3. **l &apos; affectation ou l &apos; habilitation incorrectes**,
   4. **structure héritée de Scheduling**.
4. Si le conflit semble affecter de nombreuses personnes du même groupe, il révise d'abord les règles et l'affectation.
5. Si le conflit concerne des cas individuels, vérifiez d'abord disponibilité, absence ou cession.
6. Si le problème semble provenir du travail hérité, envisagez de retourner à Scheduling.

Pour le cas de référence, posez-vous ces questions:
1. La tâche n'a pas été couverte parce qu'il n'y avait personne disponible ?
2. La personne existait-elle, mais n'était-elle pas qualifiée ou rattachée au contexte correct ?
3. La règle de Rostering a bloqué une affectation qui semblait possible ?
4. Le problème n'est-il pas du personnel, mais du travail hérité ?

Une fois cette section terminée, vous devriez avoir une hypothèse raisonnable sur la cause des conflits majeurs.

## Examen de la faisabilité globale de la solution

Une solution peut être presque couverte et ne pas être bonne. C'est pourquoi, en plus de la couverture et des conflits, vous devez réviser la **faisabilité générale**. Ici la question n'est pas seulement de savoir si le système a affecté des personnes, mais si l'affectation qui en résulte a un sens opérationnel et humain.

Avant de continuer, assurez-vous que:
1. Tu as vérifié la couverture.
2. Tu as déjà identifié des conflits majeurs.
3. Tu es prêt à évaluer la qualité, pas seulement la quantité.

Pour examiner la faisabilité globale:
1. Vérifiez si la répartition du travail semble raisonnable.
2. Vérifiez s'il y a des signes de déséquilibre évident entre les personnes ou les groupes.
3. Vérifie si la solution semble répondre aux critères suivants:
   1. pauses,
   2. limites,
   3. des critères fondamentaux d &apos; équité,
   4. et cohérence opérationnelle.
4. Si la solution couvre le travail, mais le fait de manière très forcée, ne la valide pas encore.
5. Si le résultat semble opérationnel, équilibré et explicable, il continue vers la décision finale.

Pour le cas de référence, demandez-vous:
1. La couverture a-t-elle été obtenue de manière raisonnable ou trop forcée?
2. L'affectation semble-t-elle équilibrée entre conducteurs ?
3. La solution semble-t-elle applicable dans le monde réel ou uniquement valable sur papier?

Une fois cette section terminée, vous devriez avoir une lecture plus complète de la question de savoir si la solution mérite d'avancer ou si elle a besoin d'être corrigée.

## Décider quoi corriger avant de valider

La dernière étape est de transformer l'analyse en une décision pratique. Ici, l'objectif n'est pas de tout arranger une fois pour toutes, mais d'identifier la couche de correction suivante.

Avant de finir, assurez-vous que:
1. Tu as vérifié la couverture.
2. Tu as déjà analysé les conflits.
3. Tu as déjà apprécié la faisabilité générale.
4. Tu sais si la solution peut avancer ou non.

Pour décider quoi corriger avant de valider:
1. Si le problème principal est **règles**, retournez à P22.
2. Si le problème principal est **absences, inactivité ou disponibilité**, retournez à P23.
3. Si le problème principal est **cession, transfert ou détachement**, retournez à P24 ou P21 selon le cas.
4. Si le problème principal est le travail hérité, retournez à Scheduling.
5. Si la solution est suffisamment complète et viable, préparez-la pour validation.
6. Ne validez pas une solution uniquement parce que  &lt; &lt; Presque fonctionne &gt; &gt; , Validez-la lorsque vous comprenez pourquoi elle fonctionne et pourquoi les conflits restants sont acceptables ou résolus.

Pour le cas de référence, terminez ce quick start seulement lorsque vous pouvez affirmer l'une de ces deux choses:
1. La solution L1 est déjà suffisamment solide pour être validée.
2. Tu sais exactement quelle couche tu dois corriger avant de réestimer.

Une fois cette section terminée, vous devriez avoir une lecture claire de la couverture, des conflits et de la faisabilité, et une décision pratique sur l'étape suivante.

## Lectures supplémentaires

- [Validation et consolidation de la solution de Rostering](P27_Validation_Et_Consolidation_De_La_Solution_De_Rostering.md)
