---
title: Gérer le détachement opérationnel du conducteur
shortTitle: Affectation opérationnelle
intro: Apprenez à lier chaque conducteur à son dépôt, à son unité d'affaires et à
  son groupe de travail, et à comprendre comment cette affectation conditionne son
  éligibilité réelle avant de passer à des règles, absences et calculs de Rostering.
contentType: how-tos
versions:
- '*'
---
## Comprenant le détachement opérationnel du conducteur

Avant de définir des règles avancées, des absences ou des calculs de Rostering, vous devez comprendre comment **détaché** se trouve chaque conducteur au sein de l'organisation. Dans GoalBus, le détachement opérationnel n'est pas basé sur un seul champ. Il est construit en combinant trois coordonnées principales:
1. **Dépôt**
2. **Unité d &apos; affaires**
3. **Groupe de travail**

Cette combinaison définit l'endroit où la personne travaille, la division à laquelle elle appartient et le type de tâches qu'elle peut recevoir. Elle conditionne également la visibilité de la ressource pour les planificateurs et les gestionnaires.

Utilisez cette quick start lorsque vous avez déjà chargé le modèle de conducteur et vous devez vous assurer que chaque personne est située dans le contexte opérationnel correct avant de passer à des règles et disponibilités.

Avant de commencer, assurez-vous que:
1. Tu as déjà chargé et vérifié les chauffeurs sur P20.
2. Vous savez quels dépôts, unités et groupes utilisent votre opération.
3. Tu sais bien quel groupe de personnel participera au calcul de Rostering.
4. Tu sais qu'une mauvaise affectation peut rendre une personne inéligible même si elle existe dans le système.

Pour ce quick start, utilisez ce cas de référence:

> **Je vais vérifier que les conducteurs qui couvriront la ligne L1 sont rattachés à l'entrepôt, à l'unité et au groupe de travail corrects avant de configurer les règles et la disponibilité.**

Pour comprendre le détachement opérationnel:
1. Il traite le **dépôt** comme l'emplacement physique de base de la ressource.
2. Il traite le **Unité d &apos; activité** comme la division stratégique ou modal à laquelle appartient la personne.
3. Il traite le **Groupe de travail** comme la fonction qui détermine le type de tâches que vous pouvez recevoir.
4. Utilisez cette règle de lecture:
   1. le dépôt répond à **Où travaille-t-il ?**,
   2. l'unité répond à **dans quelle entreprise ou mode d'exploitation**,
   3. le groupe répond à **Quel type de travail peut-il faire ?**.
5. Ne mélangez pas ces trois concepts comme si c'était la même chose.

Lorsque vous aurez terminé cette section, vous devrez être sûr que l'affectation opérationnelle est une structure composite et non pas un attribut isolé.  &lt; &lt; Profilecite &gt; &gt; , &lt; &lt; Turn39file1 &gt; &gt; , &lt; &lt; Turn39file3 &gt; &gt; , &lt; &lt; Turn39file3 &gt; &gt; , &lt; &lt; Turn39file3 &gt; &gt;

## Vérification du réservoir, de l'unité et du groupe de travail dans le profil du conducteur

Une fois la logique comprise, vous devez vérifier comment elle est configurée dans le profil réel du conducteur. Ces champs font partie du  &lt; &lt; ADN structurel &gt; &gt; de l &apos; employé et constituent la base de son contexte opérationnel. S &apos; ils sont mal définis, l &apos; affectation ultérieure est contaminée à partir de l &apos; origine. &lt; &lt;  &gt; &gt; , &lt; &lt; Filecite &gt; &gt; , &lt; &lt;turn39file0 &gt; &gt; , &lt; &lt;turn39file2 &gt; &gt;

Avant de commencer cette section, assurez-vous que:
1. Vous avez déjà des chauffeurs créés dans le personnel.
2. Tu sais quel conducteur ou quel groupe tu utiliseras comme échantillon.
3. Vous voulez vérifier l'affectation structurelle, pas encore une cession temporaire.

Pour vérifier l'adscription dans le profil & #160;:
1. Sur la liste générale des conducteurs, il ouvre le profil d'une personne.
2. Vérifiez la barre latérale de données structurelles.
3. Vérifiez au moins:
   1. **Dépôt principal**
   2. **Unité d &apos; affaires**
   3. **Groupe de travail**
   4. **Zone**, si votre opération l'utilise
