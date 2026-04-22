---
title: Gestion des transferts, cessions et changements de détachement
shortTitle: Posologie et modifications
intro: Apprenez à gérer les changements de contexte opérationnel des conducteurs en
  faisant la distinction entre transfert, cession et changement d'affectation pour
  que Rostering utilise chaque personne dans le bon domaine sans perdre de traçabilité.
contentType: how-tos
versions:
- '*'
---
## Comprendre la différence entre transfert, cession et changement de détachement

Avant de calculer Rostering, vous devez distinguer correctement les mouvements de personnel entre les contextes opérationnels. Toutes les situations ne signifient pas la même chose. Un conducteur peut continuer à appartenir à son dépôt principal, mais travailler temporairement sur un autre. Vous pouvez également changer de détachement de manière plus stable. Si vous mélangez ces concepts, l'éligibilité du personnel devient confuse et le calcul peut assigner du travail dans le mauvais contexte.

Utilisez cette quick start lorsque vous avez déjà chargé les conducteurs, vérifiez leur détachement principal et modelés leurs absences et leurs inactivités, et vous devez refléter des mouvements réels entre les réservoirs, groupes ou unités.

Avant de commencer, assurez-vous que:
1. Tu as déjà chargé et vérifié les chauffeurs sur P20.
2. Tu as validé l'adscription opérationnelle sur P21.
3. Tu as déjà défini les règles de Rostering sur P22.
4. Vous avez déjà enregistré des absences, des inactivités et des disponibilités sur P23.
5. Tu sais quelles personnes vont changer de contexte et pendant quelle période.

Pour ce quick start, utilisez ce cas de référence:

> **Je vais noter que l'un des conducteurs qui appartient normalement à l'entrepôt nord travaillera temporairement dans un autre contexte, et qu'un autre conducteur changera d'affectation de manière plus stable avant le calcul de Rostering.**

Pour distinguer correctement chaque mouvement:
1. Vous utilisez un **cession** lorsque la personne appartient toujours à votre contexte principal, mais vous travaillerez temporairement sur un autre.
2. Utilisez un **transfert** lorsque la personne change de contexte de manière plus structurelle ou permanente.
3. Utilisez un **changement d'affectation** lorsque vous avez besoin de mettre à jour formellement le dépôt, le groupe ou l'unité de base à partir de laquelle le système doit traiter le conducteur.
4. N'utilisez pas une absence pour modeler un changement de contexte opérationnel.
5. N'utilisez pas une cession pour corriger un détachement principal mal configuré.

Gardez ces questions comme guide:
1. Où appartient normalement cette personne ?
2. Où travaillerez-vous vraiment pendant cette période ?
3. Ce mouvement est-il temporaire ou structurel ?

Quand vous aurez terminé cette section, vous devriez être clair sur le type d'enregistrement correspondant à chaque changement de contexte.

## Enregistrer une cession temporaire du conducteur

La cession est destinée à refléter qu'un conducteur travaillera temporairement en dehors de son contexte habituel sans perdre son détachement de base. Ceci est utile lorsqu'une personne continue d'appartenir à son dépôt, unité ou groupe principal, mais opérera pendant un certain temps dans un autre environnement.

Avant de commencer cette section, assurez-vous que:
1. Tu as déjà identifié la personne qui sera cédée.
2. Tu sais quel est son contexte principal.
3. Vous connaissez le contexte temporel de destination et les dates d'application.

Pour enregistrer une cession temporaire:
1. Ouvre le profil du conducteur sur la liste générale.
2. Voir la section **Mouvements**, **d &apos; affectation temporaire** ou **cessions**, selon la vue disponible.
3. Créez un nouveau registre de cession.
4. Définit:
   1. le **contexte d &apos; origine**,
   2. le **contexte de destination**,
   3. la **Date de début**,
   4. la **Date de fin**,
   5. et toute observation nécessaire.
5. Garde le registre.
6. Vérifiez que le conducteur conserve son détachement principal.
7. Il vérifie que le système peut le traiter dans le contexte temporel correct pendant la période de cession.

Dans le cas d'espèce, une cession valide serait:
1. conducteur attaché à l'entrepôt nord,
2. cédé pendant deux semaines au dépôt Sud,
3. sans changer son affectation principale historique.

Quand vous aurez terminé cette section, vous devriez avoir correctement modelé une cession temporaire sans perdre de traçabilité structurelle.

## Enregistrer un transfert ou un changement plus stable

Contrairement à la cession, un transfert répond à un mouvement plus structurel. Ici, il ne s'agit plus seulement de travailler temporairement dans un autre contexte, mais de déplacer de manière plus stable l'appartenance opérationnelle du conducteur.

Avant de commencer cette section, assurez-vous que:
1. Tu as déjà identifié la personne qui changera de contexte de manière plus durable.
2. Vous savez quel dépôt, unité ou groupe deviendra votre nouveau contexte principal.
3. Tu ne parles plus d'un besoin temporaire ou exceptionnel.

