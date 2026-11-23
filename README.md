# Odin pour iPhone (expérimental)

Version iPhone d'[Odin](https://github.com/Tovarichtch/Odin), l'émulateur SEGA
Hikaru et Gaelco ATV Track de Réda Chérif-Touil (GPL 3), tirée du portage
Android [odin-android](https://github.com/Laurent-67370/odin-android).

**État : expérimental, mais les jeux tournent.** Sur un iPad Pro M5 sous
iOS 27 (LiveContainer), **sans JIT**, un bêta-testeur a joué une course
complète de Star Wars Racer Arcade, fluide à l'œil, environ 60 images par
seconde, à la manette DualSense : Vulkan sur le GPU M5, les menus, la liste des
jeux, tout marche. **Avec le JIT** (StikDebug), la version 0.1.6 se fermait
quelques secondes après le début du jeu : sous iOS 26 et plus récent, la
mémoire qu'une app se donne ne peut pas exécuter de code. La version 0.1.8 la
demande à StikDebug (script **`universal.js`**), comme les émulateurs iOS : à
essayer. Sans JIT, un appareil moins puissant qu'un M5 risque d'être trop lent.
D'autres **bêta-testeurs** sont les bienvenus, surtout avec un iPhone :
[Tovarichtch/Odin#56](https://github.com/Tovarichtch/Odin/issues/56).

> **In English, for beta testers:** an experimental, unsigned iPhone build of
> Odin (iOS 16.3+, arm64). Download
> [odin.ipa](https://github.com/Laurent-67370/odin-ios/releases/download/odin-ios/odin.ipa),
> sideload it with SideStore or AltStore, then in Odin use MENU → File → Add
> games... to pick `hikaru.zip`, `mie.zip` and your games from Files. On an iPad Pro M5
> (iOS 27, LiveContainer), **without JIT**, a full race of Star Wars Racer
> Arcade ran smoothly, about 60 fps, with a DualSense. With JIT, build 0.1.6
> closed a few seconds into the game; 0.1.8 asks StikDebug for its JIT memory
> the iOS 26 way: pick the **`universal.js`** script in StikDebug (to be
> tried). `odin.log` says `JIT: on` or `JIT: off`. Please report your iPhone model, iOS version, screenshots and
> `odin.log` (Files → On My iPhone → Odin) on
> [Tovarichtch/Odin#56](https://github.com/Tovarichtch/Odin/issues/56) or in
> [this repository's issues](https://github.com/Laurent-67370/odin-ios/issues).

## Télécharger

[odin.ipa](https://github.com/Laurent-67370/odin-ios/releases/download/odin-ios/odin.ipa)
(publication [`odin-ios`](https://github.com/Laurent-67370/odin-ios/releases/tag/odin-ios),
reconstruite à chaque modification). L'`.ipa` n'est pas signé : on l'installe
soi-même.

**Toutes les versions** depuis la 0.1.8 restent disponibles, chacune dans sa
publication `ios-0.1.NNN` (par exemple `ios-0.1.008` pour la 0.1.8) : [la liste](https://github.com/Laurent-67370/odin-ios/releases)
(pour revenir à une version précédente si la dernière pose problème) ; ce que
chacune apporte : [Les versions](#les-versions).

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
   Les jeux maison d'Odin (gratuits) : **MENU → File → Get homebrew games...**
   les télécharge depuis GitHub ; il leur faut aussi `hikaru.zip`.
4. Lancer Odin : la liste des jeux s'affiche, en portrait comme en paysage.
   Une manette (DualSense, Xbox…) marche comme la manette tactile.

## Par rapport à la version Android

Les **fonctions** sont les mêmes que dans [odin-android](https://github.com/Laurent-67370/odin-android) :
les deux partagent le même patch d'Odin. iOS est **moins essayé**, et son JIT
n'en est pas au même point.

| | Android | iOS |
|---|---|---|
| Menus pour le téléphone, portrait et paysage | oui, essayé | oui, essayé (iPad) |
| Manette tactile ; manette Bluetooth | oui, essayé | oui ; DualSense essayée |
| Liste des jeux, rubrique HOMEBREW | oui, essayé | oui, essayé (iPad) |
| MENU → File → **Add games...** (import, vérification « ready to play ») | oui, essayé | oui (sélecteur de Fichiers/iCloud), **pas encore essayé** |
| MENU → File → **Get homebrew games...** (nouveau, installé, mise à jour) | oui, essayé ; cases à cocher | oui ; un bouton par jeu ou « tous les nouveaux et mis à jour », **pas encore essayé** |
| Les jeux | à pleine vitesse (JIT toujours actif) | **sans JIT** : marchent, environ deux fois moins vite (fluide sur iPad Pro M5) |
| JIT | toujours actif | par StikDebug ; sous iOS 26+, script `universal.js` : **pas encore réussi** (iPad Pro M5, iOS 27 : l'app se fermait ; depuis la 0.1.16, sans réponse de StikDebug, Odin tourne sans JIT au lieu de se fermer) |
| Installation | APK signé | `.ipa` non signé, sideload (SideStore, AltStore, LiveContainer) |


| Étape | Contenu | État |
|---|---|---|
| 1 | l'app s'ouvre : menus, liste des jeux, manette tactile, manette Bluetooth, dossiers dans Fichiers ; Vulkan par MoltenVK | **marche** (iPad Pro M5, iOS 27) |
| 2 | les jeux : sans JIT, les instructions décodées (plus lent) ; avec le JIT (Odin recompile le SH-4 et l'ARM7 en ARM64) activé par un débogueur (**StikDebug**), la mémoire du code projetée deux fois, comme dans les émulateurs iOS ; `odin.log` dit `JIT: on` ou `JIT: off` | **sans JIT : marche** (Star Wars Racer, ~60 images/s sur iPad Pro M5) ; avec le JIT sous iOS 26+ : 0.1.8 à essayer |
| 3 | l'import de jeux depuis l'app (MENU → File → Add games...) | **construit**, à essayer |
| 4 | « Get homebrew games... » comme sur Android : la liste des jeux maison, chacun nouveau, installé ou avec une mise à jour, téléchargé et ajouté | **construit**, à essayer |

Sous **iOS 26 et plus récent**, la mémoire qu'une app se donne ne s'exécute
plus, même avec le débogueur : Odin la demande à StikDebug (`brk #0xf00d`,
protocole de StikJIT), qui la prépare avec son script **`universal.js`** ;
Odin y écrit par une seconde projection. `odin.log` dit d'où vient sa mémoire
(`JIT: … KB of code memory from the debugger` ou `mapped twice by the app`).
Sans StikDebug, les jeux tournent sans JIT, plus lentement.

## Les versions

Le numéro est `0.1.N`. Depuis la 0.1.15, il n'augmente que quand **l'app
change** : le code d'Odin (le patch d'[odin-android](https://github.com/Laurent-67370/odin-android))
ou ce qui la construit ici (`ios/`). Une modification du README ou de la
publication ne crée pas de nouvelle version. Chaque jour, une vérification
légère publie la nouvelle version quand le patch d'odin-android a changé. Jusqu'à la 0.1.14, N comptait
toutes les modifications de ce dépôt, d'où les versions sans rien de neuf dans
l'app et les numéros qui manquent. Odin affiche le numéro dans MENU → About
(`ios-0.1.N-odin-xxxxxxx`).

| Version | Ce qu'elle apporte | Essayée sur un appareil | À télécharger |
|---|---|---|---|
| 0.1.3 | la première qui se construit (Mac Intel de GitHub) : menus, liste des jeux, manette tactile, Vulkan par MoltenVK | écran noir (Vulkan pas trouvé) | non |
| 0.1.4 | sans JIT, les instructions décodées au lieu d'un plantage ; avec le JIT, la mémoire du code projetée deux fois | non essayée (même défaut de Vulkan) | non |
| 0.1.5 | MENU → File → **Add games...** : les jeux choisis dans Fichiers ou iCloud | non essayée (même défaut de Vulkan) | non |
| 0.1.6 | **Vulkan trouvé** : MoltenVK donné à SDL, aussi sous LiveContainer ; `odin.log` dit où | **les jeux tournent sans JIT** (iPad Pro M5, ~60 images/s) ; avec le JIT, l'app se ferme | non |
| 0.1.8 | **le JIT d'iOS 26** : la mémoire du code demandée à StikDebug (script `universal.js`) ; la publication ne reste plus en brouillon | à essayer | [0.1.8](https://github.com/Laurent-67370/odin-ios/releases/tag/ios-0.1.008) |
| 0.1.10 | MENU → File → **Get homebrew games...** : les jeux maison d'Odin téléchargés depuis GitHub | à essayer | [0.1.10](https://github.com/Laurent-67370/odin-ios/releases/tag/ios-0.1.010) |
| 0.1.11 | chaque version gardée dans sa publication `ios-0.1.N` | rien de neuf dans l'app | [0.1.11](https://github.com/Laurent-67370/odin-ios/releases/tag/ios-0.1.011) |
| 0.1.12 | les versions documentées (ce tableau, les notes des publications) | rien de neuf dans l'app | [0.1.12](https://github.com/Laurent-67370/odin-ios/releases/tag/ios-0.1.012) |
| 0.1.13 | les publications rangées dans l'ordre des versions, la dernière (`odin-ios`) en tête | rien de neuf dans l'app | [0.1.13](https://github.com/Laurent-67370/odin-ios/releases/tag/ios-0.1.013) |
| 0.1.14 | les tags sur trois chiffres (`ios-0.1.008`) : GitHub range les publications par tag, en texte | rien de neuf dans l'app | [0.1.14](https://github.com/Laurent-67370/odin-ios/releases/tag/ios-0.1.014) |
| 0.1.15 | « Get homebrew games... » signale les **mises à jour** des jeux maison, comme sur Android (le CRC de leur première EPROM) ; « All the new and updated » | à essayer | [0.1.15](https://github.com/Laurent-67370/odin-ios/releases/tag/ios-0.1.015) |
| 0.1.16 | sous iOS 26+, si StikDebug ne donne pas la mémoire du JIT, Odin tourne **sans JIT au lieu de se fermer** ; `odin.log` dit ce que StikDebug a répondu | à essayer | [0.1.16](https://github.com/Laurent-67370/odin-ios/releases/tag/ios-0.1.016) |

Les notes de chaque publication reprennent le titre de sa modification.

## Historique des essais

| Version | Appareil | Résultat |
|---|---|---|
| 0.1.3 – 0.1.5 | iPad Pro M5, iOS 27, LiveContainer | écran noir : SDL ne trouvait pas Vulkan (MoltenVK) ; corrigé en 0.1.6 |
| 0.1.6 | iPad Pro M5, iOS 27, LiveContainer, StikDebug | menus, manette DualSense, Vulkan, jeu chargé (`Running`, `JIT: on`) ; l'app se ferme une dizaine de secondes plus tard : la mémoire du JIT |
| 0.1.6 | iPad Pro M5, iOS 27, LiveContainer, sans JIT | **une course complète de Star Wars Racer Arcade**, fluide à l'œil (~60 images/s), manette DualSense ; le jeu se ferme proprement |
| 0.1.8 | — | le JIT d'iOS 26 par StikDebug (`universal.js`) : à essayer |
| 0.1.12 | iPad Pro M5, iOS 27, LiveContainer, StikDebug | JIT on, mais `odin.log` montre que StikDebug n'a pas fourni la mémoire (« mapped twice by the app ») : l'app se ferme ; sans JIT, 60 images/s en résolution maximale et filtrage anisotrope maximal |

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

Le numéro de version est `0.1.N` : voir [Les versions](#les-versions).

Code écrit avec Claude Code (Claude Opus 5.5).
