---
title: Analyser et comparer les scénarios de Scheduling
shortTitle: Comparer les scénarios
intro: Apprenez à comparer les scénarios de Scheduling, à vérifier KPI et les différences
  opérationnelles, et à décider de la solution à retenir comme référence ou à avancer
  vers une nouvelle itération.
contentType: how-tos
versions:
- '*'
---
## En identifiant les scénarios que vous allez comparer

Après avoir créé, calculé, validé et publié des scénarios, l'étape suivante naturelle est de les comparer. Comparer les scénarios ne consiste pas seulement à voir ce qui est le mieux sorti d'une manière intuitive. Il s'agit de vérifier ce qui a changé, quel impact ce changement a eu et si la nouvelle itération améliore réellement la solution de référence.

Utilisez ce quick start lorsque vous avez déjà au moins deux scénarios comparables, par exemple une solution publiée et une nouvelle itération calculée, et vous devez décider de ce qui doit rester une référence opérationnelle ou de ce qui mérite d'avancer dans le cycle de vie.

Avant de commencer, assurez-vous que:
1. Tu as déjà créé et calculé au moins un scénario de base.
2. Vous avez déjà une deuxième version, itération ou variante à comparer.
3. Tu sais quelle ligne, quel genre de journée et quel contexte opérationnel tu regardes.
4. Vous savez quelle est la version de référence actuelle.

Pour ce quick start, utilisez ce cas de référence:

> **Je vais comparer le scénario publié de la ligne L1 à une nouvelle itération calculée pour décider si la nouvelle solution améliore réellement la programmation actuelle.**

Pour identifier correctement les scénarios à comparer:
1. Sous GoalBus, ouvre le module **Scénarios de planification**.
ref: P18_Imagen1.png | compact
2. Localisez le scénario qui agit comme référence actuelle.
3. Trouvez le nouveau scénario ou l'itération que vous voulez évaluer.
4. Vérifiez que les deux scénarios appartiennent au même contexte fonctionnel:
   1. la même ligne ou l'ensemble comparable de lignes,
   2. le même type de jour,
   3. même logique opérationnelle générale.
5. Vérifiez le nom, la description et l'état de chaque scène.
6. Confirmez ce qui suit:
   1. la version en vigueur ou publiée;
   2. et quelle est la nouvelle proposition.
7. Si les scénarios ne sont pas comparables les uns aux autres, ne continuez pas à corriger ce point.

Dans le cas de référence, assurez-vous que:
1. Les deux scénarios appartiennent à la ligne L1.
2. Les deux sont ouvrables ou répondent au même contexte temporel.
3. L &apos; un sert de référence et l &apos; autre d &apos; alternative.

Quand tu auras fini cette section, tu devrais avoir clairement identifié les scénarios que tu vas comparer et le rôle que chacun remplit.

## Révision de la KPI, de la charge de travail et de l &apos; équilibre général

Une fois les scénarios sélectionnés, vous devez commencer par une comparaison de haut niveau. Ici, l'objectif est de vérifier les indicateurs généraux avant d'entrer dans les détails des tâches ou des règles. Cette première comparaison vous aide à détecter si la nouvelle solution est vraiment mieux équilibrée ou si elle ne change que le résultat sans apporter de valeur réelle.

Avant de commencer cette section, assurez-vous que:
1. Tu sais quels sont les deux scénarios que tu vas comparer.
2. Tu as identifié la référence.
3. Vous avez déjà accès aux KPI visibles du scénario ou aux mesures comparables.

Pour examiner les KPI généraux des scénarios:
1. Ouvrez le premier scénario et vérifiez vos KPI principaux.
2. Note ou rappelle au moins:
   1. volume de travail total,
   2. nombre de tâches,
   3. temps total,
   4. distance ou magnitude opérationnelle pertinente,
   5. tout autre indicateur visible dans l'interface.
3. Ouvrez le deuxième scénario et vérifiez les mêmes KPI.
4. Comparez si la nouvelle itération:
   1. réduit la complexité inutile,
   2. amélioration de l'équilibre,
   3. ou déplace le problème d'un endroit à l'autre.
5. Il évite de donner pour une bonne itération uniquement parce qu'il change les nombres. L'important est que le changement ait un sens opérationnel.

Pour le cas de référence, demandez-vous:
1. La nouvelle itération réduit-t-elle les tâches inutiles ?
2. L'équilibre général semble-t-il plus raisonnable?
3. Le volume total reste-t-il cohérent avec l'offre validée?
4. L'amélioration est-elle réelle ou n'est-elle qu'une redistribution sans bénéfice évident?

Une fois cette section terminée, vous devriez avoir une lecture globale de la question de savoir si la nouvelle solution mérite un examen plus approfondi.

## Comparer l'impact sur les véhicules et les équipes

Après avoir examiné les KPI globaux, vous devez descendre à la logique fonctionnelle. À ce stade, la comparaison doit séparer deux choses:
1. l'impact sur **véhicules**,
2. et l'impact sur **Nombre d &apos; heures d &apos; attente**.

