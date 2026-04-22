---
title: Mise en œuvre du premier calcul de Rostering
shortTitle: Calculer Rostering
intro: Apprenez à préparer et à exécuter le premier calcul de Rostering, à vérifier
  si la solution du personnel est viable et à identifier les problèmes qui relèvent
  des règles, de la disponibilité ou du détachement avant de valider l'affectation.
contentType: how-tos
versions:
- '*'
---
## Préparez la base avant de lancer le calcul de Rostering

Avant d'exécuter le calcul, vous devez vérifier que la base de personnel est déjà suffisamment mûre. Rostering ne devrait pas être utilisé pour découvrir les données maîtres manquantes à la dernière minute. Si le modèle, le détachement, les règles ou la disponibilité ne sont pas bien préparés, le calcul échouera ou produira une solution trompeuse.

Utilisez cette quick start lorsque vous avez déjà une solution de Scheduling stable et que vous avez préparé toute la couche de personnel nécessaire pour affecter du travail réel aux conducteurs.

Avant de commencer, assurez-vous que:
1. Tu as déjà fermé la transition depuis Scheduling sur P19.
2. Tu as déjà chargé et vérifié les chauffeurs sur P20.
3. Tu as validé l'adscription opérationnelle sur P21.
4. Tu as déjà défini les règles de Rostering sur P22.
5. Vous avez déjà enregistré des absences, des inactivités et des disponibilités sur P23.
6. Vous avez déjà enregistré des cessions, des transferts ou des changements d'affectation dans P24.
7. Vous savez bien quelle solution Scheduling va être utilisée comme entrée dans le calcul.

Pour ce quick start, utilisez ce cas de référence:

> **Je vais exécuter le premier calcul de Rostering pour la ligne L1, en utilisant une solution de Scheduling déjà stable et une base de conducteurs correctement préparée.**

Pour préparer la base avant le calcul:
1. Ouvre l'environnement ou le module **Rostering**.
ref: P25_Imagen1.png | compact
2. Vérifiez quelle solution Scheduling sera l'entrée du calcul.
3. Il confirme que le groupe de conducteurs qui y participera est disponible et appartient au bon contexte.
4. Vérifiez que les règles de Rostering actives répondent au cas réel.
5. Il vérifie que les absences et les inactivités principales sont déjà enregistrées.
6. Il confirme que les cessions ou transferts pertinents sont déjà pris en compte.
7. Si vous détectez un problème de données maîtres, corrigez-le avant de calculer.

Pour le cas de référence, ne continuez pas jusqu'à ce que vous puissiez affirmer:
1. La solution de L1 n'a plus besoin de changements structurels.
2. Le groupe de conducteurs existe déjà et est prêt.
3. Les règles et les disponibilités représentent déjà la réalité de la période.
4. Tu peux déjà essayer une vraie affectation de travail.

Une fois cette section terminée, vous devriez avoir une base de calcul suffisamment stable pour lancer Rostering.

## Sélectionner la bonne entrée à partir de Scheduling

Rostering a besoin d'une entrée de travail claire. Cette entrée ne devrait pas être un mélange ambigu de scénarios, mais une solution de Scheduling déjà connue et utilisable. À ce stade, l'important est de confirmer que vous allez affecter des personnes au bon travail.

Avant de commencer cette section, assurez-vous que:
1. Vous savez quel scénario ou solution Scheduling vous utiliserez.
2. Tu sais quelle ligne, quel genre de jour ou de contexte tu vas couvrir.
3. Vous pouvez déjà faire la distinction entre la solution existante et une itération non encore consolidée.

