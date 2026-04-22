---
title: Création du premier scénario de Scheduling avec le moteur Classic
shortTitle: Scénario Classic
intro: Apprenez à créer votre premier scénario de Scheduling avec le moteur GoalBus
  Classic, sélectionner correctement les entrées de calcul et distinguer quand appliquer
  des règles de véhicules et quand appliquer des règles de rotation.
contentType: how-tos
versions:
- '*'
---
## Création du scénario avec l'offre validée comme point de départ

Maintenant que vous avez déjà l'offre validée, la logique des véhicules et la logique des tours, l'étape suivante est de créer le **Scénario de Scheduling** qui utilisera cette base pour calculer une solution exécutable.

Ce scénario est l'environnement contrôlé où vous allez combiner:
1. la **offre validée**,
2. la **Matrice des voyages à vide**,
3. le **modèle de règles de véhicule**,
4. et le **modèle de règles de rotation**.

Utilisez ce quick start lorsque vous avez déjà fermé le paramétrage de base et que vous voulez préparer le scénario définitif pour le calcul avec le moteur Classic.

Avant de commencer, assurez-vous que:
1. Tu as déjà configuré et validé l'offre de service sur P10.
2. Tu as vérifié la structure opérationnelle sur P11.
3. Tu as déjà défini les règles des véhicules en P12.
4. Tu as déjà défini les types de gardes et les règles de garde en P13.
5. Vous avez déjà préparé la matrice des voyages à vide de P7.
6. Tu sais quel genre de journée et quelles lignes vont faire partie du calcul.

Pour ce quick start, utilisez ce cas de référence:

> **Je vais créer le premier scénario de Scheduling pour la ligne L1, en utilisant l'offre ouvrable validée, la matrice de voyages à vide correspondante et les modèles corrects de règles de véhicules et de tours, pour lancer le calcul final avec GoalBus Classic.**

Pour créer le scénario de base de votre affaire:
1. Sous GoalBus, ouvre le module **Planification**.
ref: P14_Imagen1.png | compact
2. Cliquez sur **Nouveau scénario**.
ref: P14_Imagen2.png | compact(2x)
3. Introduisez l'identité de base du scénario:
   1. **Nom**
   2. **Type de jour**
   3. **Description** si vous voulez donner plus de détails.
   4. Scénario **uniquement pour véhicules** ou non.
ref: P14_Imagen3.png | compact(x10)
4. Sélectionnez les éléments de base du scénario & #160;:
   1. Le **service commercial validé** que tu veux couvrir.
   2. Sélectionnez le **Modèle de règles d'heure**.
   3. Sélectionnez le **Modèle de règles relatives aux types de véhicules** (en option).
   4. Sélectionnez le **Matrice des voyages à vide** correspondant au même type de jour.
   5. Sélectionnez le **matrice de déplacement des conducteurs** qui fera partie de la scène.
ref: P14_Imagen4.png | compact(x10)
5. Sélectionnez la ligne.
ref: P14_Imagen5.png | compact(x12)
6. Enregistrez ou terminez la création du scénario.
7. Vérifiez que le scénario apparaît dans le tableau principal de planification.

Dans le cas de référence, une option valable pourrait être:
- **Scheduling Classic - L1 ouvrable**

Une fois cette section terminée, vous devriez avoir un scénario créé avec ses entrées logistiques et commerciales correctes créé comme dans l'image suivante:
ref: P14_Imagen6.png | full

## Comprendre quand utiliser des règles de véhicule et quand utiliser des règles de service

Avant de configurer le moteur, vous devez préciser une distinction importante: **les règles de véhicules et les règles de rotation ne résolvent pas le même problème**.

Utilisez **règles applicables aux véhicules** quand vous voulez contrôler le comportement de la flotte. Ce sont les règles correctes si vous avez besoin de modeler:
1. compatibilité physique des véhicules,
2. limites de capacité ou de portée,
3. restrictions en matière d'infrastructure,
4. ou des politiques opérationnelles liées à l'utilisation de la flotte.

