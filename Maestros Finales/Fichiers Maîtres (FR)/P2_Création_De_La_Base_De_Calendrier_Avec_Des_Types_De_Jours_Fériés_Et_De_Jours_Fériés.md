---
title: Création de la base de calendrier avec des types de jours fériés et de jours
  fériés
shortTitle: Types de jours fériés et de jours fériés
intro: Apprenez à configurer les types de jour et de jours fériés pour que la logique
  de planification applique le bon schéma opérationnel avant de passer à des itinéraires,
  des temps de voyage et de création de services.
contentType: how-tos
versions:
- '*'
---
## Créant le type de jour que vous utiliserez pour planifier

Avant de créer des services ou de lancer des calculs de planification, vous devez définir la logique de calendrier qui dit au système avec quel type de jour vous travaillez. Dans GoalBus, les types de jour sont les catégories opérationnelles qui regroupent des jours comme ouvrables standard, vendredi, week-end ou jours spéciaux, afin que vous n'ayez pas à construire la logique de planification date par date.

Utilisez ce quick start lorsque vous préparez votre premier cas de planification, lorsque vous devez créer ou valider le type de jour que votre scénario utilisera, ou quand vous voulez vous assurer que la logique des fêtes est prête avant de continuer.

Avant de commencer, assurez-vous que:
1. Vous avez accès à l'environnement avec permission pour afficher ou modifier les paramètres de calendrier.
2. Tu sais quelle affaire de planification tu veux construire.
3. Vous savez quelle période vous voulez préparer, par exemple janvier 2026.
4. Tu as vérifié ton rôle de planificateur et le flux global sur P1.

Pour ce quick start, utilisez ce cas de référence:

> **Je prépare la base de calendrier pour un scénario ouvrable de janvier 2026, y compris le comportement correct des fêtes.**

Pour créer ou valider le type de jour de votre cas:
1. Dans GoalBus, vous allez à **Configuration** > **Gestion du temps** > **Gestion des types de jour**.
ref: P2_Imagen1.png | compact
2. Vérifiez les types de jour existants et vérifiez s'il y en a déjà un qui représente la logique opérationnelle dont vous avez besoin.
3. S'il existe déjà un type de jour approprié, il confirme que:
   1. Son nom est clair.
   2. Son nom court est clair.
   3. Il représente vraiment le modèle opérationnel dont vous avez besoin.
4. En l'absence d'un type de jour approprié, cliquez sur **Créer un type de jour**.
ref: P2_Imagen2.png | compact(2x)
5. Définit le **Nom** et le **Nom court** du nouveau type de jour.
ref: P2_Imagen3.png | compact(8.5x)
6. Choisissez les jours de la semaine qui s'appliquent à ce type de jour.
ref: P2_Imagen4.png | compact(8.5x8)
7. Si le type de jour doit également s'appliquer aux jours fériés, activez l'option pour appliquer le type de jour férié.
ref: P2_Imagen5.png | compact(8.5x8)
8. Garde le genre de jour.
9. Vérifiez le résultat et confirmez que le type de jour représente maintenant clairement l'affaire que vous préparez.

Une fois cette section terminée, vous devriez avoir un type de jour que le système peut utiliser comme catégorie opérationnelle pour votre cas de planification.

## Enregistrer les jours fériés qui modifient la logique normale du calendrier

Après avoir défini le type de journée générale, vous devez indiquer au système ce que vous devez faire avec les dates exceptionnelles. Les jours fériés sont importants parce que le calendrier peut dire qu'une date est mardi, tandis que l'opération devrait se comporter comme un dimanche ou comme un autre motif spécial. Si vous ne enregistrez pas bien les jours fériés, le système peut appliquer le mauvais plan lorsque vous publiez ou calculez ultérieurement des scénarios.

Avant de commencer cette section, assurez-vous que:
1. Tu as déjà créé ou confirmé le genre de jour que ton affaire va utiliser.
2. Tu sais si la période de planification comprend des jours fériés ou des dates spéciales.
3. Vous êtes prêt à décider quel modèle opérationnel doit suivre chaque jour férié.

Pour enregistrer et valider les jours fériés de votre cas:
1. Dans la même section de gestion des types de jour, passez à l'onglet **Jours fériés**.
ref: P2_Imagen6.png | compact
2. Vérifie si le jour férié dont tu as besoin existe déjà dans le système.
3. Si le jour férié n'existe pas, créez un nouveau registre des jours fériés.
4. Si le jour férié existe déjà, ouvrez-le et vérifiez sa configuration.
5. Saisissez ou confirmez le **Nom** du jour férié.
6. Assigne le **type de jour** correct à ce jour férié.
ref: P2_Imagen7.png | compact
7. Garde le registre du jour férié.
8. Répétez ce processus pour tout autre jour férié qui affecte la période que vous préparez.
9. Vérifiez la liste des jours fériés et confirmez que chaque date exceptionnelle indique le bon schéma opérationnel.

Pour le cas de référence, posez-vous ces questions:
1. Un an de 2026 inclut-il des jours fériés qui doivent se comporter différemment d'un jour férié standard?
2. Ce jour férié devrait-il se comporter comme un dimanche, comme un samedi ou comme une autre journée spéciale ?
3. Si vous publiiez un scénario pour cette période, le système saurait-il exactement quel modèle appliquer à cette date?

Une fois cette section terminée, le système devrait pouvoir remplacer le comportement normal du calendrier aux dates festives importantes pour votre cas.

## Vérifier que votre base de calendrier est prête à planifier

Maintenant que vous avez défini le type de journée générale et les exceptions pour les jours fériés, vous devez confirmer que la base de calendrier est réellement utilisable. C'est l'étape dans laquelle vous vérifiez que la structure que vous avez créée peut soutenir les quick starts suivants sans introduire d'erreurs évitables.

Avant de continuer, assurez-vous que:
1. Le type de jour existe et a la bonne logique hebdomadaire.
2. Les jours fériés pertinents sont enregistrés.
3. Chaque jour férié est lié au type de jour correct.
4. Votre cas de planification reste clair et concret.

Pour valider votre base de calendrier avant de passer au quick start suivant:
1. Vérifiez le cas de planification que vous avez défini au début de cet article.
2. Confirmez que le type de jour que vous avez créé ou validé correspond à cette affaire.
3. Il confirme que tout jour férié au cours de la période de planification a été enregistré et associé au type de jour correct.
4. Vérifiez si l'option d'application aux jours fériés que vous activez dans le type de jour reflète vraiment le comportement que vous voulez.
5. Demandez-vous si le système pourrait déjà distinguer:
   1. les jours normaux de la période; et
   2. les dates exceptionnelles à suivre par un autre modèle opérationnel.
6. Si la réponse est oui, continuez avec le prochain quick start.
7. Si la réponse est non, retournez en arrière et corrigez le type de jour ou l'association de jours fériés avant de suivre.

À la fin de cette section, vous devriez pouvoir affirmer que votre cas de planification a une base de calendrier fiable et que les quick starts suivants pourront s'appuyer sur elle sans hériter d'une erreur de logique temporelle.

## Lectures supplémentaires

- [Validation de l'année opérationnelle avant planification](P3_Validation_De_Lannée_Opérationnelle_Avant_Planification.md)
