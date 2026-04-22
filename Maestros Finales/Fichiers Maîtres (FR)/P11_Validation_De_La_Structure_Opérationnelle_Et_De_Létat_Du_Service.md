---
title: Validation de la structure opérationnelle et de l'état du service
shortTitle: Structure opérationnelle
intro: Apprenez à vérifier les dépôts, les unités et les groupes d'exploitation, et
  à valider le service créé afin qu'il soit effectivement éligible à Scheduling avant
  de passer à des règles et à des calculs.
contentType: how-tos
versions:
- '*'
---
## J'examine la structure opérationnelle de votre service.

Avant de passer aux règles et au scénario de Scheduling, vous devez vérifier que votre offre existe non seulement, mais qu'elle est soutenue par une structure opérationnelle cohérente. À ce stade, vous devez vérifier si la ligne, le dépôt, l'unité opérationnelle et les groupes connexes appartiennent au même contexte d'affaires et d'exploitation.

Utilisez cette quick start lorsque vous avez déjà créé l'offre de service de base et vous devez confirmer que l'environnement organisationnel qui la soutient est correct avant de calculer.

Avant de commencer, assurez-vous que:
1. Tu as déjà créé l'offre de service sur P10.
2. Vous avez déjà configuré des parkings et des dépôts sur P6.
3. Vous avez déjà défini la flotte et les restrictions de base de ligne sur P8.
4. Vous savez quelle ligne et quel service vous utiliserez comme référence.

Pour ce quick start, utilisez ce cas de référence:

> **Je vais valider que la ligne L1, le dépôt Nord, l'unité opérationnelle associée et les groupes connexes forment une base cohérente avant d'apporter le service à Scheduling.**

Pour vérifier la structure opérationnelle de votre cas:
1. Ouvre la configuration ou la vue d'exploitation liée au service que vous venez de créer.
2. Identifiez ce que **dépôt** soutient le service.
3. Vérifiez que ce dépôt correspond à la base physique que vous avez définie plus tôt.
4. Vérifiez à quel **unité opérationnelle** appartient la ligne ou le service.
5. Vérifiez si cette unité correspond à l'infrastructure, à la géographie et à l'organisation de l'affaire.
6. Vérifiez les **groupes** connexes qui affectent ce contexte, s'ils existent.
7. Il confirme que la ligne, l'unité et le réservoir ne sont pas des structures incompatibles.
8. Si vous détectez une incohérence, corrigez-la avant d'aller plus loin.

Pour le cas de référence, vérifiez:
1. Que la ligne L1 est associée au dépôt Nord.
2. Que ce dépôt appartient à la bonne unité.
3. Que les groupes liés ne s'orientent pas vers un autre domaine opérationnel.

Quand vous aurez terminé cette section, vous devriez être sûr que l'offre de service vit dans une structure opérationnelle cohérente.

## Confirmant que le service est déjà validé et prêt pour la programmation

Après avoir examiné la structure opérationnelle, vous devez confirmer quelque chose de critique: le service créé en P10 est déjà en état **Validation**. Il ne suffit pas d'avoir créé des voyages, des intervalles et des itinéraires. Pour que Scheduling puisse lire le service et le considérer comme éligible, le service doit avoir passé par l'action de validation.

Avant de commencer cette section, assurez-vous que:
1. Tu as vérifié le service commercial et ses voyages sur P10.
2. Tu as vérifié les intervalles, les itinéraires et les durées.
3. Vous n'avez plus besoin de modifier le service à ce stade.

Pour confirmer que le service est prêt pour la programmation:
1. Ouvre le service commercial que tu utiliseras comme référence.
2. Vérifiez votre **État** actuel.
3. Si l'état est déjà **Validation**, confirmez qu'il n'y a rien en suspens avant de continuer.
4. Si le service est toujours en édition ou dans un état antérieur, exécutez l'action **Valider**.
5. Vérifiez que l'état change correctement.
6. Vérifie ce qui suit:
   1. le service n'est plus en projet,
   2. les voyages sont protégés contre les changements accidentels,
   3. et le service peut déjà être consommé par Scheduling.
7. Si vous détectez une erreur de structure, corrigez-la avant de la valider à nouveau.

Pour le cas de référence, ne continuez pas tant que vous ne pouvez pas affirmer:
1. La ligne L1 a déjà révisé son offre.
2. Le service a déjà changé à l'état **Validation**.
3. Le système peut déjà l'utiliser comme entrée de programmation.

Quand vous aurez terminé cette section, vous devriez avoir un service vraiment prêt à être lu par le moteur.

## Vérification de la cohérence entre la structure, le service et l'éligibilité

Maintenant, vous devez faire une dernière révision conjointe. L'objectif n'est pas seulement d'avoir un service validé, mais de confirmer que le service validé vit dans la bonne structure et qu'il n'entraîne pas des incohérences organisationnelles qui compliquent ensuite le calcul.

Avant de continuer, assurez-vous que:
1. Tu as vérifié l'entrepôt, l'unité et les groupes.
2. Tu as validé le service ou confirmé sa validation.
3. Tu sais quelle affaire tu vas mener à l'étape suivante.

Pour valider l'éligibilité complète avant Scheduling:
1. Vérifiez le service validé et confirmez quelle ligne vous utilisez.
2. Vérifiez que cette ligne est toujours liée au bon dépôt.
3. Vérifiez que l'unité opérationnelle et les groupes ne contredisent pas le contexte du service.
4. Demandez-vous si le système pourrait déjà prendre ce service comme une entrée valide et cohérente pour le calcul.
5. Si la réponse est oui, continuez avec le prochain quick start.
6. Si la réponse est non, corrigez la structure ou retournez le service en édition uniquement si vous avez besoin de refaire une partie de la base avant de la valider à nouveau.

Dans le cas de référence, assurez-vous que:
1. L1 appartient au contexte organisationnel correct.
2. Le dépôt Nord est vraiment la base qui soutient le service.
3. Le service ouvrable est déjà validé et n'a pas de contradictions avec sa structure.

Une fois cette section terminée, vous devriez pouvoir affirmer que l'offre n'est plus seulement créée, mais aussi structurellement alignée et éligible à Scheduling.

## Lectures supplémentaires

- [Définir les règles de véhicules pour Scheduling](P12_Définir_Les_Règles_De_Véhicules_Pour_Scheduling.md)
