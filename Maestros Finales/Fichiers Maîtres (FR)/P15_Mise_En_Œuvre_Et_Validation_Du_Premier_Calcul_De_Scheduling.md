---
title: Mise en œuvre et validation du premier calcul de Scheduling
shortTitle: Calculer et valider
intro: Apprenez à exécuter le premier calcul de Scheduling, à revoir le cycle de vie
  du scénario, à valider la solution préparée et à préparer le scénario pour la publication
  ou l'audit ultérieur.
contentType: how-tos
versions:
- '*'
---
## Mise en œuvre du calcul du scénario

Maintenant que vous avez déjà le scénario créé et configuré avec l'offre validée, les matrices correctes et les modèles de règles de véhicules et de tours, l'étape suivante est d'exécuter le calcul.

À ce stade, le moteur prend:
1. l'offre validée,
2. les règles actives,
3. la logistique des voyages à vide,
4. et la structure de la scène,

pour construire des tâches logiques programmables.

Utilisez cette quick start lorsque vous avez déjà préparé le scénario de Scheduling et vous devez obtenir la première solution calculée avant de la vérifier et de la valider.

Avant de commencer, assurez-vous que:
1. Tu as déjà créé la scène en P14.
2. Vous avez déjà sélectionné le bon service validé.
3. Tu as déjà attribué la bonne matrice de voyages à vide.
4. Tu as déjà choisi le bon modèle de règles de véhicules.
5. Tu as déjà choisi le bon modèle de règles de service.
6. Vous avez déjà configuré le moteur Classic et les paramètres de calcul.

Pour ce quick start, utilisez ce cas de référence:

> **Je vais exécuter le premier calcul du scénario de Scheduling de la ligne L1, vérifier si la solution est cohérente et laisser le scénario prêt à être validé.**

Pour exécuter le calcul du scénario:
1. Ouvre la scène que tu veux calculer.
2. Vérifiez une dernière fois que les entrées de la scène sont correctes.
3. Lancez l'action **Calculer** ou **Commencer le calcul**.
ref: P15_Imagen1.png | compact(3x)
ref: P15_Imagen2.png | compact
4. Vérifiez que l'état du scénario passe de **Solution en instance** à **Calcul de la solution**.
ref: P15_Imagen3.png | full
ref: P15_Imagen4.png | full
5. Attends que le moteur finisse le processus.
ref: P15_Imagen5.png | compact(1x18)
6. Vérifie le nouvel état de la scène.
7. Si le calcul se termine correctement, il confirme que le scénario passe à **Solution préparée**.
ref: P15_Imagen6.png | compact(x7)
8. Si la solution nécessite des réglages manuels, entrez dans l'état **Édition** pour raffinement.
9. Si le moteur ne retourne pas une solution valide, vérifiez à nouveau:
   1. l'offre,
   2. la matrice des voyages à vide,
   3. les règles,
   4. et les paramètres de la scène.

Dans le cas de référence, elle confirme que:
1. La scène de L1 sort de l'état initial.
2. Le moteur termine le calcul sans se verrouiller.
3. Le scénario atteint une solution préparée ou une phase d'édition raisonnable.

En outre, dans le cas où le type de scénario choisi est pour les véhicules et pour les tours, on peut voir la solution générée par les tours de vue du personnel.
ref: P15_Imagen12.png | compact

Une fois cette section terminée, vous devriez avoir une première solution calculée ou un signal clair de la partie de la paramétrage qui doit être corrigée.

## Examiner l'état du scénario et le résultat du calcul

Après avoir exécuté le calcul, vous devez comprendre à quel point le scénario est resté dans le cycle de vie. C'est important parce que chaque état a une signification opérationnelle différente et vous dit quelles actions vous pouvez faire ci-dessous.

Avant de commencer cette section, assurez-vous que:
1. Tu as déjà fait le calcul.
2. Tu connais le nom de la scène que tu vérifies.
3. Tu sais si tu t'attendais à une solution prête ou à une phase de raffinement.

Pour vérifier l'état et le résultat:
1. Retournez à la table principale des scénarios ou restez à l'intérieur de la scène.
2. Vérifie l'état actuel.
3. Interprétez l'état selon cette logique:
   1. **Solution en instance**: le scénario n'a pas encore été calculé.
   2. **Calcul de la solution**: le moteur traite la solution.
   3. **Édition**: Un utilisateur ajuste manuellement la solution.
   4. **Solution préparée**: la phase de calcul ou d'édition est terminée et le scénario est prêt à être révisé.
   5. **Validation**: la solution a déjà été approuvée et bloquée.
   6. **Publication**: la solution est en cours d'incorporation dans le calendrier opérationnel.
   7. **Publié**: la solution a déjà été implantée dans l'opération.
4. Si le scénario est sur **Solution préparée**, continuez avec l'examen de cohérence.
5. Si le scénario est sur **Édition**, les réglages manuels nécessaires sont terminés d'abord.
6. Si le scénario suit **Calcul de la solution** trop longtemps, vérifiez s'il y a eu une incidence technique ou une configuration trop restrictive.

Dans le cas de référence, vous devriez vous attendre à ce que le scénario se termine au moins par:
1. **Solution préparée**, si vous n'avez plus besoin de toucher la structure,
2. ou **Édition**, si vous voulez encore raffiner manuellement.

Une fois cette section terminée, vous devriez comprendre clairement ce que signifie l'état actuel du scénario et ce qu'il faut faire ensuite.