Ceci est important parce qu'une itération peut améliorer la logique de flotte et aggraver la logique des tours, ou à l'envers. Si vous mélangez les deux dimensions, la lecture devient confuse.

Avant de commencer cette section, assurez-vous que:
1. Tu as vérifié les KPI généraux.
2. Tu sais quelles règles de voiture et de service sont impliquées dans le changement.
3. Tu as déjà compris quel était le but de l'itération.

Pour comparer l'impact sur les véhicules:
1. Regardez comment la solution se comporte en ce qui concerne:
   1. flotte utilisée,
   2. compatibilités,
   3. des sorties de dépôts ou de parkings,
   4. et kilométrage non productif, s'il est visible ou déductible.
2. Vérifiez si l'itération améliore la cohérence entre ligne, flotte et infrastructure.
3. Il détecte si le nouveau scénario force des solutions qui étaient auparavant plus réalistes.

Pour comparer l'impact à tour de rôle:
1. Vérifiez comment les tâches ou les blocs de travail sont construits.
2. Vérifiez si les types de service actifs ont toujours un sens.
3. Notez si la nouvelle solution:
   1. améliore la clarté du travail,
   2. aggrave la structure,
   3. ou introduit des rigidités inutiles.
4. Relier le changement au modèle de règles de service que vous avez utilisé.

Pour le cas de référence, demandez-vous:
1. La nouvelle itération améliore-t-elle la logique des véhicules sans punir la logique des tours ?
2. La logique des rotations s'améliore-t-elle sans empirer la flotte ?
3. Laquelle des deux dimensions gagne ou perd ?
4. Le résultat global est-il plus robuste ou juste plus différent ?

Quand tu auras fini cette section, tu devrais comprendre où ça s'améliore et où chaque scénario s'aggrave.

## Décider si la nouvelle itération apporte une valeur réelle

Vous devez maintenant transformer la comparaison en une décision. Tout nouveau scénario ne mérite pas d'avancer. Parfois, une nouvelle itération ne sert qu'à l'apprentissage interne et la meilleure décision est de maintenir la version actuelle. D'autres fois, l'amélioration est suffisamment claire pour justifier un nouveau cycle de validation et de publication.

Avant de continuer, assurez-vous que:
1. Tu as déjà comparé la KPI générale.
2. Tu as déjà vérifié l'impact sur les véhicules et les équipes.
3. Tu sais quel était l'objectif originel de la nouvelle itération.

Pour décider si l'itération apporte une valeur réelle:
1. Résumez mentalement quel était le but du nouveau scénario.
2. Vérifie si cet objectif a été atteint de manière claire.
3. Demande-toi si l'amélioration est:
   1. opérationnellement visible,
   2. techniquement défendable,
   3. et suffisamment stable pour aller de l'avant.
4. Si l'itération améliore clairement la référence, préparez-la à la validation ou à la publication, selon le cas.
5. Si l'itération n'améliore pas la référence, gardez-la en tant qu'apprentissage et maintenez la version actuelle.
6. Ne promène pas une itération juste parce que c'est plus nouveau. Promène-la seulement si c'est mieux pour le cas.

Pour le cas de référence, terminez cette section seulement lorsque vous pouvez affirmer l'une de ces deux choses:
1. La nouvelle itération de L1 améliore clairement la solution publiée et mérite d'avancer.
2. La solution publiée reste la meilleure référence et l'itération nouvelle reste en tant qu'analyse.

Une fois cette section terminée, vous devriez avoir une décision claire et justifiable sur le scénario à retenir comme référence.

## Laisser la traçabilité de la comparaison pour les futures itérations

La dernière étape est de laisser une trace de la comparaison. Comparer les scénarios sans laisser de traçabilité oblige à répéter l'analyse à l'avenir et rend plus difficile d'expliquer pourquoi une version a été promue ou abandonnée.

Avant de finir, assurez-vous que:
1. Tu as déjà pris une décision sur la scène.
2. Tu sais ce qu'il reste comme référence.
3. Tu as déjà compris la raison principale de cette décision.

Pour permettre la traçabilité de la comparaison:
1. Vérifiez le nom et la description des deux scénarios.
2. Si nécessaire, mettez à jour la description du nouveau scénario afin de mieux refléter son but ou son résultat.
3. Conserve identifiée la version de référence comme:
   1. publiée,
   2. validée,
   3. ou maintenu comme base officielle.
4. Gardez l'itération non encouragée comme référence comparative si elle apporte une valeur historique.
5. Si votre processus interne l'exige, enregistrez ce qui a changé entre les deux scénarios et pourquoi la décision finale a été prise.

Dans le cas de référence, assurez-vous que:
1. Vous pouvez expliquer pourquoi le nouveau scénario s'améliore ou ne s'améliore pas à L1 en vigueur.
2. La décision est prise en compte dans les noms, descriptions ou processus internes.
3. L'itération suivante, si elle existe, ne partira pas d'une confusion.

Une fois cette section terminée, vous devriez avoir non seulement une comparaison faite, mais aussi une décision traçable et utile pour de futures itérations.

## Lectures supplémentaires

- [De Scheduling à Rostering](P19_De_Scheduling_À_Rostering.md)
