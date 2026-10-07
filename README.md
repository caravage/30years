# Thirty Years of Misery – galerie des cartes

Galerie web des 125 cartes du jeu *Thirty Years of Misery* (Brian Asklev, © 2026 VUCA Games, LLC), extraites du module VASSAL `Thirty Years of Misery V1.vmod` (module VASSAL de Kevin Conway).

Ouvrir `index.html` dans un navigateur : aucune installation n'est nécessaire.

## Fonctions

- Recherche plein texte, insensible aux accents, dans le titre, le moment de jeu, l'effet et le texte d'ambiance, avec surlignage. Plusieurs mots sont combinés (ET). La touche `/` place le curseur dans la recherche.
- Filtres combinables : faction, paquet (Westphalie, A, B, Troubles A à D), moment de jeu (début de tour, bataille, phase religieuse, round, autre).
- Tris : faction puis numéro, nom, cavalier, botte, cavalier + botte, numéro.
- Deux affichages : grille des cartes ou liste avec le texte complet.
- Visionneuse : clic sur une carte, flèches ← → pour naviguer.

## Contenu

| Paquet | Cartes |
|---|---|
| Impériaux | 27 |
| Ligue catholique | 26 (la n° 25 n'existe pas dans le module) |
| France | 27 |
| Suède | 27 |
| Troubles allemands (A à D) | 18 |

## Paquets A et B

Chaque faction a deux paquets d'événements. Le paquet A est utilisé dès le début de la partie. Les cartes B sont mélangées dans les paquets quand la carte Troubles « Sweden Enters the War » est tirée. On les reconnaît au petit losange « B » imprimé en bas à droite. La carte n° 1 de chaque faction (Treaty of Westphalia) est classée à part, dans « Westphalie ».

Dans le module VASSAL, chaque carte est rattachée au paquet A ou B par un prototype (`def_Card_Sweden_A`, `def_Card_France_B`…). Ce rattachement ne correspond pas toujours à ce qui est imprimé sur les cartes :

| Faction | Paquet B selon le module | Losange B imprimé sur |
|---|---|---|
| Impériaux | 20 à 27 | 20 à 27 |
| Ligue catholique | 20 à 27 | 20 à 27 |
| France | 20 à 27 | **19** à 27 |
| Suède | 20 à 27 | **19** à 27 |

Les cartes France n° 19 (*Annus Horribilis*) et Suède n° 19 (*Swedish Training*) portent le losange B, alors que le module les place dans le paquet A. La galerie suit ce qui est imprimé sur les cartes. Elle classe donc ces deux cartes en B. France et Suède ont ainsi 9 cartes B chacune, contre 8 pour les Impériaux et 7 pour la Ligue (à cause de la carte n° 25 manquante).

## Régénérer la page

Le texte des cartes n'existe que dans les images. Il a été transcrit à la main, en anglais d'origine, dans `tools/cards_*.txt` (une ligne par carte, champs séparés par `|`). Pour corriger une coquille, modifiez le fichier `.txt` concerné puis lancez :

```bash
python tools/build.py
```

Pour réexporter aussi les images depuis le module décompressé (nécessite Pillow) :

```bash
python tools/build.py chemin/vers/vmod/images
```

Syntaxe des transcriptions : `[G]`, `[I]`, `[CL]`, `[Sp]`, `[Sw]`, `[F]`, `[S]` pour les unités ; `{imp}`, `{cl}`, `{fra}`, `{swe}`, `{rw}` pour les factions ; `{rel}` pour la phase religieuse ; `{church}` pour le symbole principauté ; `{horse}` et `{boot}` pour les valeurs de la carte ; `**texte**` pour le gras.

## Droits

Les illustrations et les textes des cartes appartiennent à VUCA Games, LLC. Ce dépôt est une aide de jeu non officielle.
