---
title: Validation de l'année opérationnelle avant planification
shortTitle: Année opérationnelle
intro: Apprenez à valider l'année d'exploitation de votre cas de planification afin
  d'éviter les failles, les chevauchements ou les coupures artificielles de données
  avant de passer au réseau, à l'infrastructure et aux services.
contentType: how-tos
versions:
- '*'
---
## Création ou validation de l'année d'exploitation qui utilisera votre planification

Avant de continuer avec le réseau, les temps, les services ou les règles, vous devez vérifier que la période que vous voulez planifier tombe dans le **l'année de fonctionnement correcte**. Dans GoalBus, l'année opérationnelle existe pour adapter la logique temporelle du système à la réalité des affaires. Ceci est important parce que beaucoup d'opérations ne suivent pas l'année civile de janvier à décembre. Par exemple, une opération scolaire peut travailler de septembre à août, et un contrat fiscal ou syndical peut avoir besoin d'un autre rang.

Utilisez ce quick start lorsque vous avez déjà défini la logique des types de jours et de jours fériés, lorsque vous voulez préparer votre premier cas de planification réelle, ou lorsque vous devez confirmer que la période que vous allez utiliser est supportée par une ligne temporelle valide.

Avant de commencer, assurez-vous que:
1. Tu as vérifié le rôle du planificateur en P1.
2. Vous avez déjà défini ou validé les types de jours fériés et de jours fériés en P2.
3. Tu sais exactement quelle période tu veux planifier.
4. Vous avez accès à l'environnement avec permission pour consulter ou modifier les paramètres temporaires.

Pour ce quick start, utilisez ce cas de référence:

> **Je vais planifier janvier 2026 et je dois confirmer que cette période tombe dans la bonne année opérationnelle avant de poursuivre ma première planification.**

Pour créer ou valider l'année d'exploitation de votre cas:
1. Dans GoalBus, allez à **Configuration**.
2. Ouvre la section **Gestion du temps** > **Années opérationnelles**.
ref: P3_Imagen1.png | compact
3. Vérifiez les années d'opération existantes et cherchez qui devrait couvrir la période que vous voulez planifier.
4. S'il n'y a pas d'année opérationnelle appropriée, cliquez sur l'option pour en créer un nouveau en cliquant sur **Créer une année opérationnelle**.
ref: P3_Imagen2.png | full
5. Définit un **Nom unique** et, si nécessaire, un **Description**.
6. Réglez la **Date de début** et la **Date de fin** pour les adapter à la réalité opérationnelle ou fiscale de votre affaire.
7. Associez les **Unités d &apos; affaires** s'il y en avait.
8. Garde l'année opérationnelle.
ref: P3_Imagen3.png | compact(x10)
9. Confirmez que la période que vous voulez planifier est entièrement couverte pour cette année.
10. Si l'année existait déjà, vérifiez également qu'elle est toujours la bonne pour votre cas et que ses dates ne suscitent aucun doute.

Quand vous aurez terminé cette section, vous auriez dû identifier ou créer l'année opérationnelle qui soutient vraiment votre cas de planification.

## En examinant la continuité temporelle et en évitant les vides ou les chevauchements

Après avoir identifié l'année d'exploitation correcte, vous devez vérifier que sa séquence temporelle est cohérente. Dans GoalBus, la continuité entre les années d'exploitation n'est pas facultative. Le système est conçu pour éviter qu'il n'y ait **lacunes** ou **Doublons** entre des années, car ces erreurs finiraient par affecter des métriques accumulées, des KPI annuelles et des calculs ultérieurs.

Avant de commencer cette section, assurez-vous que:
1. Tu as trouvé l'année d'opération qui devrait couvrir ton affaire.
2. Vous connaissez sa date de début et sa date de fin.
3. Tu sais s'il y a des années antérieures ou postérieures qui font partie de la même séquence.

Pour examiner la continuité temporelle de l'année opérationnelle:
1. Ouvre le détail de l'année d'exploitation que tu utiliseras comme référence.
2. Vérifiez le **Date de début** et le **Date de fin**.
3. Vérifiez si la période que vous voulez planifier tombe dans cette plage sans ambiguïté.
4. Vérifiez l'année opérationnelle précédente ou ultérieure, si elle existe, pour vous assurer qu'il n'y a pas:
   1. entre un an et l'autre; ou
   2. Des chevauchements entre deux plages temporelles.
5. Si vous avez besoin de créer une nouvelle année à la fin de la séquence, ajoutez-la à la fin et vérifiez qu'elle continue exactement là où se termine la précédente.
6. Si vous détectez une inconsistance, corrigez les dates avant de suivre.
7. Confirmez que le système permet d'enregistrer la séquence sans bloquer l'enregistrement par erreur de continuité.

Pour le cas de référence, posez-vous ces questions:
1. Un an de 2026 est-il complètement en cours d'année opérationnelle ?
2. Cette année-là est-elle connectée correctement avec l'année précédente et l'année suivante ?
3. Le système pourrait-il accumuler des données sans rompre la continuité de la période?

Quand tu auras terminé cette section, tu devrais être sûr qu'il n'y a pas d'écarts ou de chevauchements qui affectent ton affaire.

## Vérification de la relation entre l'année opérationnelle et la logique de calendrier

Maintenant que vous avez validé l'année opérationnelle et sa continuité, vous devez le connecter à ce que vous avez défini dans P2. Il ne sert à rien d'avoir des types de jours et des jours fériés bien configurés si le calendrier où ces données vivront n'est pas bien construit.

Avant de continuer, assurez-vous que:
1. La bonne année opérationnelle est déjà identifiée.
2. Les types de jours fériés et de jours fériés sont déjà configurés.
3. La période que vous prévoyez reste claire et courte.

Pour vérifier que l'année opérationnelle est déjà prête à soutenir la planification:
1. Vérifiez le cas de planification que vous avez défini au début de cet article.
2. Il confirme que cette période vit dans la bonne année opérationnelle.
3. Vérifiez que la logique de calendrier définie dans P2 s'applique également dans le même délai.
4. Demandez-vous si le système peut déjà être utilisé simultanément:
   1. la bonne catégorie de type de jour,
   2. les bons jours fériés; et
   3. la bonne année d'activité.
5. Si la réponse est oui, continuez avec le prochain quick start.
6. Si la réponse est non, corrigez l'année opérationnelle ou vérifiez la cohérence avec le calendrier avant de suivre.

À la fin de cette section, vous devriez pouvoir affirmer que votre affaire a une base temporelle complète: calendrier correct et année opérationnelle correcte.

## Lectures supplémentaires

- [Préparation du réseau principal: arrêts, lignes et itinéraires](P4_Définir_Les_Types_De_Véhicules_Et_De_Flotte_Autorisés_Par_Ligne.md)
