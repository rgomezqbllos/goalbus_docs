---
title: Définir les règles de véhicules pour Scheduling
shortTitle: Règles applicables aux véhicules
intro: Apprenez à configurer les règles de véhicules qui limiteront les solutions
  de flotte valides dans Scheduling, afin que le calcul respecte la réalité opérationnelle,
  l'infrastructure et l'offre validée.
contentType: how-tos
versions:
- '*'
---
## Préparation de la base d'utilisation des règles de véhicule

Avant d'activer les règles de véhicules, vous devez vérifier que la base que ces règles vont consommer est déjà prête. Les règles de véhicules ne remplacent pas une mauvaise paramétrage préalable. Leur fonction est d'affiner le comportement du calcul afin que le moteur rejette des combinaisons impossibles ou non désirées.

Utilisez cette quick start lorsque vous avez déjà une offre de service validée, une ligne avec flotte autorisée et une structure opérationnelle cohérente, et vous devez préparer le cas avant de créer le scénario de Scheduling.

Avant de commencer, assurez-vous que:
1. Vous avez déjà configuré la flotte autorisée par ligne sur P8.
2. Tu as déjà défini la version du temps et les temps de parcours en P9.
3. Tu as déjà créé et validé l'offre de service sur P10.
4. Vous avez vérifié la structure opérationnelle et l'état du service sur P11.
5. Vous savez quelle ligne et quel service vous utiliserez comme référence.

Pour ce quick start, utilisez ce cas de référence:

> **Je vais définir les règles des véhicules pour la ligne L1, de sorte que Scheduling n'utilise qu'une seule flotte compatible avec l'infrastructure, l'offre validée et les restrictions réelles du service.**

Pour préparer la base de l'affaire avant d'activer les règles:
1. Ouvre la ligne que tu utiliseras comme référence.
2. Vérifiez quels types de véhicules sont autorisés.
3. Vérifiez le dépôt ou le parking de l'opération.
4. Confirmez que le service que vous utiliserez comme entrée est déjà **Validation**.
5. Vérifiez que vous n'essayez pas de résoudre avec des règles un problème qui aurait dû être corrigé plus tôt en ligne, flotte ou infrastructure.
6. Si vous détectez une incohérence dans cette base, corrigez-la avant de passer à la configuration des règles.

Quand tu auras fini cette section, tu devrais être clair sur le cas réel que tu essaies de protéger avec les règles des véhicules.

## Création ou sélection du modèle de règles de véhicules

Une fois la base révisée, vous devez entrer dans le modèle ou catalogue de règles de véhicules. Il ne s'agit pas ici d'activer tout. Il s'agit de choisir ou de construire un ensemble de restrictions représentant la logique réelle du service.

Avant de commencer cette section, assurez-vous que:
1. Vous savez quel service validé vous utiliserez comme référence.
2. Tu as déjà confirmé les types de véhicules qui sont valables pour la ligne.
3. Tu sais quels vrais problèmes tu veux éviter.

Pour créer ou sélectionner le modèle de règles:
1. Dans GoalBus, vous voyez **Configuration** > **Véhicules** > **Règles applicables aux types de véhicules**.
ref: P12_Imagen1.png | compact
2. Vérifiez s'il existe déjà un modèle de règles adapté à votre cas.
3. Si le modèle existe déjà, ouvrez-le et vérifiez sa configuration.
4. S'il n'existe pas, créez un nouveau modèle de règles.
5. Assigne un **Nom** clair au modèle.
6. Si vous appliquez, ajoutez une **description** qui vous permettra de distinguer votre but.
7. Garde le modèle.
ref: P12_Imagen2.png | compact
8. Il confirme que le modèle est déjà disponible pour ajouter des règles spécifiques.

Dans le cas de référence, une option valable pourrait être:
- **Véhicules - L1 ouvrable**
- **Règles de flotte - Service ouvrable L1**

Quand tu auras fini cette section, tu devrais avoir un conteneur clair pour configurer les restrictions de véhicules dans le cas d'espèce.

## Activer seulement les règles de véhicules dont vous avez vraiment besoin

Maintenant, vous pouvez commencer à activer des règles. Ici, il est important de garder un critère clair: une règle doit représenter un besoin réel d'exploitation, de sécurité, d'infrastructure ou de conformité. Si une règle ne répond pas à un problème particulier, il ne convient pas de l'activer encore.

Avant de commencer cette section, assurez-vous que:
1. Vous avez déjà créé ou sélectionné un modèle de règles.
2. Tu sais quelle flotte est valable pour la ligne.
3. Vous savez quelles combinaisons devraient être interdites ou limitées.