Utilisez **Règles de rotation** lorsque vous voulez contrôler la façon dont le travail humain est organisé. Ce sont les règles correctes si vous avez besoin de modeler:
1. les horaires de travail,
2. pauses et pauses,
3. les heures de début et de fin,
4. amplitude,
5. ou des différences entre les types de garde, comme demain, soir ou soir.

Avant de continuer, assurez-vous que:
1. Tu sais quelles sont les restrictions du véhicule.
2. Tu sais quelles sont les restrictions du service.
3. Vous n'essayez pas de résoudre un problème de personnel avec des règles de flotte, ni à l'envers.

Pour décider quel modèle vous devez utiliser dans chaque cas:
1. Demandez-vous si la restriction affecte le **bus** ou le **conducteur**.
2. Si vous affectez le **bus**, utilisez le **modèle de règles de véhicule**.
3. Si vous affectez le **travail humain** ou le type de service, utilisez le **modèle de règles de rotation**.
4. Si une règle doit s &apos; appliquer à tous les types de tours, la modifier en tant que règle globale ou avec la portée la plus large disponible.
5. Si une règle ne s &apos; applique qu &apos; à un type de service donné, elle ne s &apos; applique qu &apos; à ce type de service.

Pour le cas de référence:
1. Si vous voulez limiter la flotte qui peut couvrir la L1, utilisez **règles applicables aux véhicules**.
2. Si vous voulez contrôler la construction d'une équipe de demain ou de nuit, utilisez **Règles de rotation**.
3. Si une restriction mélange les deux choses, séparez-la et configurez-la dans le bon modèle.

Quand vous aurez terminé cette section, vous devriez être clair sur le modèle qui répond à chaque besoin et éviter les configurations croisées ou contradictoires.

## Sélectionner le moteur GoalBus Classic pour le calcul final

Maintenant, vous devez configurer le moteur de calcul. Pour ce quick start, l'objectif est de travailler avec **GoalBus Classic** comme moteur principal de la scène. C'est le moteur d'optimisation profonde visant à obtenir la meilleure solution finale lorsque la paramétrage est déjà suffisamment mûre.

Avant de commencer cette section, assurez-vous que:
1. Tu as déjà la scène créée.
2. Vous avez déjà sélectionné correctement le service, les lignes et la matrice de voyage sous vide.
3. Tu as déjà les modèles de règles que tu vas utiliser.
4. Vous êtes prêt pour un calcul final ou presque final, pas seulement pour un test tactique rapide.

Pour sélectionner le moteur Classic:
1. Ouvre la scène que tu viens de créer en appuyant sur elle.
2. Dans la barre supérieure, cliquez sur **Configuration de calcul**.
ref: P14_Imagen7.png | compact
3. Dans le panneau latéral, sélectionnez **Moteur GoalBus Classic**.
4. Confirmez que le scénario n'est plus configuré avec le moteur d'apprentissage automatique.
5. Détermine le **Flexibilité de programmation pour première solution** (par défaut est 0.)
6. Utilisez une valeur prudente pour trouver une solution initiale sans dénaturer l'affaire.
7. Sélectionnez le **Temps de calcul maximal** qui aura le moteur pour obtenir de nouvelles solutions.
ref: P14_Imagen8.png | compact(x8)
8. Enregistre les paramètres.

