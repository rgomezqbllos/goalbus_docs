---
title: Préparez les parkings et les dépôts pour l'opération
shortTitle: Parkings et dépôts
intro: Apprenez à configurer les parkings et les dépôts de manière cohérente afin
  que Scheduling puisse utiliser une infrastructure physique réaliste, minimiser le
  kilométrage vide et respecter la hiérarchie correcte des données.
contentType: how-tos
versions:
- '*'
---
## Configuration du réservoir comme structure opérationnelle et de relais

Avant de créer le parking, vous devez vérifier le **dépôt**. Dans GoalBus, le dépôt est la base opérationnelle de l'organisation et est le lien obligatoire pour les véhicules et les conducteurs. En outre, sa configuration sert non seulement à identifier l'unité, mais aussi à définir d'où peuvent commencer ou terminer les tours, y compris les en-têtes ou les terminaux autorisés qui permettent des relais efficaces et réduisent le kilométrage à vide.

Avant de commencer cette section, assurez-vous que:
1. Tu sais quel dépôt est responsable de la ligne ou du service que tu prépares.
2. Vous comprenez que le dépôt est l'entité principale et que le parking dépend de lui.
3. Tu as déjà créé tous les types de véhicules nécessaires à l'opération.

Pour créer ou valider le dépôt de votre cas:
1. Sous GoalBus, ouvre le module **dépôts**.
ref: P5_Imagen3.png | full
2. Cherche si le dépôt dont tu as besoin existe déjà.
3. Si le dépôt existe déjà, ouvrez-le et vérifiez sa configuration.
4. S'il n'existe pas, créez-en un nouveau.
ref: P5_Imagen4.png | compact(2x)
5. Définit ou valide ces champs:
   1. **Code** en tant qu'identificateur unique.
   2. **Nom court** pour une vue compacte.
   3. **Pourcentage de participation %** en tant que part du dépôt dans le total des opérations. Parmi tous les dépôts doivent être ajoutés à 100%.
   4. **Nom long** en tant que nom principal du dépôt.
   5. **ID externe**, si le client travaille avec des intégrations ERP ou RR. HH.
6. Ajoutez les **Arrêts de début et de fin autorisés**, comme les en-têtes ou les terminaux où des relais ou des fin de service sont autorisés.
7. Range le dépôt.
ref: P5_Imagen5.png | compact(8.5x)
8. Confirmez que le dépôt peut déjà soutenir opérationnellement l'affaire que vous construisez.

Dans le cas de référence, il vérifie que:
1. Le dépôt nord est le bon dépôt d'organisation.
2. Les en-têtes ou terminaux pertinents de la ligne L1 sont autorisés en tant qu'emplacements de démarrage ou de fin lorsqu'ils sont appliqués.

Une fois cette section terminée, vous devriez avoir un dépôt correctement identifié et lié à ses emplacements opérationnels autorisés.

## Configurer le parking comme nœud physique du réseau

Après avoir défini le dépôt et avant de passer à des voyages à vide, flotte ou règles de Scheduling, vous devez laisser le **parking** bien configuré qui tiendra votre cas. Dans GoalBus, un parking n'est pas seulement une étiquette administrative. C'est un nœud physique géolocalisé du réseau, et lorsque vous le créez, le système génère automatiquement un arrêt associé à ces coordonnées afin que le moteur puisse calculer des distances, des temps d'entrée et des temps de sortie de manière cohérente. En outre, chaque parking doit obligatoirement être lié à un dépôt organisationnel.

Utilisez cette quick start lorsque vous avez déjà créé le réseau de base et que vous devez connecter ce réseau à l'infrastructure physique réelle avant de continuer avec les déplacements et Scheduling.

Avant de commencer, assurez-vous que:
1. Vous êtes sûr de la ligne ou du service que vous allez utiliser comme cas de référence.
2. Tu sais de quelle base physique cette opération devrait sortir.
3. Tu as déjà configuré le ou les réservoirs d'exploitation.
4. Tu as déjà créé tous les types de véhicules nécessaires.

