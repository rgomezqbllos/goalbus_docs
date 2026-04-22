---
title: Définir les règles de Rostering pour l'affectation du personnel
shortTitle: Règles de Rostering
intro: Apprenez à configurer les règles de base et avancées de Rostering afin que
  l'affectation du personnel respecte les limites de travail, les critères d'équité
  et les restrictions opérationnelles réelles avant de calculer le personnel.
contentType: how-tos
versions:
- '*'
---
## Je comprends ce que les règles de Rostering contrôlent.

Avant de calculer les affectations de personnel, vous devez définir les **règles de Rostering** qui guideront la façon dont les employés sont affectés aux équipes. Ces règles ne construisent pas le travail, parce que cette étape a déjà été réglée par Scheduling. Ici, vous faites c'est de contrôler la répartition de ce travail entre les personnes réelles, dans le respect des politiques opérationnelles, des critères d'équité et des limites de travail.

Utilisez cette quick start lorsque vous avez déjà une solution de Scheduling suffisamment stable, un modèle de conducteur chargé et un détachement opérationnel déjà révisé.

Avant de commencer, assurez-vous que:
1. Tu as déjà fermé la transition depuis Scheduling sur P19.
2. Tu as déjà chargé et vérifié les chauffeurs sur P20.
3. Tu as validé l'adscription opérationnelle sur P21.
4. Tu sais déjà quelle solution Scheduling va servir de base.
5. Vous savez quel groupe ou groupe d'employés sera affecté par le calcul.

Pour ce quick start, utilisez ce cas de référence:

> **Je vais configurer les règles de Rostering pour la ligne L1 et son groupe de conducteurs, de sorte que le calcul assigne du personnel réel dans le respect des pauses, des limites de travail et des critères opérationnels.**

Pour comprendre le rôle de ces règles:
1. Il traite les règles de Rostering comme des restrictions et des préférences sur l'affectation des personnes.
2. Utilisez ces règles quand vous voulez contrôler:
   1. pauses,
   2. temps de travail,
   3. modèles hebdomadaires,
   4. groupe de travail,
   5. les correspondances,
   6. et d &apos; autres critères d &apos; équité ou de politique intérieure.
3. N'utilisez pas ces règles pour corriger les problèmes de:
   1. offre,
   2. temps,
   3. flotte,
   4. ou construction de base de tours.
4. Si vous constatez que le problème reste structurel, retournez à Scheduling avant de continuer.

Quand tu auras fini cette section, tu devrais être sûr que les règles de Rostering gouvernent les gens et non la structure de base du travail.

## Distinction entre les règles de base et les règles avancées

Avant de créer un modèle de règles, vous devez distinguer deux niveaux de configuration:
1. **Règles de base**
2. **Règles avancées**

Les règles de base sont conçues pour configurer rapidement les restrictions communes. Elles sont utiles lorsque vous voulez une paramétrage agile ou un test initial. Les règles avancées sont conçues pour modeler avec plus de précision des restrictions et des préférences par des limites et des pénalités.

Avant de commencer cette section, assurez-vous que:
1. Tu sais si ton affaire a besoin de rapidité ou de précision.
2. Vous comprenez que les règles de base ont moins de flexibilité de modélisation que les règles avancées.
3. Tu sais si tu vas avoir besoin de modèles différents selon l'utilisation.

Pour choisir le type de règles approprié:
1. Utilisez **règles de base** pour couvrir rapidement les restrictions courantes.
2. Utilisez **règles avancées** si vous avez besoin de façonner des politiques complexes, des conventions ou des conditions opérationnelles spécifiques.
3. Notez que les règles de base actives s'appliquent aussi bien aux opérations quotidiennes que dans les scénarios de calcul de l'allocation.
4. Si vous avez besoin de modèles différents pour différents contextes, par exemple pour une opération quotidienne et un autre pour un calcul futur, travaillez avec des règles avancées.
5. Décidez de l'approche que vous utiliserez avant de commencer à paramétrer.

