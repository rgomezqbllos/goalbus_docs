---
title: Validation et consolidation de la solution de Rostering
shortTitle: Validar Rostering
intro: Apprenez à clore la révision de la solution de Rostering, à valider l'affectation
  du personnel lorsqu'elle est déjà opérationnellement fiable et à la consolider comme
  référence prête pour une utilisation ultérieure ou une intégration avec l'opération.
contentType: how-tos
versions:
- '*'
---
## Confirmant que la solution est prête à être validée

Après examen de la couverture, des conflits et de la faisabilité, l'étape suivante est de décider si la solution de Rostering peut déjà être considérée comme suffisamment solide. Valider ne signifie pas seulement donner un bon accord administratif. Cela signifie que l'affectation du personnel est déjà cohérente, compréhensible et utilisable comme base approuvée.

Utilisez cette quick start lorsque vous avez déjà exécuté le calcul de Rostering, vous avez analysé son résultat et vous devez fermer formellement la solution avant de poursuivre sa consolidation.

Avant de commencer, assurez-vous que:
1. Tu as déjà fait le calcul de Rostering sur P25.
2. Tu as déjà vérifié les conflits, la couverture et la faisabilité sur P26.
3. Tu as déjà réglé les principaux problèmes ou tu comprends pourquoi les conflits restants sont acceptables.
4. Tu sais quelle solution concrète tu vas valider.

Pour ce quick start, utilisez ce cas de référence:

> **Je vais valider la solution de Rostering de la ligne L1 parce que l'affectation couvre déjà le travail de manière suffisamment fiable et je veux la consolider comme référence approuvée.**

Pour confirmer que la solution est prête à être validée:
1. Ouvre la solution de Rostering que tu utiliseras comme référence.
2. Vérifie une dernière fois la couverture du travail.
3. Il confirme que les conflits principaux ont déjà été résolus ou diagnostiqués.
4. Vérifie si l &apos; allocation qui en résulte reste cohérente avec:
   1. les règles de Rostering,
   2. la disponibilité effective du personnel,
   3. l'affectation opérationnelle,
   4. et la solution héritée de Scheduling.
5. Si vous détectez un problème majeur non résolu, ne validez pas encore la solution.
6. Si la base est déjà stable, continuez au passage de validation.

Pour le cas de référence, ne continuez pas jusqu'à ce que vous puissiez affirmer:
1. Le travail de L1 est déjà couvert ou les vides restants sont compris.
2. La solution est opérationnellement défendable.
3. Tu n'as plus besoin de changer de structure avant de l'approuver.

Une fois cette section terminée, vous devriez être sûr que la solution mérite déjà une validation formelle.

## Mise en œuvre de la validation de la solution de personnel

Une fois que la solution est suffisamment stable, vous devez exécuter la validation. Cette étape marque la fermeture de la phase de calcul et de révision de Rostering, et convertit la solution en une référence approuvée dans le flux de travail.

Avant de commencer cette section, assurez-vous que:
1. Tu as décidé que la solution était valable.
2. Tu n'as plus besoin de recalculer ou d'ajuster les règles avant d'approuver.
3. Vous savez que valider signifie geler la solution comme référence approuvée.

Pour valider la solution de Rostering:
1. De la vue de la solution ou du tableau principal, ouvrez le menu d'actions correspondant.
ref: P27_Imagen1.png | full
2. Sélectionnez l'action **Valider**.
3. Vérifiez le résumé final de la solution avant de confirmer.
4. Il confirme la validation à la demande du système.
5. Vérifiez que l'état de la solution passe à l'état d'approbation correspondant.
6. Vérifiez que la solution n'est plus traitée comme une version provisoire de travail.
7. Si votre flux utilise des autorisations spécifiques, confirmez que la validation a été correctement enregistrée.

Dans le cas de référence, assurez-vous que:
1. La solution de L1 change d'état après validation.
2. Le système la reconnaît déjà comme une version approuvée.
3. La solution cesse d'être traitée comme une itération encore ouverte.

Une fois cette section terminée, vous devriez avoir une solution de Rostering officiellement validée.

## Consolider la solution en tant que référence opérationnelle

Après validation, vous devez consolider la solution. Consolider signifie traiter cette version comme la référence approuvée pour le prochain niveau du processus. À partir de là, la solution ne devrait plus être gérée comme un test, mais comme la base sérieuse et traçable de l'affectation du personnel.

