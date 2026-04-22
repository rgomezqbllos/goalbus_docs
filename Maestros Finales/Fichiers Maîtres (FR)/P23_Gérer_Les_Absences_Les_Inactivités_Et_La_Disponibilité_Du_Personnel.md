---
title: Gérer les absences, les inactivités et la disponibilité du personnel
shortTitle: Disponibilité personnelle
intro: Apprenez à enregistrer des absences, des inactivités et des restrictions de
  disponibilité afin que Rostering n'attribue que des personnes réellement éligibles
  et n'essaie pas de couvrir le travail avec des conducteurs non disponibles.
contentType: how-tos
versions:
- '*'
---
## Comprendre la différence entre absence, inactivité et disponibilité

Avant de calculer Rostering, vous devez contrôler quelles personnes sont réellement disponibles pour travailler. Dans cette couche, il ne suffit plus que le conducteur existe, soit attaché au bon contexte et ait des règles applicables. Vous devez également dire au système si cette personne:
1. est disponible,
2. il est absent,
3. est inactive,
4. ou a une disponibilité partielle ou restreinte.

Utilisez cette quick start lorsque vous avez déjà chargé les conducteurs, vérifiez leur détachement opérationnel et préparez la base de règles de Rostering, et vous devez empêcher le calcul d'affecter du travail à des personnes non éligibles.

Avant de commencer, assurez-vous que:
1. Tu as déjà chargé et vérifié les chauffeurs sur P20.
2. Tu as déjà validé son détachement opérationnel sur P21.
3. Tu as déjà défini la base des règles de Rostering sur P22.
4. Tu sais bien quel groupe de personnel participera au calcul.
5. Vous savez si dans votre opération vous avez besoin d'enregistrer des vacances, des congés, des congés, des troubles partiels ou des états non opérationnels.

Pour ce quick start, utilisez ce cas de référence:

> **Je vais enregistrer des absences, des inactivités et des restrictions de disponibilité sur les conducteurs qui couvriront la ligne L1 pour m'assurer que Rostering n'emploie que des personnes réellement éligibles.**

Pour bien comprendre ces concepts:
1. Il utilise un **absence** lorsque la personne existe et appartient au collectif, mais il n'est pas disponible pendant une période donnée.
2. Utilisez un **Inactivité** lorsque la personne doit rester hors de l'opération pendant une période plus structurelle ou ne pas participer au calcul.
3. Utilisez un **limitation de la disponibilité** lorsque la personne peut travailler, mais pas à tout moment ou pas sous toutes les conditions.
4. Ne mélangez pas ces concepts comme si c'était la même chose.
5. Utilisez cette règle de lecture:
   1. **absence** = ne peut pas travailler pendant une période donnée,
   2. **Inactivité** = ne doit pas être considéré comme une ressource opérationnelle dans ce contexte ou cette période,
   3. **disponibilité restreinte** = peut travailler, mais avec des limites.

Pour enregistrer les types d'absences, d'inactivité ou d'inactivité:
1. Sous GoalBus, vous devez ouvrir **Configuration** > **Personnel** > **Configuration des absences**.
ref: P23_Imagen1.png | compact
2. Vérifie si tous les types d'absence dont tu as besoin sont créés.
3. S'il n'y a pas d'absence ou si vous devez en créer de nouveaux, cliquez sur le bouton **Créer une nouvelle absence**.
ref: P23_Imagen2.png | compact(2x)
4. Pour créer un nouveau type d'absence, les champs suivants doivent être remplis:
   1. **Nom d &apos; absence**: nom du type d'absence à créer.
   2. **Nom court**: pour une vue compacte.
   3. **GoalDriver ID**: code interne si vous travaillez avec des intégrations.
   4. **Catégorie d &apos; absence**: peut être **Pure**, **Libre** ou **Travail**. En fonction de ce que vous choisissez, une durée (**Horaire** ou **Journée complète**), une durée de **Temps de travail** ou de **Maximum de jours** doit être assignée.
   5. **Éligibilité pour l'attribution du travail**: si vous pouvez choisir le conducteur pour lui assigner du travail ou non, en dépit de son absence.
   6. Sélectionnez si ce type d'absence sera **Sollicitable par le conducteur**.
5. Garde le nouveau type d'absence.
ref: P23_Imagen3.png | compact(x10)
6. Il continue d &apos; enregistrer tous les types d &apos; absence nécessaires.
7. Confirmez que vous avez tous les types d'absence nécessaires pour votre planification.

