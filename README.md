# Projet_info_PPMD_QGIS_isochrone
## Notes de début - Compréhension du sujet
Plugin QGIS présente une interface pour faire le choix des paramètres (si possible renseigner le point par coordonnées et par clic sur canva)
A partir des paramètres, construction d'une requête (format json <-> dictionnaire python). La requête est envoyée au serveur GPF. La requête sous format json (contrainte pas modifiable) est récupérer et ajout de la geomètrie de réponse sur QGIS 


## Faits
### Diagrammes (plant UML ou https://app.diagrams.net/) : 
    Diagramme de cas d'utilisation
    Diagramme de classes
    Diagramme d'activité ou de séquence

### Classes attendues d'un point algo (pas GQIS) :
    #### Requetes
        Attributs : point, resource, costValue, costType, profile, direction, constraints, geometryFormat, distanceUnit, timeUnit, crs, dico
    #### Réponses
        Attributs : code, point, resource, costValue, costType, profile, direction, constraints, geometryFormat, distanceUnit, timeUnit, crs, geometry (coord, type)

## A faire
### Mettre à jour diagrammes
    Diagramme de séquence (mettre numéro des étapes)
    Diagramme de classe avec les bons attributs et méthodes

### Plugin QGIS
    PyQT
    Lien entre les fonctions python QGIS et les classes
    Récupération et affichage du json 

## Description  
## Installation  
## Usage