La flexibilité initiale ne s'applique qu'au moteur GoalBus Classic et permet à la première solution de ne pas bloquer si les restrictions sont trop rigides dès le début. Le temps maximum de calcul sert de garantie de livraison et oblige le système à retourner la meilleure solution valable qu'il ait trouvée dans le délai disponible.     &lt;filecite &gt; 34file0 &gt; L1-L20 &lt; &lt; L20 &gt; &gt; , &lt; &lt; Filecite &gt; &gt; , &lt; &lt; Firecite &gt; &gt; , &lt; &lt; Five &gt; &gt; , &lt; &lt; Five &gt; &gt; , &lt; &lt; Classic &gt; &gt; , &lt; &lt; GoalBus &gt; &gt; et &lt; &lt; Classic &gt; &gt; , &lt; &lt; &lt; &lt; &lt; &gt; &gt; &gt; &gt; &gt; &gt; &gt; &gt; &gt; &gt; &gt; &gt; &gt; &gt; &gt; &gt; &gt; &gt; &gt; &gt; &gt; &gt; &gt; &gt; &gt; &gt; &gt; &gt; &gt; &gt; .

Pour le cas de référence:
1. Utilisez **GoalBus Classic** comme moteur principal.
2. Réservez le moteur d'apprentissage automatique uniquement pour les validations rapides préalables, pas comme moteur de calcul final.
3. Utilisez une flexibilité initiale modérée si vous pensez que les restrictions pourraient bloquer la première solution.
4. Définit un délai maximum réaliste pour que l'équipement reçoive une solution viable dans les délais impartis.  &lt; &lt; Filefilecite &gt; &gt; , &lt; &lt;turn34file0 &gt; &gt; , &lt; &lt; L20 &gt; &gt; , &lt; &lt;filecite &gt; &gt; , &lt; &lt; L1 &gt; &gt; , &lt; &lt; L2 &gt; &gt; , &lt; &lt; L2 &gt; &gt; , &lt; &lt; L2 &gt; &gt; , &lt; &lt; L2 &gt; &gt; , &lt; &lt; L2 &gt; &gt; , &lt; &lt; L2 &gt; , &lt; L2 &gt; , &lt; &lt; L2 &gt; &gt; , &lt; &lt; L2 &gt; , &lt; L2 &gt; L20 &gt; , &lt; L2 &gt; .

Une fois cette section terminée, vous devriez avoir le moteur Classic configuré avec un cadre de calcul contrôlé et réaliste.

## Je regarde la scène avant de la lancer.

Avant de calculer, vous devez effectuer une révision finale du scénario complet. L'objectif est de confirmer que vous n'entrez pas dans le calcul avec des entrées contradictoires.

Avant de continuer, assurez-vous que:
1. Tu as choisi le bon service validé.
2. Tu as déjà choisi la matrice des voyages à vide du bon jour.
3. Tu as déjà attribué les bons modèles de règles de voiture et de service.
4. Vous avez déjà sélectionné GoalBus Classic comme moteur.
5. Tu as déjà ajusté la flexibilité et le temps maximum.

Pour vérifier le scénario avant de lancer le calcul:
1. Vérifiez le nom et le type de jour de la scène.
2. Confirmez que le **service commercial** correspond exactement à celui que vous voulez programmer.
3. Il confirme que le **Matrice des voyages à vide** correspond au même contexte temporel.
4. Vérifiez le **modèle de règles de véhicule** et confirmez qu'il protège la logique de la flotte.
5. Vérifiez le **modèle de règles de rotation** et confirmez qu'il protège la logique du travail humain.
6. Vérifiez que vous n'oubliez pas un modèle obligatoire pour votre affaire.
7. Si tout est cohérent, laissez le scénario prêt pour le calcul.

Pour le cas de référence, ne continuez pas jusqu'à ce que vous puissiez affirmer:
1. Le L1 ouvrable utilise son service validé correct.
2. La matrice est la bonne.
3. Le modèle de véhicule limite la flotte de manière réaliste.
4. Le modèle de rotation organise le travail de manière cohérente.
5. GoalBus Classic est déjà sélectionné.

Quand tu auras fini cette section, tu devrais avoir un scénario propre, cohérent et prêt pour le calcul final.

## Lectures supplémentaires

- [Mise en œuvre et validation du premier calcul de Scheduling](P15_Mise_En_Œuvre_Et_Validation_Du_Premier_Calcul_De_Scheduling.md)