Pour le cas de référence, utilisez cette logique:
1. Si vous commencez et que vous voulez une première couche de contrôle, commencez par des règles de base.
2. Si vous savez déjà que vous aurez besoin d'ajuster des préférences, des pénalités ou des modèles par contexte, continuez avec des règles avancées.

Quand vous aurez terminé cette section, vous devriez savoir si votre affaire sera résolue par des règles de base, avancées ou une combinaison contrôlée des deux.

## Activer les règles de base les plus courantes pour une première affectation

Si votre cas nécessite une configuration initiale rapide, vous pouvez commencer par les **règles de base**. Celles-ci couvrent les restrictions les plus courantes et permettent de lancer le calcul avec une base raisonnable avant d'entrer dans des niveaux de contrôle plus fins.

Avant de commencer cette section, assurez-vous que:
1. Tu as décidé de commencer par des règles de base.
2. Tu sais quelles restrictions minimales tu veux imposer.
3. Il est clair que toutes les règles ne doivent pas être activées par défaut.

Pour activer les règles de base & #160;:
1. Dans GoalBus, vous allez à **Configuration** > **Règles d &apos; attribution**.
ref: P22_Imagen1.png | compact
2. Ouvre la section **Règles de base**.
3. Regardez le catalogue des règles de base disponibles.
ref: P22_Imagen2.png | full
4. Activez seulement celles qui correspondent à l'affaire que vous construisez.
5. Configuration, lorsque vous appliquez:
   1. limites générales,
   2. limites spécifiques pour les propriétés d'employé,
   3. ou des exceptions pour certains employés.
6. Garde les changements.
7. Vérifiez que les règles actives reflètent vraiment les politiques que vous voulez imposer.

Une base initiale de règles de base peut inclure:
1. **Modèle de travail**
2. **Repos entre les jours**
3. **Temps de travail mensuel**
4. **Temps de travail hebdomadaire**
5. **Jour de congé par semaine**
6. **Première solution publiée**
7. **Groupe de travail**
8. **Eparpillement**
9. **Compatibilité de l'attribution**
10. **Activation de la ligne**
11. **Heure de Première Solution Postée**
12. **Jours de travail consécutifs**, lorsque vous appliquez

Pour le cas de référence, n'activez pas une règle uniquement parce qu'elle existe. Activez-la uniquement si:
1. répond à un besoin réel,
2. Tu peux expliquer pourquoi tu en as besoin.
3. Et tu sais comment ça affectera l'affectation.

Quand tu auras fini cette section, tu devrais avoir une première base de contrôle pour l'affectation du personnel.

## Création d'un modèle de règles avancées lorsque vous avez besoin de plus de précision

Si les règles de base ne suffisent pas, l'étape suivante consiste à créer un **modèle de règles avancées**. Cette approche vous permet de contrôler avec précision la façon dont les affectations sont générées, en ajustant les limites et les préférences selon les politiques d'entreprise, les accords de travail et les conditions réelles d'exploitation.

Avant de commencer cette section, assurez-vous que:
1. Tu as déjà identifié la partie de l'affaire qui ne peut pas être réglée avec des règles de base.
2. Vous savez quels comportements doivent être obligatoires et quels sont ceux que vous préférez seulement.
3. Vous avez déjà besoin d'un modèle plus fin qui puisse être réutilisé par scénario ou par contexte.

Pour créer un modèle de règles avancées:
1. Sous **Configuration** > **Règles d &apos; attribution**, ouvre la section **Modèles de règles**.
2. Créez un nouveau modèle de règles.
3. Assigne un **Nom** clair au modèle.
4. Ajoutez un **description** qui vous permettra de le distinguer d'autres modèles.
5. Garde le modèle.
ref: P22_Imagen3.png | compact
6. Commencez à ajouter des règles avancées une par une.
7. Pour chaque règle, décide:
   1. s'il agit comme une limite obligatoire,
   2. ou s'il agit comme une préférence par incrimination.
