# Guide d'utilisation INDIM@J

Site de documentation construit avec [MkDocs](https://www.mkdocs.org/) et le thème [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).

## Prévisualiser le site en local

```bash
pip install -r requirements.txt
mkdocs serve
```

Le site est alors consultable sur <http://127.0.0.1:8000> et se recharge à chaque modification.

## Publication

Chaque push sur la branche `main` lance le workflow `.github/workflows/ci.yml`, qui construit le site et le publie sur la branche `gh-pages`.

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
├── depannage/                       Fiches de dépannage
└── assets/                          Logo et feuille de style
```

Chaque page se trouve dans son propre dossier (`index.md`), avec les captures d'écran qu'elle utilise. Le menu est défini dans la section `nav` de `mkdocs.yml`.
