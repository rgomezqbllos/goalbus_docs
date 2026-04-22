---
title: Préparez le réseau principal avec des arrêts, des lignes et des itinéraires
shortTitle: Réseau enseignant
intro: Apprenez à créer et valider la base réseau qui utilisera votre planification,
  y compris les arrêts, lignes et itinéraires, afin que les étapes suivantes de temps,
  de services et de Scheduling partent d'une structure cohérente.
contentType: how-tos
versions:
- '*'
---
## Créer ou valider les arrêts que votre réseau utilisera

Avant de créer des lignes ou des itinéraires, vous devez vous assurer que les **Arrêts** que vous utiliserez existent déjà et sont correctement définies. Dans GoalBus, un arrêt n'est pas seulement un point géographique. Il s'agit également d'une entité avec une identité opérationnelle et plusieurs couches de noms qui servent à différents publics, tels que les planificateurs, les passagers et les appareils internes. En outre, le système permet de désactiver les arrêts au lieu de les supprimer brusquement, afin de ne pas casser les itinéraires ou les voyages actifs.

Utilisez ce quick start lorsque vous avez déjà fermé la base temporaire en P2 et P3, et vous devez commencer à construire le réseau de base sur lequel vous allez ensuite définir des itinéraires, des temps de trajet et des services.

Avant de commencer, assurez-vous que:

1. Tu as déjà configuré les types de jours fériés et de jours fériés sur P2.
2. Tu as déjà validé l'année d'exploitation en P3.
3. Vous avez accès à l'environnement avec permission pour consulter ou modifier l'infrastructure réseau.
4. Vous savez déjà quelle ligne ou coureur vous voulez préparer comme première affaire.

Pour ce quick start, utilisez ce cas de référence:

> **Je vais préparer la ligne L1, créer ou valider vos arrêts de base et laisser vos itinéraires aller-retour pour les utiliser plus tard dans mon premier cas de Scheduling.**

Pour créer ou valider les arrêts de votre cas:

1. Dans GoalBus, allez au module **Configuration des arrêts** dans la configuration des services.
ref: P6_Imagen1.png
2. Cherche si les arrêts de base de ton affaire existent déjà.
3. Si un arrêt existe déjà, ouvrez et confirmez que votre identité est correcte.
4. Si un arrêt n'existe pas, cliquez sur **Nouveau arrêt**.
5. Saisissez ou validez ces champs:
   1. **Code** en tant qu'identificateur unique.
   2. **Nom commercial** comme nom visible pour le passager.
   3. **Nom long** comme référence descriptive interne.
   4. **Nom court** si vous en avez besoin pour une vue compacte.
6. Définit l'emplacement de l'arrêt par coordonnées ou adresse.
7. Ajoutez un **ID externe** si vous voulez un identifiant supplémentaire.
8. Garde l'arrêt.
ref: P6_Imagen2.png | compact(20x)
9. Répétez le processus jusqu'à ce que vous ayez les arrêts minimums nécessaires pour votre affaire.
10. Si vous détectez un ancien arrêt qui ne devrait plus être utilisé dans une nouvelle planification, changez-le à **Inactif** au lieu de l'éliminer.

Pour le cas de référence, utilisez une logique comme celle-ci:

1. Terminal Nord
2. Centre
3. Hôpital
4. Université
5. Terminal Sud

Une fois cette section terminée, vous devriez avoir les arrêts de base prêts et dans un état cohérent pour construire la ligne et les routes.

## Création ou validation de la ligne en tant que conteneur opérationnel

Après avoir eu les arrêts de base, vous devez vérifier la **ligne**. Dans GoalBus, une ligne est plus qu'un simple numéro de service. C'est un conteneur de logique opérationnelle. Lorsque vous la configurez correctement, vous définissez les limites physiques et logistiques du service, comme le type de flotte autorisé ou la géographie opérationnelle des réservoirs et des parkings qui influera ensuite sur l'optimisation.

Avant de commencer cette section, assurez-vous que:

1. Tu as vérifié ou créé les bases de ton affaire.
2. Tu sais quel service tu veux représenter.
3. Il est clair que la ligne est le conteneur administratif et pas encore le trajet physique détaillé.

