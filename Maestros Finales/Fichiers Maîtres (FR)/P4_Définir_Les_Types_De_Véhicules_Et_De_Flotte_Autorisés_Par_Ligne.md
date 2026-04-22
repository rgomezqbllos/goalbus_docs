---
title: Définir les types de véhicules et de flotte autorisés par ligne
shortTitle: Flotte par ligne
intro: Apprenez à configurer les types de véhicules et les restrictions de flotte
  autorisées par ligne pour que GoalBus bloque les affectations impossibles, respecte
  les limites physiques et environnementales, et préparez une base cohérente avant
  de définir les temps et les services.
contentType: how-tos
versions:
- '*'
---
## Définir les types de véhicules autorisés pour une ligne

Dans GoalBus, cette restriction n'est pas décorative: elle agit comme un filtre de sécurité, de conformité et de faisabilité physique. L'objectif est d'empêcher le système de proposer un véhicule qui ne s'arrête pas dans une rue, qui viole une restriction environnementale ou qui ne devrait pas circuler dans ce service.

Utilisez ce quick start quand vous devez fermer la base de flotte qui utilisera votre cas avant de définir les temps et l'offre de service.

Avant de commencer, assurez-vous que:
1. Vous savez quelle ligne vous utiliserez comme référence.
2. Tu sais, au moins au niveau de base, quelles restrictions physiques ou environnementales affectent cette ligne.

Pour ce quick start, utilisez ce cas de référence:

> **Je vais définir quels types de véhicules peuvent fonctionner la ligne L1 pour m'assurer que ma première planification n'utilise qu'une seule flotte conforme à la réalité physique et réglementaire du service.**

Pour définir les types de véhicules autorisés dans votre cas:
1. Dans GoalBus, si une ligne existe déjà, ouvrez les paramètres de la **ligne** que vous utiliserez comme référence.
2. Cherche la section **Types de véhicules autorisés**.
3. Vérifiez si la ligne a déjà des gars assignés.
4. Si la ligne a déjà des types définis, confirmez qu'ils sont toujours corrects pour le cas.
5. Si elles ne sont pas encore définies, vérifiez d'abord si le **type de véhicule** dont vous avez besoin existe déjà dans la configuration générale des véhicules.
6. Si le type **Oui, c'est vrai.**, sélectionnez-le comme permis pour cette ligne.
7. Si le type **n &apos; existe pas**, sortez de la configuration de la ligne et allez à la configuration générale de **véhicules** pour créer ou compléter d'abord le catalogue de types disponible à partir du panneau **Types de véhicules**.
ref: P4_Imagen1.png | full
8. Créez le type de véhicule dont vous avez besoin en utilisant une catégorie claire et compréhensible pour les affaires, par exemple:
   1. Minibus
   2. Standard électrique
   3. Diesel articulé
ref: P4_Imagen2.png | compact(2x5)
9. Garde le nouveau type de véhicule.
ref: P4_Imagen3.png | compact(x9)
10. Retournez à la configuration de la ligne.
11. Marque les types de véhicules spécifiques qui sont autorisés à fonctionner sur cette ligne.
ref: P4_Imagen4.png | compact(8x)
12. Laisse les gars qui n'ont pas besoin d'opérer ce service.
13. Enregistre les paramètres.
14. Revoit la ligne (si elle existe déjà) et confirme que le filtre représente déjà correctement la réalité opérationnelle.

Pour le cas de référence, demandez-vous:
1. La ligne L1 prend-elle en charge un bus standard, un minibus ou les deux ?
2. Y a-t-il un type de véhicule qui doit être exclu par taille ou environnement?
3. S'il n'y avait pas le gars dont tu avais besoin, tu l'as créé avant d'essayer de l'attribuer à la ligne ?
4. Le système devrait-il bloquer une affectation manuelle si vous essayez d'utiliser un véhicule non autorisé?

Lorsque vous aurez terminé cette section, vous devrez avoir défini une restriction de flotte par ligne qui servira déjà de base pour le calcul ultérieur.

## En reliant la ligne aux dépôts ou parkings autorisés

Après avoir défini la flotte qui va ou ne va pas dans la ligne, vous devez vérifier à partir de quelles bases physiques ce service peut sortir. GoalBus permet de définir **parkings ou dépôts autorisés** par ligne pour forcer le système à démarrer le service depuis des emplacements géographiquement corrects et à réduire le kilométrage à vide.

Avant de commencer cette section, assurez-vous que:
1. Tu as déjà configuré les types de véhicules autorisés de la ligne.
2. Tu sais à partir de quelle base opérationnelle le service devrait vraiment commencer.

Pour relier la ligne à vos dépôts ou parkings autorisés:
1. Dans la même configuration de la ligne, localisez la section **Parkings autorisés** ou **Dépôts autorisés**.
2. Vérifiez si la ligne a déjà des dépôts autorisés.
3. Choisissez uniquement les dépôts ou les automobilistes qui sont autorisés géographiquement pour démarrer les services de cette ligne.
4. Laisse tomber les bases qui n'ont aucun sens opérationnel pour ce coureur.
5. Enregistre les paramètres.
6. Vérifiez que la ligne a maintenant une logique de sortie cohérente à partir de la base la plus raisonnable.

Dans le cas de référence, il constate que:
1. La ligne L1 peut sortir du dépôt nord.
2. Le parking principal associé est le bon.
3. Vous ne laissez pas un dépôt lointain vous forcer à parcourir de nombreux kilomètres à vide pour commencer le premier voyage.

Une fois cette section terminée, vous devriez avoir aligné la ligne (si elle existe déjà), la flotte autorisée et la géographie de départ du service.

## Validant que la ligne a déjà une base de flotte cohérente

Maintenant que vous avez défini les types de véhicules autorisés et les réservoirs ou parkings autorisés, vous devez faire une validation finale.

Avant de continuer, assurez-vous que:
1. La ligne a déjà des types de véhicules autorisés.
2. Si le type de véhicule requis n'existait pas, il a déjà été créé dans la configuration générale.
3. La ligne a déjà des dépôts ou des parkings autorisés.
4. La configuration reflète la réalité de l'affaire que vous construisez.

Pour valider que la base de flotte est déjà prête:
1. Vérifiez à nouveau la configuration complète de la ligne.
2. Il confirme que les types de véhicules sélectionnés représentent la flotte qui devrait réellement fonctionner ce service.
3. Il confirme que les dépôts ou parkings autorisés minimisent le kilométrage sous vide.
4. Demandez-vous si le système, avec cette configuration, éviterait:
   1. affectations physiquement impossibles,
   2. Non-respect de l'environnement,
   3. des sorties à partir de bases géographiquement inefficaces.
5. Si la réponse est oui, continuez avec le prochain quick start.
6. Si la réponse est non, corrigez la ligne ou créez le type de véhicule manquant avant de suivre.

Une fois cette section terminée, vous devriez pouvoir affirmer que vous avez tous les types de véhicules et de flotte nécessaires à la planification de votre ligne.

## Lectures supplémentaires

- [Préparez le parking et les dépôts](P5_Préparez_Les_Parkings_Et_Les_Dépôts_Pour_Lopération.md)
