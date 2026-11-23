# Odin pour iPhone (expérimental)

Version iPhone d'[Odin](https://github.com/Tovarichtch/Odin), l'émulateur SEGA
Hikaru et Gaelco ATV Track de Réda Chérif-Touil (GPL 3), tirée du portage
Android [odin-android](https://github.com/Laurent-67370/odin-android).

**État : expérimental.** Premier essai réel (version 0.1.6, iPad Pro M5 sous
iOS 27, LiveContainer, JIT par StikDebug) : l'app s'ouvre, Vulkan tourne sur
le GPU M5, les menus, la liste des jeux et une manette DualSense marchent, un
jeu (Star Wars Racer Arcade) se charge et démarre ; **puis l'app se ferme**
au bout d'une dizaine de secondes, sans erreur dans `odin.log`. Piste
principale : le JIT, qu'iOS 26 et plus récent n'accorde plus de la même façon.
La version suivante demande sa mémoire de code à StikDebug, comme les
émulateurs iOS : sous iOS 26 et plus récent, choisir le script
**`universal.js`** dans StikDebug. D'autres
**bêta-testeurs** sont les bienvenus :
[Tovarichtch/Odin#56](https://github.com/Tovarichtch/Odin/issues/56).

> **In English, for beta testers:** an experimental, unsigned iPhone build of
> Odin (iOS 16.3+, arm64). Download
> [odin.ipa](https://github.com/Laurent-67370/odin-ios/releases/download/odin-ios/odin.ipa),
> sideload it with SideStore or AltStore, then in Odin use MENU → File → Add
> games... to pick `hikaru.zip`, `mie.zip` and your games from Files. First real test
> (iPad Pro M5, iOS 27, LiveContainer, JIT by StikDebug): the menus, the
> pad and the graphics work, a game loads and starts, then the app closes
> after about ten seconds: the JIT is the main suspect, the next build asks
> StikDebug for its code memory, as iOS emulators do: on iOS 26 and later,
> pick the **`universal.js`** script in StikDebug. Without StikDebug the games
> run slower (`JIT: off` in `odin.log`). Please report your iPhone model, iOS version, screenshots and
> `odin.log` (Files → On My iPhone → Odin) on
> [Tovarichtch/Odin#56](https://github.com/Tovarichtch/Odin/issues/56) or in
> [this repository's issues](https://github.com/Laurent-67370/odin-ios/issues).

## Télécharger

[odin.ipa](https://github.com/Laurent-67370/odin-ios/releases/download/odin-ios/odin.ipa)
(publication [`odin-ios`](https://github.com/Laurent-67370/odin-ios/releases/tag/odin-ios),
reconstruite à chaque modification). L'`.ipa` n'est pas signé : on l'installe
soi-même.

## Installer

1. Un iPhone **arm64** sous **iOS 16.3 ou plus récent** (une puce A14 ou plus
   récente conseillée : l'émulation Hikaru est lourde).
2. Installer `odin.ipa` avec **SideStore** ou **AltStore** (gratuits, avec un
   identifiant Apple ; l'app est à renouveler tous les 7 jours avec un compte
   gratuit).
3. Dans Odin, **MENU → File → Add games...** : choisir dans Fichiers (ou
   iCloud) `hikaru.zip`, `mie.zip` et les jeux (archives MAME `.zip` / `.7z`),
   plusieurs à la fois ; Odin les copie dans son dossier `roms/` et dit pour
   chacun s'il est prêt. On peut aussi les déposer soi-même : **Fichiers** →
   **Sur mon iPhone** → **Odin** → `roms/` (avec LiveContainer, dans le dossier
   de LiveContainer). `odin.ini` et `odin.log` sont écrits à côté.
4. Lancer Odin : la liste des jeux s'affiche, en portrait comme en paysage.
   Une manette (DualSense, Xbox…) marche comme la manette tactile.

## Les étapes

| Étape | Contenu | État |
|---|---|---|
| 1 | l'app s'ouvre : menus, liste des jeux, manette tactile, dossiers dans Fichiers ; Vulkan par MoltenVK | **marche** (iPad Pro M5, iOS 27) |
| 2 | les jeux : sans JIT, les instructions décodées (plus lent) ; avec le JIT (Odin recompile le SH-4 et l'ARM7 en ARM64) activé par un débogueur (**StikDebug**), la mémoire du code projetée deux fois, comme dans les émulateurs iOS ; `odin.log` dit `JIT: on` ou `JIT: off` | le jeu démarre puis l'app se ferme (JIT on, iOS 27) : **en cours** |
| 3 | l'import de jeux depuis l'app (MENU → File → Add games...) | **construit**, à essayer |
| 4 | « Get homebrew games... » comme sur Android | plus tard |

Sous **iOS 26 et plus récent**, la mémoire qu'une app se donne ne s'exécute
plus, même avec le débogueur : Odin la demande à StikDebug (`brk #0xf00d`,
protocole de StikJIT), qui la prépare avec son script **`universal.js`** ;
Odin y écrit par une seconde projection. `odin.log` dit d'où vient sa mémoire
(`JIT: … KB of code memory from the debugger` ou `mapped twice by the app`).
Sans StikDebug, les jeux tournent sans JIT, plus lentement.

## Historique des essais

| Version | Appareil | Résultat |
|---|---|---|
| 0.1.3 – 0.1.5 | iPad Pro M5, iOS 27, LiveContainer | écran noir : SDL ne trouvait pas Vulkan (MoltenVK) ; corrigé en 0.1.6 |
| 0.1.6 | iPad Pro M5, iOS 27, LiveContainer, StikDebug | menus, manette DualSense, Vulkan, jeu chargé (`Running`, `JIT: on`) ; l'app se ferme une dizaine de secondes plus tard |

## Bêta-testeurs : ce qui aide

- le modèle de l'iPhone et la version d'iOS ;
- des captures d'écran ;
- le fichier `odin.log` (Fichiers → Sur mon iPhone → Odin ; avec LiveContainer,
  dans son dossier), après chaque essai ;
- si l'app se ferme : le rapport de plantage d'iOS (Réglages → Confidentialité
  et sécurité → Analyse et améliorations → Données d'analyse, l'entrée la plus
  récente au nom de l'app ou de LiveContainer) ;
- si StikDebug a été utilisé ou non.

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
