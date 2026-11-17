# Double authentification (MFA)

## La double authentification, c'est quoi ?

Pour mieux protéger votre compte INDIM@J, la connexion se fait désormais **en deux temps** :

- **ce que vous connaissez** : votre mot de passe, comme d'habitude ;
- **ce que vous avez** : votre téléphone, qui affiche un code de **6 chiffres**.

Même si quelqu'un découvre votre mot de passe, il ne peut pas entrer dans votre compte sans votre téléphone.

Le code est fourni par une application gratuite, **Google Authenticator**. Il change toutes les 30 secondes.

!!! info "Le même principe qu'à la banque"
    C'est comme le code reçu sur votre téléphone pour valider un paiement par carte sur Internet : après le mot de passe, une petite étape de vérification s'ajoute.

### Les étapes, en résumé

1. **Installer** l'application Google Authenticator sur votre téléphone (une seule fois).
2. **Activer** la double authentification en scannant un QR code (une seule fois).
3. **Noter** vos 10 codes de secours sur une feuille (une seule fois).
4. **À chaque connexion**, taper le code à 6 chiffres affiché par l'application.

## Ce qu'il vous faut

- un **téléphone Android** ou un **iPhone** (iOS 16 ou plus récent) ;
- l'application **Google Authenticator**, gratuite (voir l'[étape 1](installer/index.md)) ;
- votre téléphone réglé sur l'**heure automatique** ;
- sur votre ordinateur, **Java 8 update 60** ou une version plus récente ;
- une **feuille de papier** et un stylo, pour noter vos codes de secours.

!!! warning "L'heure du téléphone doit être exacte"
    Le code dépend de l'heure. Si l'heure de votre téléphone est décalée, même d'une minute ou deux, le code sera refusé.

### Régler l'heure automatique

- **Android** : Paramètres › Système › Date et heure › activez **Date et heure automatiques** (le nom exact peut varier selon le téléphone).
- **iPhone** : Réglages › Général › Date et heure › activez **Réglage automatique**.

## Télécharger le guide

Version imprimable du guide, en français et en arabe :

[:material-file-pdf-box: Guide MFA — français](telechargements/Manuel_MFA_INDIMAJ_FR.pdf){ .md-button target="_blank" }
[:material-file-pdf-box: دليل المصادقة الثنائية — العربية](telechargements/Manuel_MFA_INDIMAJ_AR.pdf){ .md-button target="_blank" }

## Assistance

Pour toute question : [equipe_indimaj@tgr.gov.ma](mailto:equipe_indimaj@tgr.gov.ma)
