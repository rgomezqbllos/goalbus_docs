---
title: Création de l'offre de service de base avec voyages et horaires
shortTitle: Offre de service
intro: Apprenez à créer un service commercial, à vérifier vos voyages en ligne et
  sens, et à laisser une offre validée et exécutable avant de passer à Scheduling
  sur GoalBus.
contentType: how-tos
versions:
- '*'
---
## Création du service commercial qui servira de conteneur de l'offre

Avant d'examiner les voyages individuels, vous devez créer le **service commercial** qui fera office de conteneur de votre offre. Dans GoalBus, les services commerciaux sont la couche de gouvernance de l'offre: ils relient lignes et itinéraires, types de jour et logique de calendrier, et les voyages qui définissent le service réel. L'outil indique clairement que cette structure empêche que des horaires incomplets ou non révisés soient utilisés de manière opérationnelle.

Utilisez ce quick start lorsque vous avez déjà un réseau validé, une base temporelle définie et vous devez transformer cette structure en une offre réelle qui peut ensuite être validée, mesurée et consommée dans Scheduling.

Avant de commencer, assurez-vous que:

1. Vous avez déjà configuré des types de jours fériés et de jours fériés sur P2.
2. Tu as déjà validé l'année d'exploitation en P3.
3. Vous avez déjà préparé le réseau de base et opérationnel sur P4 et P5.
4. Vous avez déjà défini des parkings, des dépôts et des déplacements sur P6 et P7.
5. Vous avez déjà défini les types de véhicules autorisés en P8.
6. Tu as déjà créé la version du temps et les temps de voyage sur P9.
7. Tu sais quelle ligne, quel genre de jour et quel sens tu utiliseras comme cas de référence.

Pour ce quick start, utilisez ce cas de référence:

> **Je vais créer le service commercial de la ligne L1, vérifier vos voyages aller-retour et laisser l'offre validée avant de passer à Scheduling.**

Pour créer le service commercial de votre cas:

1. Dans GoalBus, consultez **Services**.
ref: P10_Imagen1.png | compact
2. Cherchez s'il existe déjà un service commercial adapté à votre cas.
3. Si le service existe déjà, ouvrez-le et vérifiez qu'il correspond vraiment au type de jour et à l'offre que vous voulez préparer.
4. S'il n'existe pas, créez-en un nouveau.
ref: P10_Imagen2.png | compact(2x)
5. Définit:
   1. Un **Nom** clair pour le service,
   2. Le **type de jour** qu'il appliquera,
   3. Les **lignes** qui feront partie de ce service.
   4. Le **description** de service si vous voulez donner plus de détails, bien que ce champ n'est pas obligatoire.
6. Garde le service.
ref: P10_Imagen3.png | compact(x8)
7. Confirmez que vous pouvez déjà entrer dans sa vue des horaires ou des grilles de voyages.

Dans le cas de référence, une option valable pourrait être:

- **Jour ouvrable standard - L1**

Il est également possible de créer le nouveau service à partir de la charge de fichiers GTFS. Pour cela:
1. 1. Dans GoalBus, voyez la vue **Services**.
ref: P10_Imagen1.png | compact
2. Importe les fichiers GTFS à partir de **Importer des services**.
ref: P10_Imagen11.png | compact
3. S'il n'y a pas d'erreurs dans le chargement, le service aura été créé correctement.
4. En entrant dans le service, vous pouvez voir tous les voyages créés avec l'importation.

Une fois cette section terminée, vous devriez avoir un service commercial qui agit comme conteneur structuré de l'offre.
ref: P10_Imagen4.png  | full



## Accès à la grille de voyages et changement de contexte

Une fois le service créé, l'étape suivante est d'entrer dans la grille de voyages. Cette vue est une  &lt; &lt; tour de contrôle &gt; &gt; centralisée pour tous les voyages programmés au sein du service. D'ici, vous pouvez changer de ligne, changer de service et alterner entre **Sentido 1** et **Sentido 2** sans perdre le contexte opérationnel.