Pour ce quick start, utilisez ce cas de référence:

> **Je vais préparer le parking du dépôt Nord et valider que votre relation avec le dépôt et la ligne L1 est cohérente avant de continuer avec les voyages à vide et Scheduling.**

Pour créer ou valider le parking de votre cas:
1. Sous GoalBus, il ouvre le module **parkings** ou **parkings** dans l'infrastructure réseau.
ref: P5_Imagen1.png | full
2. Cherche si le parking dont tu as besoin existe déjà.
3. Si le parking existe déjà, ouvrez-le et vérifiez sa configuration.
4. Si le parking n'existe pas, créez-en un nouveau.
ref: P5_Imagen2.png | compact(2x)
5. Définit ou valide ces champs:
   1. **Code** comme identifiant court pour les vues compactes.
   2. **Nom court** pour une vue compacte.
   3. **Nom long** en tant que nom descriptif du garage ou de la cour.
   4. **Coordonnées** pour placer correctement le parking sur la carte.
   5. **ID externe**, si le client travaille avec des intégrations ERP ou RR. HH.
6. Vérifiez que le parking est lié au **dépôt** créé précédemment.
ref: P5_Imagen6.png | compact(8.5x)
7. Cliquez sur **Suivant** pour configurer la capacité du parking et les types de véhicules autorisés. Cela peut être modifié à l'avenir à mesure que les conditions changent.
ref: P5_Imagen7.png | compact(8.5x)
8. Vérifiez visuellement sur la carte que votre emplacement a un sens pour l'opération réelle.
9. Il confirme que le système peut déjà traiter ce parking comme source ou destination logistique de l'opération.

Une fois cette section terminée, vous devriez avoir un parking correctement géolocalisé et correctement subordonné au dépôt approprié.

## Validation de la cohérence entre le parking, le dépôt et la ligne

Maintenant que vous avez déjà configuré parking et dépôt, vous devez vérifier que cette infrastructure correspond à la logique de ligne et à l'efficacité logistique que GoalBus attend. Le modèle de ligne lui-même permet de définir **parkings ou dépôts autorisés** pour forcer le système à démarrer le service à partir des bases géographiquement correctes et à minimiser kilométrage à vide. Ce n'est pas une préférence cosmétique: guide directement le développeur quand il construit des solutions.

Avant de continuer, assurez-vous que:
1. Le parking est déjà lié au bon dépôt.
2. Le dépôt a déjà ses emplacements autorisés.

Pour valider la cohérence complète de l'infrastructure (si vous avez déjà une ligne):
1. Ouvre les paramètres de la **ligne** que vous utiliserez comme référence.
2. Vérifiez la section **parkings autorisés** ou **dépôts autorisés**.
3. Vérifiez que le bon dépôt est autorisé à démarrer les services de cette ligne.
4. Si le bon dépôt n'est pas autorisé, ajoutez-le.
5. Confirmez que vous ne laissez pas de dépôts qui n'ont aucun sens géographique pour cette ligne.
6. Vérifiez si le rapport entre ligne, dépôt et parking minimise la conduite sans revenu.
7. Confirmez que l'infrastructure physique que vous venez de préparer pourrait soutenir le service que vous créerez ou calculerez après.
8. Si vous détectez des incohérences, corrigez-les avant d'aller plus loin.

Pour le cas de référence, demandez-vous:
1. La ligne L1 est-elle autorisée à quitter le dépôt Nord ?
2. Ce dépôt utilise-t-il le Parking Nord comme base physique ?
3. La logique qui en résulte réduit des kilomètres à vide au lieu de les augmenter ?

Une fois cette section terminée, vous devriez pouvoir affirmer que la ligne, le dépôt et le parking forment une même logique opérationnelle et logistique.

## Lectures supplémentaires

- [Réseau enseignant](P6_Préparez_Le_Réseau_Principal_Avec_Des_Arrêts_Des_Lignes_Et_Des_Itinéraires.md)