4. Il confirme que ces valeurs correspondent au contexte réel dans lequel la personne devrait travailler.
5. Si une donnée est incorrecte, mettez-la à jour dans le profil.
6. Garde les changements.
7. Répétez l'examen sur plusieurs conducteurs pour confirmer que le modèle est cohérent.

Dans le cas de référence, il constate que:
1. Les conducteurs de L1 appartiennent au bon dépôt.
2. L'unité d'affaires correspond au mode ou à l'entreprise attendu.
3. Le groupe de travail correspond réellement à **Conducteurs** et non à un autre rôle.

Lorsque vous aurez terminé cette section, vous devrez revoir l'affectation structurelle des conducteurs qui participeront au calcul.  &lt; &lt; Filecite &gt; &gt; , " &lt; &lt; Turn39file1 &gt; &gt; , &lt; &lt; Turn39file2 &gt; &gt; , &lt; &lt; Turn39file2 &gt; &gt; .

## Comprendre la différence entre détachement principal, habilitation et cession

Avant d'aller plus loin, vous devez distinguer trois concepts qui sont souvent confondus:
1. **Inscription principale**
2. **Activation**
3. **Cession ou transfert temporaire**

L'adjectif principal définit l'endroit où appartient la personne de manière structurelle. L'habilitation répond à la question de savoir si **peut** travailler légalement ou techniquement dans un autre contexte. La cession répond à l'endroit où **Il travaille vraiment.** pendant une période temporaire. Ces trois couches cohabitent, mais ne signifient pas la même chose.

Avant de commencer cette section, assurez-vous que:
1. Tu as vérifié l'inscription principale sur le profil.
2. Vous savez que certaines personnes peuvent travailler en dehors de leur contexte principal.
3. Vous voulez éviter les erreurs d'interprétation entre  &lt; &lt;  &gt; &gt; et &lt; &lt; &lt; &gt; &gt; , &lt; &lt; &lt; &gt; &gt; , &lt; &lt; &lt; &gt; &gt; et &lt; &lt; &lt; &gt; &gt; , &lt; &lt; &lt; &gt; &gt; , &lt; &lt; &lt; &gt; &gt; , &lt; &lt; &lt; &gt; &gt; , &lt; &lt; &lt; &gt; &gt; , &lt; &lt; &lt; &gt; &gt; , &gt; &gt; .

Pour bien distinguer ces concepts:
1. Utilisez le **l'adscription principale** pour décrire le contexte structurel de base du conducteur.
2. Utilisez le **habilitation** pour indiquer que le conducteur peut travailler dans un autre réservoir, groupe ou unité.
3. Utilisez le **cession** pour indiquer que le conducteur est temporairement déplacé dans un autre contexte.
4. N'utilisez pas une cession pour corriger un détachement principal mal défini.
5. N'utilisez pas une qualification comme un transfert actif.
6. Gardez ces questions comme guide:
   1. Où appartient cette personne? → détachement principal
   2. Où puis-je travailler légalement ? → habilitation
   3. Où travaillez-vous en ce moment ? → cession

Pour le cas de référence, demandez-vous:
1. Le conducteur appartient à l'entrepôt Nord ?
2. Pouvez-vous travailler dans un autre dépôt si nécessaire ?
3. Est-il temporairement cédé à une autre base ou continue-t-il dans son contexte habituel?

Une fois cette section terminée, vous devriez avoir une bonne lecture de la hiérarchie entre l'affectation, l'habilitation et la cession.

## Validant que l'adscription permet de visualiser et d'affecter correctement le conducteur

Le détachement ne sert pas seulement à décrire le profil du conducteur. Il conditionne également la façon dont le système le voit et les tâches qu'il peut recevoir. Une personne mal rattachée peut rester en dehors du filtre correct, apparaître au mauvais endroit ou recevoir des tâches qui ne lui reviennent pas. Il peut également arriver qu'une personne valide soit cachée ou inéligible par une affectation mal définie.  &lt; &lt; Filecite &gt; &gt; , &lt; &lt; Turn39file3 &gt; &gt; , &lt; &lt; L1 &gt; &gt; , &lt; &lt; L2 &gt; &gt; , &lt; &lt; L2 &gt; &gt; , &lt; &lt; L2 &gt; &gt; , &lt; &lt; L2 &gt; &gt; , &lt; &lt; L2 &gt; &gt; , &lt; &lt; L2 &gt; &gt; , &lt; &lt; L2 &gt; &gt; &gt; &gt; &gt; .

