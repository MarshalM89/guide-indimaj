# Installation du poste

Cette partie décrit l'installation et la configuration d'un poste de travail pour accéder à INDIM@J, en quatre phases.

!!! note "Avant de commencer"
    - Télécharger `Firefox Setup 52.0.1esr.exe` et `jre-8u60-windows-i586.exe` depuis le [dossier Google Drive des fichiers d'installation](https://drive.google.com/drive/folders/1UZJvKztSVTUchLILuPxfFBg5bT1W3Tur?usp=drive_link){ target="_blank" }.
    - Disposer des **droits administrateur** sur le poste.
    - Disposer de votre **login INDIM@J** (utilisé pour générer le certificat).

[:material-download: Fichiers d'installation](https://drive.google.com/drive/folders/1UZJvKztSVTUchLILuPxfFBg5bT1W3Tur?usp=drive_link){ .md-button .md-button--primary target="_blank" }
[:material-book-open-variant: Documentation INDIM@J](https://drive.google.com/drive/folders/16wpMRpNEnHUsIAdGSu--Yr3b4I3sQGaI?usp=drive_link){ .md-button target="_blank" }

## Les quatre phases

| Phase | Contenu | Étapes |
|-------|---------|--------|
| [Phase 1 — Navigateurs](navigateurs/index.md) | Installer Firefox 52 ESR et, si besoin, Basilisk | 1 à 3 |
| [Phase 2 — Certificat](certificat/index.md) | Créer et sauvegarder le certificat d'accès | 4 à 7 |
| [Phase 3 — Java](java/index.md) | Installer et configurer Java, importer le certificat | 8 à 14 |
| [Phase 4 — Finalisation de Firefox](finalisation-firefox/index.md) | Autoriser les fenêtres popup et ajouter les exceptions | 15 et 16 |

Une fois l'installation terminée, contrôlez le poste avec la [liste de vérification finale](verification/index.md).

!!! info "Adresses de connexion"
    L'installation du poste est identique pour INDIM@J et INDIM@J Partenaire. Seul le lien de connexion diffère :

    - **INDIM@J** : [https://indimaj.tgr.gov.ma/](https://indimaj.tgr.gov.ma/){ target="_blank" }
    - **INDIM@J Partenaire** : [https://indimaj.tgr.gov.ma/forms/frmservlet?config=INDJPAR](https://indimaj.tgr.gov.ma/forms/frmservlet?config=INDJPAR){ target="_blank" }

!!! info "Navigateur alternatif : Basilisk"
    INDIM@J fonctionne aussi avec le navigateur **Basilisk (32 bits)**. Firefox 52 ESR reste indispensable pour créer le certificat. Voir l'[étape 3](navigateurs/index.md#etape-3) (facultative).
