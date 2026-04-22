---
title: Définir des versions de temps et de temps de parcours pour l'opération
shortTitle: Versions et temps
intro: Apprenez à créer des versions de temps, à définir des temps de trajet et de
  séjour par type de jour et par fuseau horaire, et à laisser une référence temporelle
  fiable avant de créer ou d'ajuster des services dans GoalBus.
contentType: how-tos
versions:
- '*'
---
## Créant la version du temps que votre cas utilisera

Avant de définir les temps de parcours, vous devez créer un **version temporelle**. Dans GoalBus, une version n'est pas seulement une étiquette: c'est la bibliothèque de temps qui regroupe la logique temporelle qui s'appliquera à des itinéraires spécifiques et à des types de jours spécifiques. C'est important parce qu'un lundi matin ne se comporte pas comme un dimanche matin, et le système ne devrait pas réutiliser un ensemble unique de temps pour toute l'année.

Utilisez ce quick start lorsque vous avez déjà une ligne et ses itinéraires définis, et vous devez construire la base temporelle qui servira ensuite à calculer les voyages, valider les durées et comparer les écarts par rapport à la norme.

Avant de commencer, assurez-vous que:
1. Tu as déjà préparé le réseau à P6.
2. Tu as déjà vérifié le réseau opérationnel sur P7.
3. Tu as déjà configuré la base temporelle des types de jour sur P2.
4. Tu as déjà validé l'année d'exploitation en P3.
5. Tu sais quelle ligne, quels itinéraires et quel genre de jour tu vas utiliser comme référence.

Pour ce quick start, utilisez ce cas de référence:

> **Je vais créer une version temporelle pour la ligne L1 en jours ouvrables et l'utiliser comme référence temporaire avant de créer ou d'ajuster des services.**

Pour créer la version temporelle de votre cas:
1. Dans GoalBus, ouvrez le **Vue Routes** de la ligne que vous utiliserez comme référence.
2. Sélectionnez l'icône ou l'option **Gestion des temps de voyage et d'arrêt**.
ref: P9_Imagen1.png | compact
3. En haut de la vue, créez une nouvelle version en sélectionnant **Nouvel ensemble d'horaires**.
ref: P9_Imagen2.png | compact
4. Définit un **Nom** clair pour la version.
5. Ajoutez un **description** qui vous aide à distinguer le contexte opérationnel.
6. Sélectionnez les **Types de jour** auxquels cette version s'applique, par exemple **Jours ouvrables**.
7. Il relie les **Variations de la route** ou des séquences spécifiques qui feront partie de cette version temporelle.
8. Garde la version.
ref: P9_Imagen3.png | compact(x8)
9. Vérifiez que la version est déjà disponible comme référence temporelle pour cette ligne.

Dans le cas de référence, une version valide pourrait être appelée:
- **Jours ouvrables d'hiver**
- **L1 ouvrable de base**

Une fois cette section terminée, vous devriez avoir créé une version temporelle que le système peut utiliser comme référence temporaire pour les services de cette ligne similaire à celle de l'image suivante.
ref: P9_Imagen4.png | full

## Définir les temps de trajet entre les arrêts principaux

Après avoir créé la version, vous devez saisir les **temps de parcours**. Dans GoalBus, ces temps sont principalement définis entre **Arrêts principaux** ou **points temporaires**, pas entre tous les arrêts intermédiaires. Les en-têtes sont principaux par défaut, et de là se construit la logique temporelle qui alimentera ensuite les services.

En outre, GoalBus ne fonctionne pas avec une seule valeur par segment. Le moteur utilise une logique **minimum, optimal et maximal** pour donner une flexibilité contrôlée au calcul:
1. **Minimum**: le temps le plus rapide possible.
2. **Optime**: le temps cible auquel le moteur tend.
3. **Maximum**: le temps le plus lent acceptable.

Avant de commencer cette section, assurez-vous que:
1. Tu as déjà créé la version temporelle.
2. Tu sais quel arrêt principal tu utiliseras comme référence.
3. Vous avez déjà identifié le sens ou l'adresse que vous voulez configurer d'abord.

Pour définir les temps de parcours de votre cas:
1. Dans la grille temporelle, sélectionnez le **segment** entre deux arrêts principaux.
ref: P9_Imagen5.png | full
2. Créez un ou plusieurs **Nombre de créneaux horaires** pour refléter la réalité opérationnelle.
3. Pour chaque bande, entrez:
   1. le temps **minimum**,
   2. le temps **optimum**,
   3. le temps **maximum**.
ref: P9_Imagen6.png | compact
4. Rangez le segment.
5. Répétez le processus pour le segment principal suivant.
6. Quand vous avez terminé un sens, répétez la même logique pour le sens inverse.

Les bandes créées ne doivent pas avoir d'écarts ou de chevauchements entre elles. S'il y en a, il ne sera pas possible de garder les temps.

Pour le cas de référence, une logique de base pourrait être:
1. **Terminal Nord → Centre**
   1. 07:00-00-09:00
      1. Minimum: 12 min
      2. Optime: 15 min
      3. Maximum: 18 min
   2. 09:00-22:00
      1. Minimum: 5 min
      2. Optime: 5 min
      3. Maximum: 5 min
   3. 22 h 00 - 06 h 00
      1. Minimum: 8 min
      2. Optime: 10 min
      3. Maximum: 12 min
