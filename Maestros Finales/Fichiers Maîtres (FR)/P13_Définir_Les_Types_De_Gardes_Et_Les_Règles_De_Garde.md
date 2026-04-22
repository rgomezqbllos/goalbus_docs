---
title: Définir les types de gardes et les règles de garde
shortTitle: Types et règles
intro: Apprenez à créer des types de rotations, à les organiser dans des modèles de
  règles et à activer les restrictions ou les sanctions nécessaires pour que Scheduling
  construise des tâches juridiquement valables et cohérentes sur le plan opérationnel.
contentType: how-tos
versions:
- '*'
---
## Création des types de gardes qui structureront le travail

Avant de configurer les règles de rotation, vous devez définir les **Types de rotations** que le système utilisera pour regrouper des voyages en travail humain cohérent. Un type de tour n'est pas seulement une étiquette visuelle. C'est la catégorie logique qui guide le moteur pour construire des tâches identifiables et ensuite utilisables dans les listes, l'opération quotidienne et l'intégration avec d'autres systèmes.

Utilisez ce quick start lorsque vous avez déjà une offre validée, une logique de véhicules définie et vous devez dire au système quelles formes de travail sont valables pour votre cas.

Avant de commencer, assurez-vous que:
1. Tu as déjà créé et validé l'offre de service sur P10.
2. Tu as validé la structure opérationnelle en P11.
3. Tu as déjà défini les règles des véhicules en P12.
4. Vous savez quel service et quel contexte opérationnel vous utiliserez comme référence.

Pour ce quick start, utilisez ce cas de référence:

> **Je vais définir les types de tours de la ligne L1 pour que Scheduling puisse construire des tâches cohérentes avant de créer le scénario de calcul.**

Pour créer les types de tours de votre cas:
1. Dans GoalBus, vous allez à **Configuration** > **Personnel** > **Types de roulement**.
ref: P13_Imagen1.png | compact
2. Vérifiez s'il y a déjà des horaires appropriés pour votre affaire.
3. Si le gars existe déjà, ouvrez-le et vérifiez s'il est toujours valide.
4. S'il n'existe pas, créez-en un nouveau.
5. Définit ces champs:
   1. **Nom complet**, avec un nom clair et descriptif.
   2. **Nom abrégé**, pour une vue compacte et des cartes opérationnelles.
   3. **ID externe**, si le client a besoin d'intégration avec des systèmes de RR. HH. ou de paie.
ref: P13_Imagen2.png | compact
6. Marquez le type comme **Actif** si vous devez participer à des calculs futurs.
7. Garde le type de garde.
8. Répétez le processus pour chaque catégorie de travail dont vous avez vraiment besoin dans votre cas.

Pour le cas de référence, vous pourriez créer des types tels que:
1. **Heure demain**
2. **Heure tardive**
3. **Heure du match**, si l'opération l'exige

Quand tu auras terminé cette section, tu devrais avoir les types de tours qui serviront comme       & #160; D & #160; ADN & #160; / & #160; Sheduling & #160; / & #160; Sheduling & #160; / & #160; Sheduling & #160; / & #160; Sheduling & #160; / & #160; Sheduling & #160; / & #160; Sheduling & #160; / & #160; Sheduling & #160; / & #160; / & #160; Sheduling & #160; / & #160; / & #160; Sheduling & #160; / & #160; / & #160; / & #160; Sheduling & #160; / & #160; / & #160; / & #160;!

## Création ou sélection du modèle de règles de rotation

Après avoir créé les types de tours, vous devez définir le conteneur où les règles vivront. Les règles de rotation ne sont pas gérées comme une liste plane, mais au sein de **modèles** qui regroupent un ensemble cohérent de restrictions pour un scénario, une période ou une simulation concrète. Cela permet de maintenir plusieurs configurations sans mélanger des règles historiques avec des règles actives.

Avant de commencer cette section, assurez-vous que:
1. Tu as déjà créé ou validé les types de gardes que tu vas utiliser.
2. Vous savez quel service ou simulation vous utiliserez comme référence.
3. Vous savez déjà si ce modèle sera réutilisable ou spécifique à l'affaire.

Pour créer ou sélectionner le modèle de règles:
1. Dans GoalBus, vous allez à **Configuration** > **Personnel** > **Règles de service**.
2. Vérifiez s'il existe déjà un **Modèle de règles** adapté à votre cas.
3. Si le modèle existe déjà, ouvrez-le et vérifiez s'il est toujours valide.
4. Si elle n'existe pas, créez un nouveau modèle en cliquant sur **Ajouter un nouveau modèle**.
5. Assigne un **Nom** clair au modèle.
6. Si vous appliquez, ajoutez un **Description** identifiant votre utilisation.
7. Garde le modèle.
ref: P13_Imagen3.png | compact
8. Confirmez que vous pouvez déjà ajouter des règles dans ce conteneur.

Dans le cas de référence, une option valable pourrait être:
- **Heures - L1**
- **Règles de service**

Une fois cette section terminée, vous devriez avoir un modèle de règles préparé pour recevoir des restrictions et des sanctions spécifiques.

## Activer les règles de rotation comme les restrictions ou les sanctions

Vous pouvez maintenant commencer à configurer les règles. Ici il est important de distinguer deux logiques:
1. **Restrictions**, qui sont obligatoires et bloquent les tâches non valides.
2. **Incriminations**, qui ne bloquent pas, mais poussent l'optimisation vers des solutions préférées.

