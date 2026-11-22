# Odin pour iPhone (expérimental)

Version iPhone d'[Odin](https://github.com/Tovarichtch/Odin), l'émulateur SEGA
Hikaru et Gaelco ATV Track de Réda Chérif-Touil (GPL 3), tirée du portage
Android [odin-android](https://github.com/Laurent-67370/odin-android).

**État : expérimental.** L'app est construite pour s'ouvrir (menus, liste des
jeux, manette tactile) ; **les jeux ne démarrent pas encore** : il leur faut le
JIT, qui fait l'objet de l'étape 2. Personne ne l'a encore essayée sur un
iPhone : des **bêta-testeurs** sont recherchés, l'appel est lancé sur
[Tovarichtch/Odin#56](https://github.com/Tovarichtch/Odin/issues/56).

> **In English, for beta testers:** an experimental, unsigned iPhone build of
> Odin (iOS 16.3+, arm64). Download
> [odin.ipa](https://github.com/Laurent-67370/odin-ios/releases/download/odin-ios/odin.ipa),
> sideload it with SideStore or AltStore, then put `hikaru.zip`, `mie.zip` and
> your games in Files → On My iPhone → Odin → `roms/`. For now only the menus
> and the game list are expected to work: the games need JIT (step 2, with
> StikDebug). Please report your iPhone model, iOS version, screenshots and
> `odin.log` (same folder) on
> [Tovarichtch/Odin#56](https://github.com/Tovarichtch/Odin/issues/56) or in
> [this repository's issues](https://github.com/Laurent-67370/odin-ios/issues).

## Télécharger

[odin.ipa](https://github.com/Laurent-67370/odin-ios/releases/download/odin-ios/odin.ipa)
(publication [`odin-ios`](https://github.com/Laurent-67370/odin-ios/releases/tag/odin-ios),
reconstruite à chaque modification). L'`.ipa` n'est pas signé : on l'installe
soi-même. Le lien fonctionne dès que la première construction est publiée
(onglet **Releases** du dépôt) ; tant qu'elle ne l'est pas, il mène à une page
introuvable.

## Installer

1. Un iPhone **arm64** sous **iOS 16.3 ou plus récent** (une puce A14 ou plus
   récente conseillée : l'émulation Hikaru est lourde).
2. Installer `odin.ipa` avec **SideStore** ou **AltStore** (gratuits, avec un
   identifiant Apple ; l'app est à renouveler tous les 7 jours avec un compte
   gratuit).
3. Ouvrir l'app **Fichiers** → **Sur mon iPhone** → **Odin** : y mettre, dans
   le dossier `roms/`, `hikaru.zip`, `mie.zip` et les jeux (archives MAME
   `.zip` / `.7z`). `odin.ini` et `odin.log` sont écrits à côté.
4. Lancer Odin : la liste des jeux s'affiche, en portrait comme en paysage.

## Les étapes

| Étape | Contenu | État |
|---|---|---|
| 1 | l'app s'ouvre : menus, liste des jeux, manette tactile, dossiers dans Fichiers | **construite**, à essayer par les bêta-testeurs |
| 2 | les jeux : le JIT (Odin recompile le SH-4 et l'ARM7 en ARM64, il n'a pas d'interpréteur), activé par un débogueur (**StikDebug**) ; la mémoire du code à la façon des émulateurs iOS | à faire, avec les testeurs |
| 3 | les jeux maison, l'import de jeux depuis l'app | plus tard |

Pas de promesse pour l'étape 2, surtout sous **iOS 26**, qui rend le JIT plus
difficile.

## Bêta-testeurs : ce qui aide

- le modèle de l'iPhone et la version d'iOS ;
- des captures d'écran ;
- le fichier `odin.log` (Fichiers → Sur mon iPhone → Odin), après chaque essai.

À envoyer sur [Tovarichtch/Odin#56](https://github.com/Tovarichtch/Odin/issues/56)
ou dans les [issues de ce dépôt](https://github.com/Laurent-67370/odin-ios/issues).

## Comment c'est construit

Ce dépôt ne contient pas le code d'Odin. Le workflow `.github/workflows/ios.yml`,
sur un Mac de GitHub :

1. récupère [odin-android](https://github.com/Laurent-67370/odin-android) et son
   patch d'Odin, commun avec Android (menus pour le téléphone, manette tactile,
   dossiers, rubrique Homebrew) : une amélioration du patch profite aux deux ;
2. construit Odin pour iOS (arm64), avec **Vulkan par MoltenVK**, intégré à
   l'app ; le moteur OpenGL d'Odin n'est que compilé : `ios/gl-stubs.py`
   remplace par des fonctions vides celles qui manquent à l'OpenGL ES 3.0
   d'iOS ;
3. assemble `odin.ipa` (non signé) et le publie.

Le numéro de version est `0.1.N` (`version.txt`, puis le nombre de
modifications de ce dépôt) ; Odin l'affiche dans MENU → About
(`ios-0.1.N-odin-xxxxxxx`).

Code écrit avec Claude Code (Claude Opus 5.5).
