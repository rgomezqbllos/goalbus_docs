---
title: De Scheduling à Rostering
shortTitle: De Scheduling à Rostering
intro: Apprenez ce qui doit être prêt à Scheduling avant d'entrer dans Rostering,
  quelles informations hérite l'affectation du personnel et quels problèmes doivent
  être résolus avant de calculer les conducteurs réels.
contentType: how-tos
versions:
- '*'
---
## Confirmant ce qui doit être fermé à Scheduling avant de passer à Rostering

Avant d'entrer dans Rostering, vous devez vérifier que Scheduling a déjà laissé une base suffisamment stable. Rostering ne remplace pas Scheduling. Rostering partie du travail déjà construit et décide comment l'attribuer à de vraies personnes.

Utilisez cette quick start lorsque vous avez déjà une solution de Scheduling calculée et validée, et vous devez décider si vous pouvez déjà commencer à travailler avec du personnel réel.

Avant de commencer, assurez-vous que:
1. Tu as créé, calculé et validé la scène de Scheduling.
2. Tu as déjà vérifié l'offre de service et sa cohérence générale.
3. Tu sais quelles lignes, quel genre de jour et quelle solution tu utiliseras comme référence.
4. Tu es sûr que Rostering n'est pas l'endroit pour réparer une mauvaise base structurelle de Scheduling.

Pour ce quick start, utilisez ce cas de référence:

> **Je vais confirmer que la solution validée de Scheduling pour la ligne L1 est déjà assez mûre pour passer à Rostering et commencer à affecter du travail à de vrais conducteurs.**

Pour confirmer que Scheduling est prêt:
1. Ouvre la scène de Scheduling que tu utiliseras comme référence.
2. Vérifiez que votre état est déjà le bon pour arrêter de le traiter comme un projet de travail.
3. Vérifiez que l'offre utilisée reste la bonne.
4. Vérifiez que la logique des véhicules et la logique des tours ont déjà été appliquées.
5. Il confirme qu &apos; il n &apos; y a pas d &apos; incohérences structurelles évidentes dans la solution.
6. Si vous avez encore besoin de refaire la base de véhicules, temps, services ou règles, retournez à Scheduling avant de suivre.
7. Si la solution est déjà stable, continuez à l'étape suivante.

Pour le cas de référence, ne continuez pas jusqu'à ce que vous puissiez affirmer:
1. La solution de L1 a déjà été calculée.
2. Il a déjà été vérifié.
3. Il n'a plus besoin de corrections structurelles de Scheduling.
4. Il peut déjà être traité comme une base de travail pour le personnel.

Quand tu auras fini cette section, tu devrais savoir si Scheduling a déjà fourni une base utilisable pour Rostering.

## Je comprends ce que Rostering hérite de Scheduling

Une fois la base confirmée, vous devez comprendre ce qui se passe de Scheduling à Rostering. Ici la clé est de ne pas penser que Rostering commence à zéro. Rostering hérite du travail déjà structuré et de là décide quelle personne réelle peut l'assumer.

Avant de commencer cette section, assurez-vous que:
1. Tu as déjà identifié la solution de Scheduling que tu vas utiliser.
2. Tu sais quelle partie de cette solution doit rester stable.
3. Vous comprenez que Rostering travaille sur le travail déjà construit, pas sur une offre sans structurer.

Pour comprendre ce que Rostering hérite:
1. Vérifiez la solution validée de Scheduling.
2. Il identifie les tâches, les blocs ou les structures de travail qui serviront de base.
3. Vérifiez que la solution a déjà une forme reconnaissable du point de vue opérationnel.
4. N'oubliez pas qu'en passant à Rostering, le système ne crée plus de travail abstrait, mais tente d'attribuer ce travail à de vraies personnes.
5. Utilisez cette règle de lecture:
   1. Scheduling définit **Quel travail existe-t-il?**.
   2. Rostering définit **qui fera ce travail**.

Pour le cas de référence, demandez-vous:
1. La solution de L1 a-t-elle déjà un travail suffisamment clair pour l'attribuer ?
2. Les blocs de travail sont-ils reconnaissables et utilisables ?
3. Le problème qui reste à résoudre est celui des personnes et non celui de la structure ?

Quand tu auras fini cette section, tu devrais comprendre ce que Rostering hérite et ce qui ne devrait pas être redéfini là-bas.

## Différents problèmes sont résolus à Scheduling et quels problèmes à Rostering

Avant de passer définitivement à la cape du personnel, vous devez bien séparer les responsabilités. Cette distinction est fondamentale parce que de nombreuses erreurs apparaissent lorsque vous essayez de corriger à Rostering quelque chose qui aurait dû être résolu plus tôt à Scheduling.

Avant de continuer, assurez-vous que:
1. Tu sais quel scénario Scheduling sera la base.
2. Vous comprenez que Rostering consomme une solution antérieure.
3. Vous êtes prêt à distinguer les problèmes structurels des problèmes de personnel.