Pour créer ou valider la ligne de votre cas:

1. Dans GoalBus, allez au module **Configuration du réseau**.
ref: P6_Imagen3.png
2. Cherche si la ligne dont tu as besoin existe déjà.
3. Si la ligne existe déjà, ouvrez et vérifiez sa configuration.
4. Si elle n'existe pas, créez une nouvelle ligne en cliquant sur **Créer une ligne**.
5. Définit ou valide:
   1. **Nom de la ligne** pour le nom interne.
   2. **Nom court** pour une vue compacte.
   3. **Nom commercial**, s'il vous plaît.
   4. **Parkings** associés à la ligne. **OJO: la création préalable de Párkings est nécessaire.**
   5. **Types de véhicules** pour associer les types de véhicules disponibles pour la ligne. **OJO: la création préalable des types de véhicules est nécessaire.**
   6. **ID externe** pour ajouter un identifiant supplémentaire.
   7. **Couleur** pour assigner une certaine couleur à la ligne.
6. Vérifiez que la ligne représente vraiment le bon service.
7. Garde la ligne.
ref: P6_Imagen4.png | compact(8.5x)8. Confirma que la línea ya puede usarse como contenedor para crear rutas específicas.

Pour le cas de référence, vous pouvez penser à une ligne comme:

- **L1**
- **L1: Terminal Nord - Terminal Sud**

Une fois cette section terminée, vous devriez avoir une ligne claire et utilisable sur laquelle vous pourrez ensuite définir des itinéraires par sens.

## Création ou validation des itinéraires aller-retour

Avec la ligne déjà prête, vous pouvez maintenant travailler avec les **itinéraires**. Dans GoalBus, une route est le trajet physique réel qui parcourt un véhicule. Une même ligne peut avoir plusieurs itinéraires valables, tels que des tours courts, des détours ou des entrées à dépôt. Le système organise ces variations par direction ou sens, et protège les itinéraires en usage  &lt; &lt; en cours d &apos; utilisation &gt; &gt; afin d &apos; éviter des changements dangereux dans les services déjà actifs.  &lt; &lt; Filecite &gt; &gt; turn20file1 &lt; &lt; L1-L20 &gt; &gt;

Avant de commencer cette section, assurez-vous que:

1. Vous avez déjà la ligne créée ou validée.
2. Tu as déjà les arrêts de base que tu vas utiliser dans la séquence.
3. Tu sais si tu vas créer un seul chemin par sens ou si ton cas a déjà besoin de variantes.

Pour créer ou valider les itinéraires de votre cas:

1. Dans la table principale des lignes, cliquez sur la ligne que vous venez de créer ou valider pour accéder à la vue des itinéraires.
ref: P6_Imagen5.png
2. Utilisez les onglets ou les commandes de direction pour travailler sur **Sentido 1** et **Sentido 2**.
3. Vérifie s'il y a déjà un bon chemin pour le sens dont tu as besoin.
4. Si la route n'existe pas, crée une nouvelle variation de la route pour ce sens.
5. Définit la séquence d'arrêts dans l'ordre correct.
6. Confirmez l'en-tête de démarrage et l'en-tête de fin.
7. Garde la route.
8. Répétez la logique pour le sens inverse.
9. Si vous trouvez un chemin marqué **En cours d &apos; utilisation**, n'essayez pas de modifier sa géométrie de base sans vérifier plus tôt s'il existe une alternative déverrouillée.


Pour le cas de référence:
1. Définit la route aller:
   1. Terminal Nord
   2. Centre
   3. Hôpital
   4. Université
   5. Terminal Sud
2. Définit le chemin de retour & #160;:
   1. Terminal Sud
   2. Université
   3. Centre
   4. Terminal Nord

Une fois cette section terminée, vous devriez avoir une ligne avec ses principaux itinéraires par sens, prête pour que dans le prochain quick start vous puissiez vérifier plus en détail les séquences, les points pertinents et la logique opérationnelle.

## Lectures supplémentaires

- [Revue du réseau opérationnel: séquences, permissions d'arrêt et points de relais]