Avant de commencer cette section, assurez-vous que:

1. Tu as déjà créé ou validé le service commercial.
2. Tu sais quelle ligne tu veux vérifier d'abord.
3. Tu sais quel sens ou quelle direction tu vas utiliser comme point de départ.

Pour accéder et changer de contexte dans la grille de voyages:

1. Dans la liste des services, cliquez sur l'identificateur du service ou sur l'icône **Afficher les horaires**.
2. Une fois à l'intérieur, utilisez le sélecteur de ligne pour changer entre les lignes incluses dans le service.
3. Utilisez le menu déroulant des services si vous voulez comparer avec un autre service commercial.
4. Changez entre **Sentido 1** et **Sentido 2** pour vérifier séparément les voyages aller-retour.
5. Restez concentré sur une seule ligne et un seul sens pendant que vous construisez votre dossier de base.

Pour le cas de référence:

1. Ouvre le service **Jour ouvrable standard - L1**.
2. Entrez d'abord dans **Sentido 1**.
3. Vérifiez ensuite **Sentido 2**.
ref: P10_Imagen5.png  | full

Une fois cette section terminée, vous devriez être en mesure de naviguer sur l'offre sans perdre le contexte de ligne, de service et d'adresse.

## Création ou révision des voyages du service

Maintenant oui, entrez dans le détail des **Voyages**. Le document explique qu'un horaire est une séquence d'événements et que chaque voyage doit être lié à:

1. une variation spécifique de route,
2. une séquence d'arrêts,
3. et une référence temporelle.

Cela garantit que les départs et les arrivées sont physiquement exécutables. En outre, la grille par défaut ne montre que les arrêts principaux ou les points temporaires pour maintenir une vision claire, bien que vous puissiez agrandir la vue pour voir tous les intermédiaires.

Avant de commencer cette section, assurez-vous que:

1. Vous avez déjà une version du temps valide sur P9.
2. Vous savez quelle variation de route correspond au voyage que vous voulez créer ou vérifier.
3. Vous savez quelle ligne et quel sens vous éditez.

Pour créer ou réviser les voyages du service:

1. Dans le service, sélectionnez une ligne et un sens.
2. Vérifie les voyages qui existent déjà sur la grille.
3. Si vous avez besoin de créer un nouveau voyage, utilisez l'action correspondante pour ajouter une nouvelle sortie.
ref: P10_Imagen9.png | compact
4. Assigne le voyage:
   1. la **itinéraire ou variation** correcte,
   2. la **heure de départ**,
   3. et **référence temporelle** compatible avec la version créée en P9.
ref: P10_Image10.png
5. Si le voyage existe déjà, passez le curseur sur votre identifiant pour vérifier la variation de route que vous utilisez.
6. Vérifiez que la durée totale calculée a un sens par rapport aux temps de parcours définis.
7. Agrandissez la séquence si vous avez besoin de vérifier tous les arrêts intermédiaires.
8. Répétez le processus jusqu'à ce que vous ayez une base minimale de voyages par sens.

Pour le cas de référence, vous pouvez commencer par une structure minimale comme ceci:

1. L1 - Sentido 1
   1. Voyage 1: sortie 06:00
   2. Voyage 2: sortie 06:20
2. L1 - Sentido 2
   1. Voyage 1: sortie 06:10
   2. Voyage 2: sortie 06:30

Une fois cette section terminée, vous devriez avoir une offre de voyage de base liée à l'itinéraire, au sens et à la référence temporelle.

## Révision des intervalles, de la durée totale et de l'équilibre de l'offre

Après avoir créé ou vérifié les voyages, vous devez vérifier que l'offre a un sens en tant qu'ensemble. La grille vous permet de surveiller en permanence:

1. la **durée totale** de chaque voyage,
2. le **intervalle** par rapport au voyage précédent,
3. et les KPI globaux par ligne, comme le nombre de voyages, la distance totale et le temps total de conduite. Cela permet d'évaluer si l'offre est équilibrée, symétrique et économiquement viable.

Avant de continuer, assurez-vous que:

1. Vous avez déjà au moins quelques voyages créés ou révisés.
2. Vous pouvez voir la durée totale de ces voyages.
3. Tu peux déjà comparer les sens et les fréquences.

Pour valider l'équilibre de l'offre:

1. Sur la grille, vérifiez le **durée totale** de chaque voyage.
2. Vérifiez qu'elle coïncide raisonnablement avec les temps de parcours attendus.
3. Vérifiez le **intervalle** par rapport au voyage précédent et détectez s'il y a des trous excessifs ou des sorties trop ensemble.
4. Comparez le nombre de voyages du **Sentido 1** avec celui du **Sentido 2**.
5. Vérifiez les KPI globaux de la ligne & #160;:
   1. **Nombre de voyages**,
   2. **Distance totale**,
   3. **Temps total**.
ref: P10_Imagen6.png | compact
6. Il corrige tout déséquilibre évident avant de rendre le service intelligent.

Pour le cas de référence, demandez-vous:

1. L'aller et le retour sont-ils équilibrés ?
2. Les intervalles entre les voyages correspondent-ils au niveau d'offre que vous voulez construire ?
3. La durée totale de chaque voyage est-elle cohérente avec la référence temporelle?
4. L'offre semble-t-elle économiquement raisonnable ou est-elle surdimensionnée ?

Une fois cette section terminée, vous devriez avoir une offre non seulement créée, mais aussi révisée du point de vue de la fréquence, de la durée et de l'équilibre.

## Valider le service pour le rendre prêt pour le calcul

La dernière étape est **valider** le service. Valider bloque les données de voyage et l'autorise pour votre programmation, tandis qu'un service non validé est toujours en phase d'édition et n'est pas prêt pour le calcul. Il indique également qu'un service validé devient limité pour l'édition, cesse d'être supprimé et est prêt à être utilisé dans la programmation.

Avant de finir, assurez-vous que:

1. Tu as vérifié les voyages du service.
2. Tu as vérifié les itinéraires, les durées et les intervalles.
3. Tu as confirmé que l'offre répond à l'affaire que tu veux construire.

Pour valider le service et le rendre prêt pour Scheduling:

1. Vérifie une dernière fois la grille des voyages du service.
2. Confirmez que vous n'avez plus besoin de modifier le service.
3. Exécutez l'action **Valider** sur le service ou sur l'ensemble de voyages correspondant.
ref: P10_Imagen7.png | full
4. Vérifiez que l'état du service passe à **Validation**.
ref: P10_Imagen8.png | compact(2x)
5. Confirme ce qui suit:
   1. les voyages sont bloqués pour des changements accidentels,
   2. le service est déjà **prêt à être calculé**,
   3. et Scheduling pourra le lire dans les étapes suivantes.
6. Si vous avez encore besoin de modifications, utilisez la logique **Ne pas valider** uniquement pour retourner le service en édition et finissez de l'ajuster avant de le valider à nouveau.

Pour le cas de référence, ne poursuivez pas Scheduling jusqu'à ce que vous puissiez affirmer:

1. La ligne L1 a une offre ouvrable cohérente.
2. Les voyages sont associés à la bonne variation de route.
3. La durée totale et les intervalles sont logiques.
4. Le service est déjà en état **Validation**.

Une fois cette section terminée, vous devriez avoir une offre commerciale déjà structurée, révisée et validée, prête à être consommée par Scheduling.

## Lectures supplémentaires

- [Validation de la structure opérationnelle: dépôts, unités et groupes](P11_Validation_De_La_Structure_Opérationnelle_Et_De_Létat_Du_Service.md)