8. Enregistre la configuration du modèle.
9. Activez le modèle de règles créé.
10. Vérifiez que le modèle peut déjà être attribué au calcul de Rostering approprié.

Dans le cas de référence, une option valable pourrait être:
- **Rostering L1 ouvrable**
- **Affectation des conducteurs L1 - règles avancées**

Une fois cette section terminée, vous devriez avoir un modèle avancé prêt à représenter des contraintes et des préférences plus complexes.

## En reliant les règles au bon collectif et au calcul réel

Après avoir activé des règles de base ou créé un modèle avancé, vous devez vérifier que les règles s'appliquent au bon collectif et que vous n'imposez pas des restrictions abstraites sans rapport avec le calcul réel.

Avant de continuer, assurez-vous que:
1. Vous avez déjà activé des règles de base ou créé un modèle avancé.
2. Vous savez quels employés, groupes ou dépôts participeront au calcul.
3. Tu sais déjà quelle solution Scheduling va servir d'entrée.

Pour relier correctement les règles au contexte de calcul:
1. Vérifiez le personnel auquel Rostering s'appliquera.
2. Vérifiez si les règles concernent:
   1. à l'ensemble du personnel concerné,
   2. à un groupe spécifique,
   3. ou à des employés ayant des propriétés particulières.
3. Confirme que tu n'imprimes pas de règles sur les personnes qui ne participeront même pas à ce calcul.
4. Vérifiez si la logique du scénario de Scheduling est toujours compatible avec ces règles.
5. Si une règle rend la répartition du travail impossible, elle ajuste sa limite ou son champ d'application.
6. Enregistrez la version finale de la configuration.

Pour le cas de référence, demandez-vous:
1. Ces règles sont-elles conçues pour les conducteurs qui vont réellement couvrir L1 ?
2. Le groupe de travail concerné est-il correct ?
3. L'affectation reste-t-elle viable après l'activation de ces règles ?

Une fois cette section terminée, vous devriez avoir une configuration de règles reliée à des personnes réelles et un calcul de Rostering spécifique.

## Confirmant que la base de règles est déjà prête à calculer Rostering

La dernière étape est de vous assurer que votre configuration est déjà prête à alimenter le calcul du personnel. Il ne s'agit pas seulement d'avoir activé des règles, mais d'avoir laissé une base cohérente, compréhensible et applicable.

Avant de finir, assurez-vous que:
1. Tu as déjà choisi entre les règles de base et les règles avancées selon le cas.
2. Vous avez déjà activé ou modelé les restrictions nécessaires.
3. Tu as déjà lié la logique au bon collectif.
4. Tu as vérifié que l'affectation est toujours possible.

Pour valider que la base de règles est déjà prête:
1. Vérifiez l'ensemble final de règles actives.
2. Elle confirme que chacune répond à un besoin réel.
3. Demandez-vous si le système pourrait déjà:
   1. bloquer les affectations non valides,
   2. respecter les pauses et les limites,
   3. refléter les critères d'équité et de groupe de travail,
   4. et de continuer à générer une solution utilisable.
4. Si la réponse est oui, continuez avec le prochain quick start.
5. Si la réponse est non, ajustez les règles avant de suivre.

Pour le cas de référence, ne continuez pas jusqu'à ce que vous puissiez affirmer:
1. Les règles de Rostering pour L1 sont déjà claires.
2. Tu sais pourquoi tu as activé chaque règle.
3. Le système peut encore assigner des personnes réelles avec cette configuration.
4. La base est déjà prête à traiter de la disponibilité et des exceptions de personnel.

Une fois cette section terminée, vous devriez avoir une base de règles de Rostering suffisamment solide pour passer au traitement des absences, des inactivités et de la disponibilité.

## Lectures supplémentaires

- [Gérer les absences, les inactivités et la disponibilité du personnel](P23_Gérer_Les_Absences_Les_Inactivités_Et_La_Disponibilité_Du_Personnel.md)