Une fois cette section terminée, vous devriez avoir une vision claire du type d'absences que vous pourrez utiliser dans votre planification de rostering et que vous serez en mesure d'attribuer aux différents conducteurs.  &lt; &lt; Fivefilecite &gt; &gt; 22file3 &lt; &lt; L1 &gt; &gt; , &lt; &lt; L2 &gt; &gt; , &lt; &lt; L1 &gt; &gt; , &lt; &lt; L1 &gt; &gt; , &lt; &lt; L1 &gt; &gt; , &lt; &lt; L1 &gt; &gt; , &lt; &lt; L1 &gt; &gt; , &lt; &lt; L118 &gt; &gt; , &lt; &lt; L1 &gt; &gt; .

## Enregistrer les absences planifiées du conducteur

Les absences planifiées sont l'un des premiers éléments que vous devez charger avant le calcul de Rostering. Ici entrent les vacances, les permissions, les incapacités, les congés ou toute autre période où une personne ne doit pas recevoir de travail.

Avant de commencer cette section, assurez-vous que:
1. Vous savez quels conducteurs auront des absences dans l'horizon de calcul.
2. Vous connaissez les dates exactes ou approximatives de ces absences.
3. Vous voulez laisser le système sans ambiguïté sur quels jours la personne ne peut pas être utilisée.
4. Tu as déjà créé tous les types d'absence nécessaires.

Pour enregistrer des absences dans le profil du conducteur:
1. Sous GoalBus, vous devez ouvrir **Configuration** > **Personnel** > **Gestion des conducteurs**.
ref: P23_Imagen4.png | compact
2. Cliquez sur le bouton de la barre supérieure pour charger les données d'absence.
ref: P23_Imagen5.png | compact(3x)
3. Sélectionnez l'action **Charger les absences de personnel**.
ref: P23_Imagen6.png | compact
4. Chargez le fichier des absences de personnel dans la fenêtre contextuelle. Dans cette fenêtre, vous pouvez vérifier le format du fichier des absences, soit en lisant les instructions, soit en téléchargeant un modèle d'exemple.
ref: P23_Imagen7.png | full
5. Confirmez le chargement du fichier.
6. Garde le registre.
7. Vous pouvez maintenant vérifier les absences chargées dans le profil de chaque conducteur.

Pour le cas de référence, une logique minimale pourrait être:
1. Conducteur A: vacances de 10 à 20
2. Conducteur B: permission le 14ème jour
3. Chauffeur C: incapacité pendant une semaine donnée

Quand vous aurez terminé cette section, vous devriez avoir enregistré les principales absences qui affectent le calcul de Rostering.

## Vérifiant que Rostering voit déjà correctement l'éligibilité réelle

La dernière étape est de valider que la combinaison entre conducteurs, détachements, règles et disponibilité reflète déjà la réalité du calcul. Ici l'objectif est de vous assurer que Rostering ne tentera pas d'attribuer du travail à des personnes absentes, inactives ou mal réglementées, et ne laissera pas de personnes qui devraient être éligibles.

Avant de finir, assurez-vous que:
1. Tu as déjà enregistré des absences importantes.
2. Vous avez déjà configuré des disponibilités partielles si nécessaire.
3. Tu sais quel collectif utilisera le prochain calcul.

Pour vérifier que la disponibilité réelle est déjà bien modelée:
1. Retourne sur la liste générale des conducteurs.
2. Vérifie plusieurs profils représentatifs du collectif.
3. Il confirme que les personnes absentes ont leurs périodes correctement enregistrées.
4. Il confirme que les restrictions partielles ne sont pas modelées comme des absences totales par erreur.
5. Demandez-vous si le système pourrait déjà:
   1. exclure ceux qui ne doivent pas travailler,
   2. y compris ceux qui peuvent travailler,
   3. et respecter des restrictions partielles sans rompre le calcul.
6. Si la réponse est oui, continuez avec le prochain quick start.
7. Si la réponse est non, corrigez les enregistrements avant de suivre.

Pour le cas de référence, ne continuez pas jusqu'à ce que vous puissiez affirmer:
1. Les conducteurs de L1 ont déjà bien reflété leur disponibilité réelle.
2. Les absences sont chargées.
3. Les inactivités sont différenciées.
4. Les restrictions partielles n'ont pas été confondues avec des absences complètes.

Une fois cette section terminée, vous devriez disposer d'une base de disponibilité suffisamment fiable pour passer à des cessions, transferts et changements de détachement.

## Lectures supplémentaires

- [Gestion des transferts, cessions et changements de détachement](P24_Gestion_Des_Transferts_Cessions_Et_Changements_De_Détachement.md)
