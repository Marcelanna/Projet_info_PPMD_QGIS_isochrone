# Projet_info_PPMD_QGIS_isochrone

## Description
Cette extension QGIS permet de calculer une zone accessible en un temps ou une distance donnée à partir d’un point sur la carte, à l’instar de la fonctionnalité disponible sur Géoportail. Le calcul est effectué via une requête au serveur Géoplateforme, avec la possibilité de personnaliser plusieurs paramètres selon les options supportées par ce dernier.

## Installation
### Prérequis
- **Version de QGIS** : 3.x.x (non compatible avec QGIS 4.x.x ou les versions futures de QT Design).

### Procédure
1. Téléchargez le fichier ZIP de l’extension : `Plugin_calcul_isochrone.zip`.
2. Ouvrez un projet QGIS.
3. Allez dans l’onglet **Extensions** > **Installer à partir d’un ZIP**.
4. Sélectionnez le fichier téléchargé sur l'explorateur de fichiers.
5. Une fois l’installation terminée, l’icône de l’extension apparaîtra dans la barre d’outils principale de QGIS.

## Utilisation
### Préparation
- Assurez-vous d’avoir une **connexion internet stable**.
- Vérifiez que le **système de coordonnées du projet** est bien défini en **EPSG:4326**.

### Étapes
1. **Lancer l’extension** : Cliquez sur l’icône du plugin dans la barre d’outils.
2. **Choisir le point de départ** :
   - Saisissez manuellement les coordonnées (format : nombre à virgule flottante, séparateur décimal = point, en EPSG:4326).
   - Ou cliquez sur le bouton **« Cliquer sur la carte »** pour sélectionner un point directement sur la carte. L’extension devient alors l’outil actif et la fenêtre se masque temporairement pour faciliter la sélection. Une fois le point choisi, ses coordonnées s’actualisent automatiquement dans la fenêtre.
3. **Paramétrer le calcul** :
   - **Ressource** : Choisissez parmi les options disponibles (`bdtopo-valhalla`, `bdtopo-osrm`, `bdtopo-pgr`). Certaines ressources peuvent limiter les types de calculs possibles.
   - **Type de calcul** : Sélectionnez **« Temps »** ou **« Distance »** via les boutons radio. Renseignez ensuite la valeur correspondante.
   - **Mode de déplacement** : Choisissez entre **« Marche »** ou **« Voiture »**.
   - **Sens du parcours** : Précisez si le calcul doit être effectué **« Depuis le point »** ou **« Vers le point »**.
4. **Lancer le calcul** : Cliquez sur **« Calculer »**.
   - En cas de succès de la requête, la zone d’atteinte s’affiche directement sur la carte.
   - En cas d’échec de la requête, un **code d’erreur** et sa signification s’affichent dans la fenêtre de dialogue **« Calcul isochrone »**.

