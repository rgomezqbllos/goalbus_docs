---
title: Chargement des voyages à vide et des déplacements
shortTitle: Voyages à vide
intro: Apprenez à configurer des matrices de voyages à vide et des déplacements de
  conducteurs pour que GoalBus utilise des temps logistiques réels, minimise les coûts
  non productifs et construit des horaires et des tours plus réalistes.
contentType: how-tos
versions:
- '*'
---
## Créer la matrice appropriée pour le bon type de jour

Avant de calculer Scheduling, vous devez définir comment l'opération se déplace physiquement quand elle ne génère pas de revenus. Dans GoalBus, ce module couvre deux choses différentes:

1. **Voyages à vide**, représentant le mouvement d'un bus avec conducteur entre le dépôt, le parking, le début de ligne ou entre les lignes.
2. **Déplacements de conducteurs**, représentant le mouvement du conducteur sans véhicule, par exemple à pied, en taxi ou en navette.

GoalBus ne traite pas ces mouvements comme une liste unique et fixe. L'outil indique clairement qu'ils doivent être organisés sur **matrices par type de jour**, parce que le trafic change en fonction du contexte opérationnel. Un trajet peut durer 15 minutes un dimanche et 45 minutes un lundi matin, donc la même connexion ne devrait pas toujours être réutilisée en même temps.

Utilisez cette quick start lorsque vous avez déjà configuré des parkings et des dépôts, et vous devez préparer la logistique invisible qui permettra une planification réaliste.

Avant de commencer, assurez-vous que:

1. Tu as déjà préparé les parkings et les dépôts sur P5.
2. Vous avez déjà la ligne ou le service que vous utiliserez comme référence.
3. Tu sais quel genre de jour tu modeles.
4. Vous comprenez la différence entre un voyage vide et un déplacement de conducteur.

Pour ce quick start, utilisez ce cas de référence:

> **Je vais préparer la matrice des voyages à vide pour un jour ouvrable de la ligne L1, reliant le Parking Nord au Terminal Nord, ainsi que la matrice des déplacements de conducteurs lorsque cela est nécessaire pour les relais.**

Pour créer la matrice correcte pour votre cas:

1. Sous GoalBus, ouvre le module **Voyages à vide et déplacements**.
ref: P8_Imagen1.png | full
2. Décidez d'abord de créer une matrice **Voyages à vide**, une matrice **Déplacements de conducteurs** ou les deux.
3. Cliquez sur **Créer un nouveau**.
ref: P8_Imagen2.png | compact(2x5)
4. Saisissez un **Nom** clair pour la matrice.
5. Ajoutez un **description** qui vous permettra de reconnaître le contexte opérationnel.
6. Assigne les **Types de jour** auxquels cette matrice sera appliquée.
7. Garde la matrice.
ref: P8_Imagen3.png | compact(x8)
8. Vérifiez que la matrice est clairement associée au contexte correct et non à une logique générique.

Dans le cas de référence, une matrice valide pourrait être appelée:

- **Vide - Janvier 2026**
- **Déplacements conducteurs - Jours ouvrables**

Une fois cette section terminée, vous devriez avoir une matrice correctement créée et liée au type de jour approprié.

## Chargement de connexions par importation massive ou édition manuelle

Une fois la matrice créée, vous devez la remplir avec les connexions réelles entre les origines et les destinations. Le document indique que GoalBus permet deux formes de travail:

1. **Importations massives CSV**, recommandé pour les grands réseaux.
2. **Entrée manuelle**, utile pour de petits cas ou pour compléter des réglages ponctuels.

Avant de commencer cette section, assurez-vous que:

1. Tu as déjà créé la bonne matrice.
2. Vous avez déjà identifié les origines et les destinations pertinentes.
3. Vous savez si votre affaire peut être chargée manuellement ou si une importation massive est souhaitable.

Pour le chargement de données par importation massive:

1. Préparez un fichier CSV au format standard de GoalBus.
2. Assurez-vous d'inclure au moins:
   1. Origines
   2. Destinations
   3. Distances
   4. Les fuseaux horaires, quand ils appliquent.
   5. Durations
3. Sous GoalBus, sélectionnez l'option **chargement** ou **importation**.
ref: P8_Imagen4.png | compact
4. Choisissez le fichier CSV.
5. Vérifiez le **validation préalable** qui fait le système.
6. Vérifiez si le système:
   1. détecte des erreurs,
   2. indique combien d'enregistrements seront créés.
ref: P8_Imagen5.png |compact
7. Si la validation est correcte, confirmez la charge.
8. Vérifiez que la grille est remplie des enregistrements attendus.

Si tout est correct, la matrice sera affichée de la même manière que celle de l'image suivante:
ref: P8_Imagen6.png |full

