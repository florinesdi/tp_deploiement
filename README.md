# Déploiement automatisé ClientHub

## Fonctionnement du pipeline

Chaque push sur la branche `main` déclenche automatiquement un workflow GitHub Actions.

Le pipeline exécute les étapes suivantes :
1. tests unitaires
2. tests E2E
3. build de l’image Docker
4. push sur Docker Hub
5. déploiement automatique sur une VM Azure via SSH
6. vérification finale via l’endpoint `/health`

## Déclenchement

Le déploiement est déclenché automatiquement à chaque `git push` sur la branche `main`.

## Choix techniques

- Flask pour l’application web
- Docker pour la conteneurisation
- GitHub Actions pour la CI/CD
- Docker Hub pour le stockage de l’image
- déploiement par SSH sur une VM Azure
- conteneur nommé de manière fixe pour garantir un déploiement idempotent