Pour sélectionner correctement l'entrée du calcul:
1. Dans le module Rostering, il ouvre la configuration du calcul ou du scénario d'attribution.
2. Sélectionnez la **solution Scheduling** qui agira comme entrée, c'est-à-dire quelle solution est publiée pour une plage de dates.
3. Vérifiez que le type de jour correspond au calcul que vous voulez faire.
4. Vérifiez que la ligne ou l'ensemble de lignes correspondent à l'affaire.
5. S'il y a plusieurs versions possibles, choisissez seulement celle que vous voulez vraiment utiliser comme base.
6. Enregistrez la sélection.
7. Vérifiez que le système montre déjà clairement quel travail sera assigné.

Dans le cas de référence, assurez-vous que:
1. L'entrée correspond à L1 ouvrable.
2. Vous ne mélangez pas une version publiée avec une itération non encore approuvée.
3. Le travail qui arrive à Rostering est exactement celui que tu veux couvrir.

Une fois cette section terminée, vous devriez avoir une entrée de Scheduling bien définie pour le calcul du personnel.

## Configurer le calcul de Rostering avec les règles et le collectif corrects

Une fois l'entrée choisie, vous devez vérifier que le calcul utilise le collectif et les règles correctes. Dans Rostering, une mauvaise combinaison entre collectif, règles et disponibilité peut rendre impossible une solution qui dans Scheduling était correcte.

Avant de commencer cette section, assurez-vous que:
1. Tu as déjà sélectionné l'entrée depuis Scheduling.
2. Tu sais quel groupe de personnel participera.
3. Vous avez déjà défini si vous utilisez des règles de base, avancées ou une combinaison contrôlée.

Pour configurer le calcul de Rostering:
1. Démarrer la configuration du calcul de l'allocation en créant un nouveau scénario de rostering.
2. Sélectionnez les données d'entrée suivantes:
   1. Les **Dépôts** qui participeront.
   2. Sélectionnez les **Dates** du nouveau scénario de rostering.
   3. Vérifiez que **Modèle de règles** s'applique au calcul. Confirmez que les règles actives correspondent au bon groupe.
   4. Ajoutez un **description** pour plus de détails.
3. Enregistre les paramètres.
ref: P25_Imagen2.png | compact(x10)
4. Vérifie si le calcul envisage:
   1. absences,
   2. d'inactivité,
   3. les cessions,
   4. et restrictions de disponibilité.
5. Vérifiez que le calcul a déjà:
   1. le travail d'entrée,
   2. collectif éligible,
   3. règles applicables.

Dans le cas de référence, elle confirme que:
1. Le groupe de conducteurs de L1 est celui qui sera utilisé.
2. Les règles actives sont celles de ce groupe.
3. La configuration ne fait pas glisser des restrictions dans un autre contexte.

Une fois cette section terminée, vous devriez avoir le calcul de Rostering correctement paramétré avant de l'exécuter.

## Mise en œuvre du premier calcul de l &apos; allocation

Maintenant, vous pouvez lancer le calcul. À ce stade, le système essaiera d'attribuer des personnes réelles au travail hérité de Scheduling, dans le respect des règles, de l'affectation et de la disponibilité.

Avant de commencer cette section, assurez-vous que:
1. Tu as choisi la bonne entrée.
2. Tu as déjà défini le collectif et les règles.
3. Vous avez déjà vérifié la base de disponibilité et les changements de contexte.
4. Vous ne manquez plus de données maîtres essentielles.

Pour exécuter le calcul de Rostering:
1. Depuis la scène ou le module de Rostering, lancez l'action **Calculer** ou **Commencer le calcul**.
ref: P25_Imagen3.png | compact(3x)
2. Vérifiez que le système commence à traiter l'affectation.
3. Attends que le calcul soit terminé.
4. Vérifiez si le système retourne:
   1. une solution attribuée,
   2. une solution partielle,
   3. ou un signe clair de conflit.
5. Si le calcul ne génère pas de solution utilisable, ne supposez pas immédiatement qu'il manque du personnel. Vérifiez d'abord:
   1. des règles trop restrictives,
   2. l'affectation incorrecte,
   3. absences mal chargées,
   4. ou cessions et allocations incohérentes.