## Vérification de la KPI, des erreurs et de la consistance avant validation

Avant de valider le scénario, vous devez le vérifier. Valider n'est pas un simple clic administratif. C'est la porte d'approbation formelle qui gèle la solution et évite les changements accidentels ultérieurs.

Avant de commencer cette section, assurez-vous que:
1. La scène est déjà sur **Solution préparée** ou vous avez terminé la phase **Édition**.
2. Tu sais qu'après validation, le scénario ne sera plus modifiable.
3. Tu es prêt pour un examen final avant l'approbation.

Pour vérifier la solution avant de la valider:
1. Ouvre la scène dans son état actuel.
2. Vérifiez les KPI disponibles.
ref: P15_Imagen7.png | full
3. Vérifiez s'il y a des erreurs, des avertissements ou des incohérences visibles.
ref: P15_Imagen8.png | compact(x7)
4. Utilisez les filtres disponibles pour inspecter la solution sous différents angles.
ref: P15_Imagen9.png | compact(3x)
5. Vérifiez que les affectations et la structure du scénario ont un sens opérationnel.
6. Si vous détectez un problème mineur et que le scénario est encore modifiable, corrigez-le avant de continuer.
7. Si vous détectez un problème majeur après l'avoir bloqué plus tard, vous devez le déverrouiller avec des permissions appropriées ou revenir à un scénario modifiable.

Dans le cas de référence, assurez-vous que:
1. Les KPI de la solution de L1 sont raisonnables.
2. Il n'y a pas d'erreurs graves qui invalident la solution.
3. La solution peut d'ores et déjà passer de la révision technique à l'approbation formelle.

Quand tu auras fini cette section, tu devrais avoir assez de confiance pour valider le scénario.

## Validation de la scène et blocage de la solution

Maintenant, vous pouvez exécuter le **validation du scénario**. Cette étape marque la fermeture officielle de la phase de calcul et d'édition. À partir d'ici, la solution devient protégée, le scénario cesse d'être modifiable et ne peut plus être recalculé tant qu'il reste validé.

Avant de commencer cette section, assurez-vous que:
1. La scène est sur **Solution préparée**.
2. Tu as fini l'examen de KPI et les erreurs.
3. Vous n'avez pas besoin d'autres réglages manuels avant d'approuver la solution.

Pour valider le scénario:
1. À partir de la table des scénarios, ouvrez le menu des actions de la scène.
2. Sélectionnez **Valider**.
3. Si vous préférez le faire à partir de la scène, utilisez le bouton **Valider** en haut de l'écran.
ref: P15_Imagen10.png | compact(2x)
4. Il confirme la validation à la demande du système.
5. Vérifiez que l'état de la solution du scénario passe à **Validationa**.
ref: P15_Imagen11.png | compact(2x)
6. Vérifie ce qui suit:
   1. le scénario n'est plus modifiable,
   2. Il ne peut plus se recalculer.
   3. et leurs données principales sont protégées.
7. Si vous découvrez une erreur de dernière minute après validation, utilisez le flux de déverrouillage uniquement avec les permissions appropriées.

Pour le cas de référence, ne continuez pas tant que vous ne pouvez pas affirmer:
1. La solution de L1 a déjà été révisée.
2. La solution du scénario est passée à l'état **Validationa**.
3. L &apos; organisation peut déjà considérer ce scénario comme une version approuvée.

Une fois cette section terminée, vous devriez avoir une solution officiellement approuvée et bloquée afin d'éviter des changements accidentels.

## Laisser le scénario prêt pour la publication ou l'audit ultérieur

Une fois validé, la scène est déjà prête pour deux chemins:
1. **publication**, si vous voulez l'emmener au calendrier opérationnel réel,
2. ou **d &apos; audit**, si vous avez encore besoin de le consulter avant de le publier.

À ce stade, le scénario est une solution approuvée et protégée. Vous pouvez toujours le consulter, vérifier KPI, filtrer et l'utiliser comme référence, mais vous ne devriez plus le traiter comme un projet de travail.

Avant de finir, assurez-vous que:
1. La solution du scénario est déjà dans l'état **Validationa**.
2. Vous connaissez la différence entre la validation et la publication.
3. Vous savez si votre prochaine étape sera d'implémenter la solution ou de continuer à l'examiner.

Pour laisser le scénario prêt pour l'étape suivante:
1. Vérifiez la table des scénarios et confirmez l'état **Validationa**.
2. Si le plan est déjà approuvé pour l'implantation, préparez le flux de **Publier**.
3. Si vous avez encore besoin d'un examen interne, gardez le scénario validé comme base d'audit.
4. Utilisez les filtres, les icônes d'information et la révision des états pour contrôler les scénarios en attente, validés ou déjà publiés.
5. Si vous avez besoin de lire une nouvelle version, envisagez de doubler le scénario au lieu d'en modifier un déjà approuvé.

Pour le cas de référence, ce quick start n'est terminé que lorsque vous pouvez affirmer:
1. Le scénario de L1 a déjà été calculé.
2. La solution a été révisée.
3. La solution du scénario est **Validationa**.
4. L'étape suivante n'est plus de calculer, mais de décider s'il est publié ou s'il est audité.

Quand vous aurez terminé cette section, vous devriez avoir un scénario calculé, révisé et validé, prêt pour votre passage à la production ou à la révision finale.

## Lectures supplémentaires

- [Publier le scénario à des dates précises](publicacion-del-escenario)