Pour charger manuellement les données & #160;:

1. Ouvre la grille de la matrice.
2. Ajoutez un nouveau journal en cliquant sur **Nouvelle relation**.
ref: P8_Imagen7.png | compact
3. Définit le **origine**.
4. Définit le **destination**.
5. Saisissez le temps ou la distance correspondant.
6. Si vous appliquez, définissez le fuseau horaire.
ref: P8_Imagen8.png | compact(15x)
7. Garde le registre.
8. Répétez le processus jusqu'à ce que les connexions minimales nécessaires à votre cas soient terminées.

Pour le cas de référence, commencez par des connexions comme celles-ci:

1. Parking Nord → Terminal Nord
2. Terminal Sud → Parking Nord

Une fois cette section terminée, vous devriez avoir une matrice avec des connexions réelles, que ce soit chargées par fichier ou introduites manuellement.

## Différencier les déplacements à vide des conducteurs

Vous devez maintenant vérifier que vous ne mélangez pas deux logiques différentes. Le document souligne que GoalBus traite les **Voyages à vide** et les **Déplacements de conducteurs** de manière similaire dans la configuration, mais avec un autre but d'affaires:

1. Le voyage à vide utilise **bus + chauffeur** et façonne la logistique de déplacer un véhicule là où il est nécessaire.
2. Le déplacement utilise **Conducteur uniquement** et façonne le temps dont une personne a besoin pour atteindre un relais ou un point de départ sans déplacer de flotte.

Avant de continuer, assurez-vous que:

1. Tu as déjà chargé au moins les connexions essentielles de ton affaire.
2. Vous pouvez identifier si chaque connexion correspond à un véhicule ou à une seule personne.
3. Tu n'as pas mélangé les deux logiques dans la même matrice.

Pour valider que chaque matrice représente la ressource correcte:

1. Vérifiez une connexion **Voyage à vide** et confirmez que votre logique répond à:
   1. déplacer un véhicule depuis le dépôt ou le parking vers la ligne, ou
   2. déplacer un véhicule entre les lignes.
2. Vérifiez une connexion **déplacement** et confirmez que votre logique répond à:
   1. transporter un conducteur sans véhicule; ou
   2. permettre une relève dans un terminal ou en-tête.
3. Vérifiez que la matrice des voyages à vide modele les temps dépendants de la circulation.
4. Vérifiez que la matrice de déplacement des conducteurs reflète le mode de transfert réel, comme la marche, le taxi ou la navette.
5. Corrigez toute connexion mal située avant de continuer.

Pour le cas de référence, demandez-vous:

1. Est-ce que je suis en train de modeler ici un bus qui sort du parking ou juste un conducteur qui va à un en-tête ?
2. Le temps que j'ai mis correspond-il à la circulation réelle ou au mode de déplacement du conducteur ?
3. Le moteur utiliserait-il cette information correctement lors de la construction des horaires et des tours ?

Quand vous aurez terminé cette section, vous devriez savoir quelle partie de votre configuration appartient à la logistique du véhicule et quelle partie appartient à la logistique du conducteur.

## Vérifier que la matrice est prête pour Scheduling

L'objectif final de ce quick start n'est pas seulement de remplir une table, mais de préparer une base logistique que Scheduling peut consommer. Le document explique qu'une modélisation précise de ces matrices améliore trois choses:

1. la **transparence des coûts**,
2. la **création réaliste de tours**,
3. et **précision de l'optimisation**.

Avant de finir, assurez-vous que:

1. La bonne matrice existe.
2. Elle est associée au bon jour.
3. Les connexions minimales de l'affaire sont déjà chargées.
4. Vous avez correctement séparé les voyages à vide et les déplacements des conducteurs.

Pour valider que la matrice est déjà prête pour l'étape suivante:

1. Vérifiez le cas de référence que vous construisez.
2. Il confirme que GoalBus sait déjà:
   1. d'où sort physiquement le véhicule,
   2. où il entre dans la ligne,
   3. comment il revient quand il y a lieu,
   4. et comment un conducteur se déplacerait pour un relais s'il applique.
3. Demandez-vous si le système pourrait déjà réduire les temps et les distances non productifs dans ce cas.
4. Si la réponse est oui, continuez avec le prochain quick start.
5. Si la réponse est non, retournez en arrière et ajoutez ou corrigez des connexions avant de suivre.

Quand vous aurez terminé cette section, vous devriez pouvoir affirmer que votre base logistique est suffisamment réaliste pour maintenir les temps, les services et Scheduling.

## Lectures supplémentaires

- [Définir les types de véhicules et de flotte autorisés par ligne](P4_Définir_Les_Types_De_Véhicules_Et_De_Flotte_Autorisés_Par_Ligne.md)