Pour activer les règles de véhicule de l'affaire & #160;:
1. Dans le modèle de règles, consultez le catalogue de règles disponibles en cliquant sur **Ajouter une nouvelle règle**.
ref: P12_Imagen3.png
2. Identifiez ceux qui répondent aux besoins réels de votre service en sélectionnant le **Tableau d &apos; effectifs** correspondant.
3. Définit un **Nom** et écrit un **Description** pour chaque nouvelle règle.
4. Activez seulement les règles dont vous avez vraiment besoin pour l'affaire.
5. Configurez les paramètres spécifiques à chaque règle lorsque vous appliquez.
6. Répétez le processus jusqu'à ce qu'il couvre les restrictions minimales nécessaires.
7. Garde les changements.
8. Vérifiez le modèle complet et confirmez qu'il n'est ni très restrictif ni trop ouvert.

Pour le cas de référence, demandez-vous:
1. Quelles sont les situations de flotte qui devraient empêcher le système?
2. Quelles combinaisons seraient physiquement possibles mais non souhaitables ?
3. Quels comportements doivent être guidés par la logique du dépôt, du parking ou de la ligne?

Lorsque vous avez terminé cette section, vous devriez avoir un ensemble initial de règles de véhicules actives et cohérentes similaire à celle de l'image suivante:
ref: P12_Imagen4.png | compact(20x)

## Relation des règles avec la ligne, la flotte et l'infrastructure

Après avoir activé les règles, vous devez vérifier qu'elles sont réellement alignées sur la ligne et l'infrastructure qui soutiennent le cas. Une règle de véhicules ne devrait pas contredire la flotte autorisée par ligne ni la géographie des réservoirs et des parkings.

Avant de continuer, assurez-vous que:
1. Vous avez déjà activé l'ensemble initial de règles.
2. Tu as vérifié les types de véhicules autorisés.
3. Tu connais la base physique d'où sort l'opération.

Pour vérifier la cohérence des règles:
1. Vérifiez à nouveau la configuration de la ligne.
2. Il confirme que les règles ne contredisent pas les types de véhicules autorisés.
3. Vérifiez la relation avec le dépôt et le parking autorisé.
4. Il vérifie que les règles renforcent cette logique au lieu de la briser.
5. Si une règle rend impossible le service ou contredit l'infrastructure, corrigez-la ou désactivez-la.
6. Enregistrez la version finale du modèle.

Dans le cas de référence, assurez-vous que:
1. La ligne L1 peut toujours utiliser la flotte autorisée.
2. Le dépôt Nord reste une sortie cohérente pour le service.
3. Aucune règle ne bloque une opération qui devrait être valide selon la base déjà configurée.

Une fois cette section terminée, vous devriez avoir des règles alignées sur la réalité du service, pas sur un modèle abstrait ou générique.

## Confirmant que l'offre validée reste calculable

La dernière étape est de vérifier que les règles de véhicules que vous venez d'activer permettent toujours de calculer l'offre validée. Une chose est de restreindre avec critère, et une autre est de fermer à la fois le modèle que le service cesse d'être viable avant même de créer le scénario.

Avant de finir, assurez-vous que:
1. Tu as déjà activé les règles nécessaires.
2. Tu as vérifié sa relation avec la ligne, la flotte et l'infrastructure.
3. Tu sais déjà quel service sera l'entrée de Scheduling.

Pour valider que le cas reste calculable:
1. Vérifiez à nouveau le service validé que vous utiliserez comme référence.
2. Vérifiez que la ligne a toujours accès à la flotte dont vous avez besoin.
3. Vérifiez si les règles activées laissent au moins une solution raisonnable à l'affaire.
4. Demandez-vous si le système pourrait déjà créer un scénario de Scheduling sans être en contradiction.
5. Si la réponse est oui, continuez avec le prochain quick start.
6. Si la réponse est non, corrigez le modèle de règles avant de suivre.

Pour le cas de référence, ne continuez pas jusqu'à ce que vous puissiez affirmer:
1. La ligne L1 conserve une flotte valide et autorisée.
2. Le service ouvrable validé reste compatible avec les règles activées.
3. Le modèle de véhicule est déjà prêt à être utilisé dans le scénario de Scheduling.

Une fois cette section terminée, vous devriez pouvoir affirmer que la logique des véhicules est déjà fermée et qu'elle est suffisamment cohérente pour passer à la définition des règles de rotation et à la création du scénario.

## Lectures supplémentaires

- [Définir les types de gardes et les règles de garde](P13_Définir_Les_Types_De_Gardes_Et_Les_Règles_De_Garde.md)
