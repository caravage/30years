# Thirty Years of Misery – galerie des cartes

Galerie web des 126 cartes du jeu *Thirty Years of Misery* (Brian Asklev, © 2026 VUCA Games, LLC), extraites du module VASSAL `Thirty Years of Misery V1.vmod` (module VASSAL de Kevin Conway).

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
| Ligue catholique | 27 (la n° 25 est reconstituée, voir plus bas) |
| France | 27 |
| Suède | 27 |
| Troubles allemands (A à D) | 18 |

## Paquets A et B

Chaque faction a deux paquets d'événements. Le paquet A est utilisé dès le début de la partie. Les cartes B sont mélangées dans les paquets quand la carte Troubles « Sweden Enters the War » est tirée. La plupart portent un petit losange « B » en bas à droite. La carte n° 1 de chaque faction (Treaty of Westphalia) est classée à part dans la galerie, sous « Westphalie ».

| Faction | Paquet A (avec Westphalie) | Paquet B |
|---|---|---|
| Impériaux | 1 à 19 (19 cartes) | 20 à 27 (8 cartes) |
| Ligue catholique | 1 à 19 (19 cartes) | 20 à 27 (8 cartes) |
| France | 1 à 18 (18 cartes) | 19 à 27 (9 cartes) |
| Suède | 1 à 18 (18 cartes) | 19 à 27 (9 cartes) |

C'est voulu : la France et la Suède ont une carte A de moins et une carte B de plus que les factions catholiques.

France n° 22 (*Louis, The Great Condé*) n'a pas de losange B imprimé, mais c'est bien une carte B.

Le module VASSAL place correctement France n° 19 (*Annus Horribilis*) et Suède n° 19 (*Swedish Training*) dans les paquets B. Seule une étiquette interne de ces deux cartes indique encore « A » (prototype `def_Card_France_A` / `def_Card_Sweden_A`, propriété `Home_Deck`). Elle n'a aucun effet en jeu : les prototypes A et B font la même chose (défausser la carte).

## Carte manquante : Ligue catholique n° 25

Le module ne contient pas de carte Ligue catholique n° 25. Cette carte est une copie exacte d'*Inexperienced Troops* (n° 23) : même texte, mêmes valeurs (3/3), paquet B. La galerie l'ajoute en réutilisant l'image de la n° 23, avec l'étiquette « Reconstituée ».

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
