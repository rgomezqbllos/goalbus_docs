---
title: Publier le scénario à des dates précises
shortTitle: Publier la scène
intro: Apprenez à publier un scénario validé à des dates précises, à contrôler la
  solution opérationnelle et à maintenir une traçabilité entre planification, validation
  et déploiement opérationnel.
contentType: how-tos
versions:
- '*'
---
## Préparation du scénario validé avant publication

Après le calcul et la validation d'une solution, l'étape suivante est de décider **quand** doit entrer en vigueur dans l'opération réelle. Publier un scénario ne consiste pas seulement à l'approuver: il s'agit d'insérer cette solution validée dans le calendrier opérationnel pour des dates précises, sans la confondre avec un projet ni avec une version encore en cours de révision.

Utilisez ce quick start lorsque vous avez déjà un scénario avec une solution à l'état **Validationa** et que vous devez l'emmener à l'opération pour une période spécifique.

Avant de commencer, assurez-vous que:
1. Tu as déjà exécuté et validé la scène sur P15.
2. La solution du scénario que vous voulez publier est dans l'état **Validationa**.
3. Tu sais quelles dates précises tu veux couvrir.
4. Il est clair que publier change l'état opérationnel de la solution et la rend visible en tant que version implantée.

Pour ce quick start, utilisez ce cas de référence:

> **Je vais publier le scénario validé de la ligne L1 pour qu'elle entre en vigueur pendant une période ouvrable donnée sans affecter les solutions qui ne correspondent pas à ces dates.**

Pour préparer la publication du scénario:
1. Ouvre le module **Scénarios de planification**.
2. Localise la scène que tu as validée.
3. Vérifiez que l'état actuel de la solution est **Validationa**.
4. Vérifiez le nom de la scène, la ou les lignes incluses, le type de jour et la description.
5. Confirmez que vous êtes sur le point de publier exactement la bonne solution.
6. Si la scène n'est pas encore validée, retournez en arrière et terminez P15 avant de continuer.
7. Si le scénario est correct, continuez la publication.

Quand vous aurez terminé cette section, vous devriez avoir clairement identifié le scénario validé que vous voulez mettre en place.

## Sélectionner la fenêtre temporelle de publication

Une fois le scénario confirmé, vous devez décider de **à quelles dates**. La publication ne devrait pas être ambigue. Elle doit être claire de quand et jusqu'à quand cette solution sera la référence opérationnelle.

Avant de commencer cette section, assurez-vous que:
1. Tu as confirmé le scénario que tu vas publier.
2. Vous savez si la publication couvrira un jour, une semaine, une plage continue ou un bloc opérationnel plus long.
3. Vous savez déjà que la période choisie ne doit pas contredire le type de jour et la logique temporelle du scénario.

Pour sélectionner la fenêtre temporelle de publication:
1. Depuis le scénario validé, ouvre l'action **Publier**.
ref: P16_Imagen1.png | compact
2. Dans le formulaire de publication, il définit le **Classement des dates**.
3. Ajoutez d'autres **Rangs de date** si vous le pensez et publiez pour d'autres jours non sélectionnés (facultatif).
ref: P16_Imagen2.png | compact(x12)
4. Vérifiez que les dates ont un sens pour:
   1. le type de jour de la scène,
   2. la ou les lignes concernées,
   3. et la vraie fenêtre d'opération que tu veux couvrir.
5. Confirmez que vous ne laissez pas un rang trop large par erreur.
6. Si le scénario ne doit être appliqué qu'à court terme, il limite la fenêtre avec précision.
7. Confirmez la publication pour le ou les rang (s) de date choisi (s).

Pour le cas de référence, demandez-vous:
1. La publication couvre-t-elle exactement les jours ouvrables que je veux mettre en place ?
2. Est-ce que j'évite de publier plus de jours que nécessaire ?
3. La solution correspond-elle vraiment aux dates retenues?

Une fois cette section terminée, vous devriez avoir une fenêtre temporelle claire et contrôlée pour l'implantation.

## Confirmer la publication et changer l'état du scénario

Après avoir sélectionné la plage temporelle, vous devez confirmer l'action de publication. À ce stade, la solution cesse d'être seulement un scénario validé et devient un rôle opérationnel dans le calendrier.

Avant de continuer, assurez-vous que:
1. Tu as bien choisi les dates.
2. Tu as vérifié le scénario validé.
3. Tu es prêt à faire avancer la solution dans son cycle de vie.

