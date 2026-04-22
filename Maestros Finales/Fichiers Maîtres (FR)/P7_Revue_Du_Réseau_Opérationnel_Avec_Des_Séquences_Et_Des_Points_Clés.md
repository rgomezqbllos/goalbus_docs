---
title: Revue du réseau opérationnel avec des séquences et des points clés
shortTitle: Réseau opérationnel
intro: Apprenez à valider la façon dont votre réseau fonctionne réellement, en vérifiant
  les séquences, les permissions d'arrêt et les points de relais avant de passer à
  des temps et des services.
contentType: how-tos
versions:
- '*'
---
## Vérification de la séquence opérationnelle des routes

Maintenant que vous avez déjà créé le réseau de base (arrêts, lignes et itinéraires), l'étape suivante est de valider que ce réseau fonctionne correctement du point de vue opérationnel.

À ce stade, vous ne créez plus de structure, vous validez la façon dont il se comporte dans la pratique.

Avant de commencer:
1. Tu as déjà créé des arrêts, des lignes et des routes sur P6.
2. Tu as au moins une route par sens.
3. Tu sais quelle ligne tu prépares.

Cas & #160;:
> Valider que la route L1 a une séquence cohérente et opérationnelle avant de définir des temps.

Étapes & #160;:
1. Ouvre la ligne sur laquelle tu travailles.
2. Accédez à la vue des routes.
ref: P7_Imagen1.png | full
3. Choisissez un sens.
4. Vérifiez la séquence d'arrêts.
5. Vérifiez que:
   - Il ne manque pas d'arrêts clés.
   - Il n'y a pas de doublons inutiles.
   - L'ordre est correct.
6. Répétez pour l'autre sens.

Résultat escompté:
- Une séquence propre et logique représentant le parcours réel.

## Validation des permis d'arrêt

Tous les arrêts ne fonctionnent pas de la même façon, certaines permettent une montée, d'autres une descente, et d'autres les deux.

Avant de continuer:
1. Tu as validé la séquence.
2. Tu sais comment ça marche dans la réalité.

Étapes & #160;:
1. Sur la route, vérifiez chaque arrêt.
2. Configurez si vous permettez & #160;:
   - Remontée
   - Descends.
   - Les deux
ref: P7_Imagen2.png | compact
3. Assure-toi que:
   - Terminaux permettent les deux.
   - Arrêts intermédiaires reflètent l'opération réelle.
4. Garde les changements.

Résultat escompté:
- Chaque arrêt a un comportement cohérent avec l'opération.

## Définir des points de relais

Les points de relais sont critiques pour le rostering et l'opération.

Avant de commencer:
1. Tu as déjà une séquence validée.
2. Tu sais où des relais se produisent dans la vraie opération.

Étapes & #160;:
1. Identifiez les arrêts où des changements de conducteur sont effectués.
2. Marquez ces arrêts comme des points de relais.
ref: P7_Imagen3.png | compact
3. Vérifiez que:
   - Ils sont bien placés.
   - Ça suffit pour l'opération.
4. Garde-la.

Résultat escompté:
- Le réseau contemple déjà l'endroit où des changements de conducteur peuvent être effectués.

## Validation finale du réseau opérationnel

Avant d'avancer:

1. Regarde la route.
2. Confirme:
   - C'est la bonne séquence.
   - Permissions cohérentes.
   - Relévés définis.
3. Demande-toi:
   - Pourriez-vous opérer cette ligne dans la vraie vie ?
   - Y a-t-il des détails opérationnels ?

Si la réponse est oui, vous pouvez continuer.

## Lectures supplémentaires

- P8 Chargement des voyages à vide et des déplacements