Avant de commencer cette section, assurez-vous que:
1. La solution est déjà validée.
2. Vous savez si c'est la référence en vigueur ou une version approuvée en attente d'utilisation ultérieure.
3. Vous pouvez déjà distinguer une solution approuvée d'une solution en cours d'examen.

Pour consolider la solution validée:
1. Vérifiez le nom et la description de la solution.
2. Si nécessaire, mettez à jour la description afin de préciser:
   1. le contexte dans lequel il couvre,
   2. la période qu'il représente,
   3. et pourquoi elle a été approuvée.
3. Vérifiez que la solution validée est clairement distincte des versions préliminaires, des essais ou des itérations.
4. Si votre processus interne l'exige, enregistrez que cette version devient la référence pour la prochaine étape.
5. Il conserve les versions antérieures en tant qu'historique, mais évite de les traiter comme s'ils étaient équivalents à la solution approuvée.

Dans le cas de référence, assurez-vous que:
1. La solution validée de L1 se distingue clairement des essais ou des versions intermédiaires.
2. L'équipe peut l'identifier comme la bonne référence.
3. La traçabilité de l'approbation est claire.

Une fois cette section terminée, vous devriez avoir une solution approuvée et reconnaissable comme référence sérieuse de Rostering.

## Examiner ce qui est bloqué et ce qui nécessiterait une nouvelle itération

Avant de fermer, vous devez être clair que valider une solution ne signifie pas que la possibilité de l'améliorer disparaît. Cela signifie que cette version spécifique est déjà fermée. Si vous avez besoin d'une amélioration ou d'un ajustement de fond par la suite, il sera bon d'ouvrir une nouvelle itération ou une nouvelle solution de travail, de ne pas modifier sans contrôle la version approuvée.

Avant de continuer, assurez-vous que:
1. La solution est déjà validée.
2. Tu sais quelles parties du travail ont été fermées.
3. Vous avez déjà compris que de futures améliorations devraient être définies comme de nouvelles itérations.

Pour clarifier la gouvernance après validation:
1. Il traite la solution validée comme une référence fermée.
2. Évitez de la modifier directement comme si elle restait un projet.
3. Si vous constatez une amélioration future:
   1. crée une nouvelle itération,
   2. ou ouvre un nouveau cycle de calcul et de révision.
4. Il conserve la version validée comme point de comparaison historique.
5. Si votre équipe doit vérifier les décisions, utilisez cette solution comme base de référence approuvée.

Pour le cas de référence, terminez cette section uniquement lorsque vous pouvez affirmer:
1. La version validée de L1 a été fermée.
2. Toute amélioration future se fera par une nouvelle itération.
3. La traçabilité entre calcul, révision et approbation est conservée.

Une fois cette section terminée, vous devriez être clair sur ce que signifie consolider une solution et sur la façon d'éviter de perdre le contrôle sur les versions.

## Laisser la solution prête pour le prochain niveau de processus

La dernière étape est de préparer mentalement la transition. A partir de là, la solution de Rostering n'est plus en phase de calcul technique, mais en phase d'utilisation, de consolidation ou de transfert au processus opérationnel suivant approprié.

Avant de finir, assurez-vous que:
1. Tu as validé la solution.
2. Tu l'as déjà traitée comme une référence consolidée.
3. Tu sais si l'étape suivante sera:
   1. communiquer,
   2. l'intégration,
   3. l'auditer,
   4. ou préparer une nouvelle itération future.

Pour fermer correctement cette quick start:
1. Vérifiez une dernière fois l'état de la solution.
2. Il confirme qu &apos; il ne s &apos; agit plus d &apos; un calcul provisoire.
3. Vérifiez que l'équipe pourrait identifier cette version comme approuvée.
4. Si votre processus l'exige, enregistrez la transition vers le niveau opérationnel suivant.
5. Conserve la solution comme référence stable pour une comparaison future.

Pour le cas de référence, ce quick start n'est terminé que lorsque vous pouvez affirmer:
1. La solution de Rostering de L1 est déjà validée.
2. Elle a déjà été consolidée en tant que référence approuvée.
3. L'étape suivante n'est plus de calculer, mais d'utiliser, de réviser ou d'évoluer cette base de manière contrôlée.

Une fois cette section terminée, vous devriez avoir une solution de Rostering validée, consolidée et prête à servir de référence stable pour le processus.

## Lectures supplémentaires

- [Gérer les versions et les itérations de la solution de Rostering](P28_Gestionando_versiones_e_iteraciones_de_la_solucion_de_Rostering.md)