Pour publier le scénario:
1. Regardez pour la dernière fois le résumé de la publication.
2. Confirme:
   1. le nom de la scène,
   2. le rang temporel,
   3. et le contexte opérationnel auquel elle s'appliquera.
3. Exécutez l'action **Publier**.
4. Vérifiez que l'état du scénario passe à **Publication** pendant que le système traite l'implantation.
5. Attends que le processus soit terminé.
6. Vérifiez que l'état final de la solution passe à **Publiée**.
ref: P16_Imagen3.png | compact
7. Si l'état ne change pas comme prévu, vérifiez s'il y a eu une incidence technique ou un problème d'éligibilité du scénario.

Pour le cas de référence, n'arrêtez pas la publication jusqu'à ce que vous puissiez affirmer:
1. La solution du scénario de L1 est déjà sortie de **Validationa**.
2. La plateforme a traité la publication.
3. La solution de l'état final du scénario est **Publiée**.

Une fois cette section terminée, vous devriez avoir un scénario déjà mis en place dans le calendrier opérationnel pour la période sélectionnée.

## Vérifiant que la solution publiée est celle qui est entrée en vigueur

Après publication, vous devez vérifier que la solution qui est devenue active est vraiment la bonne. Publier ne devrait pas être une étape aveugle. Vous devez être en mesure de vérifier quel scénario est resté en vigueur pour les dates choisies et de conserver une traçabilité sur la solution implantée.

Avant de commencer cette section, assurez-vous que:
1. La solution du scénario a déjà atteint l'état **Publiée**.
2. Tu sais les dates qu'il couvre.
3. Vous savez quel service ou ligne doit être affecté par la publication.

Pour vérifier l'implantation de la solution:
1. Retournez à la table principale des scénarios.
2. Filtre ou vérifie les scénarios par état.
3. Confirmez que la solution publiée sur le scénario apparaît sous **Publiée**.
4. Vérifiez vos dates d'application, si la vue le permet.
5. Vérifiez que vous ne confondez pas ce scénario avec un autre validé mais non implanté.
6. Si votre processus interne l'exige, enregistrez ou communiquez que cette version est déjà la solution opérationnelle en vigueur.
7. Il conserve le nom, la description et la plage temporelle comme base de traçabilité pour un audit ultérieur.

Dans le cas de référence, assurez-vous que:
1. Le scénario publié correspond à L1 ouvrable.
2. Les dates coïncident avec la période que vous vouliez mettre en place.
3. Aucun autre scénario n'a été activé par erreur.

Une fois cette section terminée, vous devriez être sûr de la solution qui est entrée en vigueur et pour quelle période exacte.

## Maintien de la traçabilité et préparation de l'itération suivante

Une fois que le scénario a été publié, le travail ne disparaît pas: il change de centre. Dès lors, la solution implantée peut devenir une référence pour l'audit, la comparaison ou une future itération. Il ne convient pas de réutiliser sans contrôle un scénario déjà publié pour expérimenter des changements structurels; la chose la plus sûre est de créer une nouvelle itération lorsque vous avez besoin de proposer une amélioration ou une variante.

Avant de finir, assurez-vous que:
1. La scène est déjà publiée.
2. Il est clair qu'il s'agit d'une plage temporelle.
3. Vous savez si la prochaine étape sera de vérifier les résultats ou de préparer une nouvelle itération.

Pour maintenir la traçabilité après publication:
1. Conserve le scénario publié avec un nom et une description suffisamment clairs.
2. Utilisez l'état **Publiée** comme référence pour le distinguer des scénarios dans le projet, le calcul ou la validation.
3. Si vous avez besoin de proposer une amélioration, créez un nouveau scénario au lieu de modifier la logique historique du scénario implanté.
4. Si votre équipe travaille avec une révision ultérieure, utilisez cette version publiée comme ligne de base de comparaison.
5. Tenez un registre interne de:
   1. qui a été publié,
   2. quand il a été publié,
   3. et à quelles dates est-il entré en vigueur.

Pour le cas de référence, ce quick start n'est terminé que lorsque vous pouvez affirmer:
1. La solution L1 est déjà publiée.
2. Tu sais exactement à quelle date c'était en vigueur.
3. Vous pouvez distinguer cette version publiée de toute autre itération future.

Une fois cette section terminée, vous devriez avoir une solution publiée, traçable et prête à servir de référence opérationnelle ou de point de départ d'une nouvelle itération.

## Lectures supplémentaires

- [Création d'une nouvelle itération du scénario à partir d'une solution publiée](iteracion-del-escenario)