Pour enregistrer un transfert ou un changement structurel:
1. Ouvre le profil du conducteur.
2. Vérifiez votre poste principal actuel.
3. Créez le mouvement de transfert ou mettez à jour l'adscription principale, en fonction du flux utilisé par votre environnement.
4. Définit:
   1. le nouveau **dépôt principal**,
   2. la nouvelle **Unité d &apos; activité**,
   3. le nouveau **Groupe de travail**, s'il change,
   4. et la date d'efficacité.
5. Garde les changements.
6. Vérifiez que le profil reflète déjà le nouveau contexte principal.
7. Vérifie que le changement n'a pas laissé de données contradictoires entre l'affectation principale et l'attribution.

Dans le cas de référence, un transfert valable serait:
1. conducteur qui cesse d'appartenir à l'entrepôt nord,
2. devient un entrepôt Sud stable,
3. et à partir de cette date, il convient de traiter cette nouvelle base comme un recours.

Quand vous aurez terminé cette section, vous devrez avoir correctement modelé un changement structurel de contexte.

## Examiner l'impact du mouvement sur les qualifications et l'éligibilité

Après avoir enregistré des cessions ou des transferts, vous devez vérifier leur impact opérationnel. Déplacer une personne entre les contextes ne sert à rien si ses qualifications ou son éligibilité n'accompagnent pas le changement. Ici, vous devez confirmer que le conducteur non seulement a changé de contexte dans le profil, mais peut également être utilisé correctement dans ce nouvel environnement.

Avant de continuer, assurez-vous que:
1. Tu as déjà enregistré au moins une cession ou un transfert.
2. Tu sais dans quel contexte opérationnel la personne devrait se voir à partir de maintenant.
3. Vous comprenez qu'un changement de contexte peut nécessiter une révision des qualifications existantes.

Pour vérifier l'impact opérationnel du mouvement:
1. Retournez à l'onglet **Compétences/qualifications** du conducteur.
2. Vérifiez s'il existe des qualifications en vigueur pour le contexte de destination.
3. S'ils manquent, ajoutez-les avec des dates correctes avant le calcul.
4. Vérifiez que la personne n'est pas simultanément visible dans des contextes incompatibles avec une erreur de configuration.
5. Vérifie que le système peut considérer la personne éligible dans le cadre correct au cours de la période correspondante.
6. Si vous détectez des contradictions, corrigez-les avant de passer au calcul de Rostering.

Dans le cas de référence, assurez-vous que:
1. le conducteur cédé peut travailler légalement ou techniquement dans le contexte de destination,
2. le conducteur transféré a déjà ses qualifications correspondant au nouveau contexte,
3. l'éligibilité coïncide avec le mouvement enregistré.

Une fois cette section terminée, vous devriez avoir des mouvements de personnel qui sont également utilisables sur le plan opérationnel.

## Confirmant que les changements de contexte sont déjà prêts pour le calcul de Rostering

La dernière étape est de vérifier que la combinaison entre détachement principal, cessions, transferts et qualifications est déjà suffisamment claire pour alimenter le calcul. Ici l'objectif est d'éviter deux erreurs:
1. désigner une personne dans un contexte où elle ne devrait pas apparaître,
2. ou laisser une personne qui devrait être admissible par un changement déjà enregistré.

Avant de finir, assurez-vous que:
1. Tu as déjà enregistré les mouvements temporaires ou structurels nécessaires.
2. Tu as vérifié son impact sur l'éligibilité.
3. Tu sais quel collectif participera au prochain calcul.

Pour confirmer que cette couche est déjà prête:
1. Retourne sur la liste générale des conducteurs.
2. Regardez plusieurs profils affectés par des changements de contexte.
3. Vérifiez que:
   1. les cessions sont considérées comme temporaires,
   2. les transferts se traduisent par des changements structurels,
   3. et le détachement principal reste cohérent le cas échéant.
4. Demandez-vous si le système pourrait déjà:
   1. utiliser le conducteur correct dans le contexte correct,
   2. au cours de la période appropriée,
   3. sans confondre appartenance structurelle avec déplacement temporaire.
5. Si la réponse est oui, continuez avec le prochain quick start.
6. Si la réponse est non, corrigez les mouvements ou les qualifications avant de suivre.

Pour le cas de référence, ne continuez pas jusqu'à ce que vous puissiez affirmer:
1. Les changements de contexte des conducteurs de L1 sont déjà correctement enregistrés.
2. Tu sais qui est cédé, qui a été transféré et qui garde son détachement d'origine.
3. La base est déjà prête à exécuter le premier calcul de Rostering.

Quand vous aurez terminé cette section, vous devriez avoir le contexte organisationnel du personnel suffisamment clair pour passer au calcul de l'affectation.

## Lectures supplémentaires

- [Mise en œuvre du premier calcul de Rostering](P25_Mise_En_Œuvre_Du_Premier_Calcul_De_Rostering.md)