Pour bien séparer les deux domaines & #160;:
1. Il traite comme problème **Scheduling** toute question liée à:
   1. structure du service,
   2. logique de la flotte,
   3. temps,
   4. règles applicables aux véhicules,
   5. les types de tours et leur construction de base.
2. Il traite comme problème **Rostering** toute question liée à:
   1. disponibilité réelle du conducteur,
   2. d'un dépôt ou d'un groupe,
   3. absences,
   4. d'inactivité,
   5. cessions ou transferts,
   6. L'éligibilité réelle à un tour de garde.
3. Si vous détectez une incohérence de travail qui affecte l'ensemble de la structure, retournez à Scheduling.
4. Si vous détectez une incohérence de personne, résumez-la à Rostering.

Pour le cas de référence, utilisez cette logique:
1. Si le problème est que le travail de L1 a été mal construit, retourne à Scheduling.
2. Si le problème est que vous ne savez pas quel vrai conducteur peut prendre ce travail, vous entrez correctement dans Rostering.

Une fois cette section terminée, vous devriez être en mesure d'expliquer clairement ce qui doit être corrigé avant de passer au personnel et ce qui appartient au module suivant.

## Confirmer ce qui doit être prêt du côté personnel avant de calculer Rostering

Maintenant que vous savez ce que Rostering reçoit, vous devez vérifier ce qui doit exister du côté personnel pour que le prochain calcul ait un sens. Il ne suffit pas d'avoir un bon Scheduling si vous n'avez pas encore une base minimale de personnes, d'affectations et de disponibilité.

Avant de commencer cette section, assurez-vous que:
1. Tu as déjà une base valable depuis Scheduling.
2. Vous savez quels groupes, dépôts ou contextes opérationnels affectent les gens.
3. Tu es prêt à examiner le personnel.

Pour confirmer que la base de personnel est prête:
1. Il constate qu &apos; il existe déjà un groupe de personnel qui peut recevoir le travail.
2. Vérifiez que les gens sont attachés au contexte correct lorsqu'ils appliquent.
3. Vérifiez que vous n'entrez pas dans Rostering sans informations minimales de disponibilité.
4. Vérifiez s'il existe déjà la structure nécessaire pour:
   1. règles de Rostering,
   2. absences,
   3. d'inactivité,
   4. les transferts ou cessions, lorsqu'ils sont appliqués.
5. Si vous n'avez pas encore cette base, ne lancez pas le calcul du personnel.
6. Si la base existe déjà ou est au moins orientée, continuez avec les quick starts suivants de Rostering.

Pour le cas de référence, demandez-vous:
1. Y a-t-il déjà du personnel qui pourrait recevoir la solution de L1 ?
2. Ce personnel appartient-il au bon domaine?
3. La base de disponibilité et d'affectation est-elle déjà au minimum prête ?

Quand tu auras fini cette section, tu devrais savoir si le personnel est prêt à entrer à Rostering.

## Éclaircir le point de passage entre Scheduling et Rostering

La dernière étape est de fermer mentalement la transition. Ce quick start n'a pas encore l'intention de calculer l'affectation du personnel. Il veut être très clair quand Scheduling se termine et quand Rostering commence pour ne pas mélanger les deux domaines.

Avant de finir, assurez-vous que:
1. Tu as vérifié la solution de Scheduling.
2. Tu as compris l'héritage de Rostering.
3. Tu as déjà séparé les problèmes structurels des problèmes de personnel.
4. Tu as vérifié s'il y a un minimum de personnel.

Pour fermer correctement la transition:
1. Il traite la solution validée de Scheduling comme entrée formelle de Rostering.
2. Ne modifiez pas cette base à moins de détecter un vrai problème structurel.
3. Utilisez les quick starts suivants pour préparer:
   1. règles de Rostering,
   2. absences et inactivité,
   3. transferts, cessions et changements de détachement.
4. Considère que l'objectif change d'ici:
   1. Il ne s'agit plus de construire du travail,
   2. Il s'agit maintenant de l'affecter à de vraies personnes.
5. Si vous pouvez affirmer cela clairement, la transition est bien faite.

Pour le cas de référence, ce quick start n'est terminé que lorsque vous pouvez affirmer:
1. Scheduling a déjà laissé une solution stable de L1.
2. Le problème suivant n &apos; est plus structurel, mais celui de l &apos; affectation du personnel.
3. Tu peux entrer dans la couche des règles de Rostering.

Quand tu auras fini cette section, tu devrais avoir une transition claire et contrôlée entre Scheduling et Rostering.

## Lectures supplémentaires

- [Définir les règles de Rostering pour l'affectation du personnel](P20_Chargement_Et_Gestion_Des_Conducteurs.md)