Avant de continuer, assurez-vous que:
1. Tu as vérifié l'entrepôt, l'unité et le groupe sur plusieurs profils.
2. Vous comprenez la différence entre détachement et cession.
3. Tu as déjà compris quel collectif participera au prochain calcul.

Pour valider l'impact opérationnel de l'inscription:
1. Vérifiez quel ensemble de conducteurs devrait être visible dans le contexte de votre calcul.
2. Vérifiez que les bonnes personnes apparaissent sous le bon dépôt, l'unité et le groupe.
3. Vérifie s'il y a des conducteurs dans le mauvais groupe.
4. Vérifiez s'il y a des conducteurs qui devraient appartenir au contexte et ne pas apparaître en tant que tels.
5. Si vous détectez une erreur d'adsignation, corrigez-la avant de passer à des règles ou disponibilités.
6. Enregistrez la configuration finale des profils affectés.

Dans le cas de référence, assurez-vous que:
1. Les conducteurs qui couvriront L1 apparaissent dans le contexte opérationnel correct.
2. Ils ne se mélangent pas avec des collectifs qui ne devraient pas recevoir de tâches de conduite.
3. Le système pourrait filtrer et affecter uniquement le personnel concerné.

Une fois cette section terminée, vous devriez avoir une base d'affectation opérationnelle qui aide le système à voir et à utiliser les bonnes personnes.  &lt; &lt; Profilecite &gt; &gt; , &lt; &lt;  &lt;  &gt; &gt; , &lt; &lt;  &gt; &gt; , &lt; &lt;  &gt; &gt; , &lt; &lt; , &lt; , &lt; , &gt; &gt; , &lt; &lt; , &gt; &gt; , &lt; &lt; , &lt; , &gt; &gt; , &lt; &lt; , &gt; &gt; , &lt; &lt; , &lt; , &lt; , &gt; &gt; , &gt; , &gt; , &lt; &lt; , &lt; &lt; , &gt; &gt; , &gt; , &gt; , &gt; , &gt; , &gt; .

## Confirmant que le détachement opérationnel est déjà prêt pour le calque suivant

La dernière étape consiste à vérifier que le détachement est resté suffisamment solide pour continuer avec des règles, des absences et des calculs. Ici, l'objectif n'est pas seulement d'avoir rempli des champs, mais d'avoir laissé une structure claire que le moteur peut interpréter sans ambiguïté.

Avant de finir, assurez-vous que:
1. Tu as déjà vérifié l'affectation structurelle des profils clés.
2. Vous distinguez déjà l'affectation, l'habilitation et la cession.
3. Tu as déjà confirmé que le collectif visible est le bon.
4. Tu as déjà corrigé les défauts principaux.

Pour confirmer que le détachement est déjà prêt:
1. Retourne sur la liste générale des conducteurs.
2. Vérifiez que le collectif pertinent pour votre affaire apparaît dans le contexte correct.
3. Vérifiez qu'il n'y a pas d'erreur évidente de dépôt, d'unité ou de groupe.
4. Demandez-vous si le système pourrait déjà:
   1. filtrer correctement les conducteurs de l'affaire,
   2. de leur appliquer les règles du bon collectif,
   3. et de les traiter comme base de disponibilité et de calcul.
5. Si la réponse est oui, continuez avec le prochain quick start.
6. Si la réponse est non, corrigez le détachement avant de suivre.

Pour le cas de référence, ne continuez pas jusqu'à ce que vous puissiez affirmer:
1. Les conducteurs de L1 sont rattachés au bon contexte.
2. Tu sais distinguer qui est à la maison, qui peut travailler et qui est cédé.
3. La base est déjà prête à appliquer les règles de Rostering et de disponibilité.

Une fois cette section terminée, vous devriez avoir un détachement opérationnel suffisamment clair pour continuer avec la couche suivante du processus.

## Lectures supplémentaires

- [Définir les règles de Rostering pour l'affectation du personnel](P22_Définir_Les_Règles_De_Rostering_Pour_Laffectation_Du_Personnel.md)
