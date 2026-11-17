# Guide d'utilisation INDIM@J

Site de documentation construit avec [MkDocs](https://www.mkdocs.org/) et le thème [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).

## Prévisualiser le site en local

```bash
pip install -r requirements.txt
mkdocs serve
```

Le site est alors consultable sur <http://127.0.0.1:8000> et se recharge à chaque modification.

Pour prévisualiser la version arabe :

```bash
mkdocs serve -f mkdocs.ar.yml
```

## Publication

Chaque push sur la branche `main` lance le workflow `.github/workflows/ci.yml`, qui construit la version française (racine du site) puis la version arabe (dossier `/ar/`), et publie le tout sur la branche `gh-pages`.

Pour l'activer la première fois : **Settings › Pages › Build and deployment**, source **Deploy from a branch**, branche **gh-pages**, dossier **/ (root)**.

## Structure

```text
docs/
├── index.md                         Accueil
├── installation/
│   ├── index.md                     Introduction et prérequis
│   ├── navigateurs/                 Phase 1 — étapes 1 à 3
│   ├── certificat/                  Phase 2 — étapes 4 à 7
│   ├── java/                        Phase 3 — étapes 8 à 14
│   ├── finalisation-firefox/        Phase 4 — étapes 15 et 16
│   └── verification/                Liste de vérification finale
├── renouvellement/                  Renouvellement d'un certificat expiré
├── mfa/                             Double authentification (MFA)
│   ├── index.md                     Présentation, prérequis, guides PDF
│   ├── installer/                   Étape 1 — Google Authenticator
│   ├── activation/                  Étapes 2 et 3 — activation, codes de secours
│   ├── connexion/                   Connexion quotidienne, code de secours
│   ├── assistance/                  Réinitialisation et contacts
│   ├── faq/                         Questions fréquentes
│   ├── img/                         Captures d'écran (données personnelles floutées)
│   └── telechargements/             Guides PDF (français, arabe)
├── depannage/                       Fiches de dépannage
└── assets/                          Logo, feuille de style, bouton de langue (langue.js)

docs-ar/                             Version arabe : mêmes dossiers et mêmes noms de pages que docs/
└── assets/extra-ar.css              Compléments de style pour l'écriture de droite à gauche
hooks/fichiers_partages.py           Reprend dans la version arabe les captures, PDF et styles de docs/
mkdocs.ar.yml                        Configuration de la version arabe (hérite de mkdocs.yml)
```

Chaque page se trouve dans son propre dossier (`index.md`), avec les captures d'écran qu'elle utilise. Le menu est défini dans la section `nav` de `mkdocs.yml`.

## Version arabe

Le bouton de langue, en haut de page, ouvre la même page dans l'autre langue. Pour qu'il fonctionne :

- toute page ajoutée dans `docs/` doit avoir sa traduction au même chemin dans `docs-ar/` (et inversement) ;
- la page doit être ajoutée au menu (`nav`) de `mkdocs.yml` et de `mkdocs.ar.yml`.

Les captures d'écran et les guides PDF restent uniquement dans `docs/` : la version arabe les reprend automatiquement.