Dans le cas de référence, elle confirme que:
1. Le calcul de L1 est exécuté sur le collectif attendu.
2. Le système essaie d'attribuer du travail réel à de vraies personnes.
3. Le résultat vous permet de vérifier la faisabilité ou de détecter des conflits spécifiques.

Une fois cette section terminée, vous devriez avoir une première solution de Rostering ou un signal clair d'où se trouve le blocage.

## Interpréter si le problème est de règles, disponibilité ou détachement

Après le calcul, vous devez interpréter correctement le résultat. Tous les bogues ne signifient pas la même chose. Si vous ne distinguez pas bien la cause, vous pouvez corriger dans la mauvaise couche.

Avant de continuer, assurez-vous que:
1. Tu as déjà fait le calcul.
2. Tu as vu si la solution était complète, partielle ou conflictuelle.
3. Vous êtes prêt à diagnostiquer avant de toucher les données.

Pour interpréter correctement le résultat:
1. Si de nombreuses affectations font défaut, vérifiez d'abord le **disponibilité** du personnel.
2. Si le système laisse des personnes qui devraient être valides, vérifiez votre **adscription** et votre **Attributions**.
3. Si l'attribution semble trop rigide ou impossible, vérifiez les **règles de Rostering**.
4. Si le travail hérité semble impossible pour n'importe quel collectif, vérifiez à nouveau si le problème vient de **Scheduling**.
5. Ne pas corriger par intuition. Trouvez d'abord si le problème appartient à:
   1. règles,
   2. la disponibilité,
   3. l'affectation,
   4. ou structure héritée.

Pour le cas de référence, posez-vous ces questions:
1. Les gens manquent-ils vraiment ou sont-ils mal configurés ?
2. La règle que j'ai activée rendait l'affectation impossible ?
3. Est-ce que j'essaie d'utiliser un conducteur dans un contexte où il n'appartient pas ou n'est pas activé ?
4. Le problème existait-il avant d'entrer à Rostering ?

Une fois cette section terminée, vous devriez avoir une première lecture diagnostique du résultat du calcul.

## Laisser la solution prête à l'examen fonctionnel

L'objectif de ce quick start n'est pas encore d'approuver définitivement la solution. L'objectif est d'exécuter le premier calcul et de laisser une base prête pour la révision fonctionnelle: couverture, conflits, équilibre et viabilité.

Avant de finir, assurez-vous que:
1. Tu as déjà fait le calcul.
2. Vous avez vérifié si la solution est complète ou partielle.
3. Vous avez déjà identifié si les problèmes appartiennent à des règles, disponibilité, détachement ou Scheduling.

Pour fermer ce premier calcul de manière utile:
1. Il conserve le résultat du calcul comme base de révision.
2. Ne fais pas de changements massifs sans avoir identifié la cause du problème avant.
3. Décide si l'étape suivante sera:
   1. examiner les conflits de couverture,
   2. ajuster les règles,
   3. corriger les données relatives au personnel,
   4. ou retourner à Scheduling si le problème est structurel.
4. Il traite cette première exécution comme une validation du modèle complet d'attribution.
5. Si la base est raisonnable, il poursuit la révision de la couverture et des conflits.

Pour le cas de référence, ce quick start n'est terminé que lorsque vous pouvez affirmer:
1. Tu as déjà fait le premier calcul de Rostering pour L1.
2. Vous savez si la solution est viable ou partielle.
3. Tu as déjà une hypothèse claire sur l'endroit où se trouvent les principaux conflits.
4. Vous êtes prêt à examiner plus en détail la couverture et les conflits.

Une fois cette section terminée, vous devriez avoir le premier calcul de Rostering et une base claire pour la prochaine phase de révision.

## Lectures supplémentaires

- [Examen des conflits, de la couverture et de la viabilité du personnel](P26_Examen_Des_Conflits_De_La_Couverture_Et_De_La_Viabilité_Du_Personnel.md)