Cette différence est essentielle parce que tout ce que vous voulez dans l'opération ne doit pas devenir une interdiction absolue. Certaines conditions doivent agir comme guide et non comme mur.

Avant de commencer cette section, assurez-vous que:
1. Vous avez déjà un modèle de règles créé ou sélectionné.
2. Tu sais quel comportement de travail tu veux empêcher.
3. Tu sais quel comportement tu veux favoriser sans le rendre obligatoire.

Pour gérer les règles de service de votre affaire:
1. Si vous souhaitez créer une nouvelle règle, cliquez sur **Ajouter une nouvelle règle**.
2. Dans le modèle de règles, vérifiez les **Modèles de règles** disponibles et donnez un **Nom** et un **Description** à la nouvelle règle.
3. Sélectionnez le modèle correspondant au contrôle que vous souhaitez appliquer.
4. Créez un **règle spécifique** à partir de ce modèle en cliquant sur **Confirmer**.
ref: P13_Imagen4.png | compact
6. Décide **à quels types de tours s'applique chaque règle**. Toutes les règles ne doivent pas s'appliquer à tous les types. Certaines peuvent être globales et d'autres doivent être adressées à des catégories spécifiques, comme demain, après-midi ou match.
7. Saisissez les paramètres spécifiques de la règle.
8. Garde la règle.
9. Répétez le processus uniquement pour les règles dont votre affaire a vraiment besoin.
10. Vérifiez si les règles que vous avez besoin d'appliquer sont actives ou non. Pour tailler une règle, vous devez avoir été assigné à au moins un type de tour.
ref: P13_Imagen5.png | compact(x19)

Pour le cas de référence, pensez à des exemples tels que:
1. Le service de demain doit commencer dans une fenêtre précise.
2. Un tour de match ne devrait pas dépasser un certain niveau d'ampleur.
3. Une séquence peu souhaitable peut être pénalisée au lieu d &apos; être interdite.

Une fois cette section terminée, vous devriez avoir un ensemble initial de règles qui reflète à la fois des limites obligatoires et des préférences opérationnelles.

## Vérifier que les règles sont attribuées au type de service correct

Une fois les règles activées, vous devez vérifier **à quels types de tours s'applique chacune d'elles**. Toutes les règles ne doivent pas s'appliquer à tous les types. Certaines peuvent être globales et d'autres doivent être adressées à des catégories spécifiques, comme demain, après-midi ou match.

Avant de continuer, assurez-vous que:
1. Vous avez déjà activé au moins une règle à l'intérieur du modèle.
2. Tu as déjà défini les types de gardes qui participent à l'affaire.
3. Tu sais si la règle doit être globale ou spécifique.

Pour vérifier correctement le champ d'application:
1. Sélectionnez chaque règle que vous avez créée.
2. Vérifiez la section **Types de roulement applicables**.
3. Sélectionnez les types particuliers auxquels la règle doit s'appliquer.
4. Si la règle doit affecter tous les types de scénario, configurez-la comme globale en sélectionnant **tous les types de service**.
5. Vérifiez qu'il n'y a pas deux règles actives du même modèle s'appliquant au même type de service si cela entraînerait un conflit logique.
6. Enregistre les paramètres.
7. Répétez la révision pour chaque règle du modèle.

Pour le cas de référence:
1. Une fenêtre de démarrage précoce ne peut être appliquée qu'à **Heure demain**.
2. Une règle de repos peut s'appliquer à plusieurs types.
3. Une préférence générale pourrait être globale.

Une fois cette section terminée, vous devriez avoir des règles avec un champ d'application clair et sans conflits logiques semblables à l'image suivante:
ref: P13_Imagen6.png | compact(x19)

## Vérifiant que la logique de rotation est toujours compatible avec le service

La dernière étape est de vérifier que les types de tours et les règles que vous venez de définir restent compatibles avec l'offre validée et avec la logique des véhicules que vous avez déjà fermés. Il ne sert à rien d'avoir des règles  &lt; &lt; Bonites &gt; &gt; , si le résultat laisse au service sans un moyen réaliste d'être programmé.

Avant de finir, assurez-vous que:
1. Tu as déjà créé les équipes nécessaires.
2. Tu as déjà activé et assigné les règles correspondantes.
3. Tu sais déjà quel service sera l'entrée de la scène de Scheduling.

Pour valider que le cas reste calculable:
1. Vérifiez le service validé que vous utiliserez comme référence.
2. Vérifiez que les types de gardes que vous avez créés peuvent organiser ce travail.
3. Vérifie s'il y a des règles de service qui rendent l'affaire trop rigide.
4. Vérifiez qu'il n'y a pas de contradiction forte avec les règles de véhicules déjà activées.
5. Demandez-vous si le système pourrait déjà construire des tâches légales et opérationnelles compatibles avec cette base.
6. Si la réponse est oui, continuez avec le prochain quick start.
7. Si la réponse est non, corrigez les types ou les règles avant de suivre.

Pour le cas de référence, ne continuez pas jusqu'à ce que vous puissiez affirmer:
1. L'offre validée de L1 reste compatible avec les types de tours définis.
2. Les règles ne bloquent pas inutilement l'affaire.
3. Le modèle est prêt à entrer dans la scène de Scheduling.

Quand vous aurez terminé cette section, vous devriez pouvoir affirmer que la logique des tours est déjà assez fermée pour passer à la création du scénario de Scheduling.

## Lectures supplémentaires

- [Création du premier scénario de Scheduling](P14_Création_Du_Premier_Scénario_De_Scheduling_Avec_Le_Moteur_Classic.md)