2. **Centre → Hôpital**
3. **Hôpital → Université**
4. **Université → Terminal Sud**

Lorsque vous avez terminé cette section, vous devriez avoir des temps de conduite élastiques définis entre les points temporels principaux de la route.

## Définir les temps de séjour pour la régulation et la récupération

En plus du temps de conduite, GoalBus doit savoir combien de temps un véhicule peut rester à un arrêt principal. Ces **temps d'échelle** sont importants parce qu'ils permettent de régler le départ, d'absorber les arrivées anticipées et de laisser une marge de récupération sur les terminaux ou les points de connexion.

Avant de commencer cette section, assurez-vous que:
1. Tu as déjà défini des temps de parcours entre les principaux segments.
2. Vous savez quels terminaux ou points importants ont besoin d'être réglementés.
3. Tu as déjà identifié l'endroit où il faut une marge de manœuvre réelle.

Pour définir les temps d'échelle & #160;:
1. Dans la grille temporelle, sélectionnez le **colonne** d'un arrêt principal.
ref: P9_Imagen7.png | full
2. Choisissez un terminal, un en-tête ou un point de connexion important.
3. Définit:
   1. **Minimum**, comme temps d'attente obligatoire.
   2. **Maximum**, comme marge autorisée pour la régulation ou la synchronisation.
4. Enregistre les paramètres.
5. Répétez le processus pour d'autres arrêts principaux où vous avez besoin de rester contrôlé.

Pour le cas de référence, une logique possible serait:
1. **Terminal Nord**
   1. Minimum: 4 min
   2. Maximum: 10 min
2. **Terminal Sud**
   1. Minimum: 5 min
   2. Maximum: 12 min

Lorsque vous avez terminé cette section, vous devriez avoir défini les marges que le moteur peut utiliser pour récupérer ou régler sans déformer la logique de l'horaire.

## Vérifier les créneaux horaires, la vue étendue et la consistance visuelle

Une fois que vous avez déjà des temps de trajet et de séjour, vous devez vérifier si la grille reflète une logique réaliste. Le document souligne que GoalBus inclut des aides visuelles pour détecter les erreurs lorsque vous manipulez de nombreux points de données, de nombreuses bandes ou plusieurs itinéraires.

Avant de continuer, assurez-vous que:
1. Tu as déjà mis en place au moins une bande horaire.
2. Tu as déjà introduit des valeurs minimales, optimales et maximales.
3. Tu as déjà ajouté des temps de séjour aux points pertinents.

Pour vérifier visuellement la cohérence de la configuration:
1. Vérifiez la grille et confirmez que chaque segment principal a une bande horaire valide.
2. Utilisez les aides visuelles disponibles pour détecter les valeurs anormales.
3. Vérifiez si les heures de pointe montrent des temps plus hauts que les heures de vallée.
4. Agrandis la vue si tu as besoin de voir plus de détails ou plus d'arrêts intermédiaires.
5. Corrige toutes les valeurs qui s'écartent directement de la vue ou du panneau d'édition.
6. Répétez la révision jusqu'à ce que la logique temporelle reflète une opération crédible.

Pour le cas de référence, demandez-vous:
1. L'heure de pointe est-elle plus longue que la nuit ?
2. Les temps minimums, optimaux et maximums ont-ils une relation logique ?
3. Les terminaux ont-ils une marge de régulation réaliste?
4. La grille représente-t-elle déjà une journée opérationnelle complète ?

Une fois cette section terminée, vous devriez avoir une base temporelle révisée visuellement et sans incohérences importantes.

## Application de la version temporelle comme référence pour les services

L'objectif ultime de ce quick start n'est pas seulement de créer des données temporaires, mais de laisser une référence qui peut ensuite être utilisée lors de la création ou de la modification de services. Le document indique que chaque voyage doit être mesuré contre un **version temporelle de référence**, et que cette référence est automatiquement utilisée lorsque vous créez de nouveaux voyages ou changez le chemin d'un voyage. Il permet également de détecter des écarts si un voyage a été importé ou modifié en dehors de la norme.

Avant de finir, assurez-vous que:
1. Tu as déjà créé une version temporaire valide.
2. Tu as déjà défini des temps de parcours et de permanence.
3. Tu as vérifié la cohérence de la grille.
4. Tu sais quelle ligne et quelle affaire tu vas utiliser pour créer des services.

Pour vérifier que votre base temporelle est déjà prête pour les services:
1. Vérifie la version du temps que tu viens de créer.
2. Il confirme qu'il est lié au bon jour.
3. Confirmez qu'il inclut les itinéraires ou les variations que vous allez utiliser.
4. Vérifiez que cette version pourrait déjà servir de référence temporaire pour:
   1. créer de nouveaux voyages,
   2. recalculer les temps d'arrivée et de départ,
   3. auditer les écarts par rapport à la norme.
5. Si la réponse est oui, continuez avec le prochain quick start.
6. Si la réponse est non, retournez en arrière et corrigez la version ou vos temps avant de suivre.

Une fois cette section terminée, vous devriez pouvoir affirmer que la ligne dispose déjà d'une version temporelle de référence suffisante pour créer des services de manière cohérente.

## Lectures supplémentaires

- [Création de l'offre de service de base: voyages ou groupes de services par ligne, itinéraire et sens](P10_Création_De_Loffre_De_Service_De_Base_Avec_Voyages_Et_Horaires.md)
