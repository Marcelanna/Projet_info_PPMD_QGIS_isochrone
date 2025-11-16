# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 09:17:02 2025

@author: ANNA
"""

import requests
# https://github.com/IGNF/gpf-filtered-getcapabilities/blob/main/main.py
from .reponse import Reponse

class Requete():
    """
    Envoie de la requete au serveur Geoplateforme à partir des pamaètre d'entrée 
    et récupération de la réponse depuis la classe Reponse 
    """
    
    def __init__(self, x, y,resource,costValue,costType,profile,direction,distanceUnit = "m",timeUnit = "second",crs = "EPSG:4326"):
        """
        Initialisation des attributs de la classe à partir des arguments rensignés pour la classe

        Parameters
        ----------
        x : float
            Longitude (E en planimètrique) du point d'intérêt.
        y : float
            Latitude (N en planimètrique) du point d'intérêt.
        resource : str
            Ressource utilisée pour le calcul, trois possibilités : bdtopo-valhalla, bdtopo-osrm, bdtopo-pgr.
        costValue : int
            Valeur du coût utilisé pour le calcul (peut être une distance ou un temps).
        costType : str
            Type du coût utilisé pour le calcul, pour le temps : "time", pour la distance : "distance" .
        profile : str
            Mode de déplacement utilisé pour le calcul, pour un piéton : "pedestrian", pour une voiture : "car".
        direction : str
            Sens du parcours, pour un point de départ : "departure", pour un point d'arrivée : "arrival".
        distanceUnit : str
            Unité pour la distance. Par défaut, fixé au mètre.
        timeUnit : str
            Unité pour le temps. Par défaut, fixé à la seconde.
        crs : str
            Système de projection. Par défaut, fixé à l'EPSG:4326.

        Returns
        -------
        None.

        """

        self.point = f"{x},{y}"
        self.resource = resource 
        self.costValue = costValue 
        self.costType = costType
        self.profile = profile
        self.direction = direction
        self.distanceUnit = distanceUnit
        self.timeUnit = timeUnit
        self.crs = crs

        # Création d'un dictionnaire pour consruire la requête
        self.dico = {"point":self.point,"resource":self.resource, "costType":self.costType,"costValue":self.costValue,"timeUnit":self.timeUnit,"profile":self.profile,"direction":self.direction,"crs":self.crs}

    def send(self):
        """
        Envoie de la requête auprès du serveur Geoplateforme

        Returns
        -------
        response : Objet de la classe Response
            Reponse de la requete : code de la réponse (détection erreur) et géometrie de la réponse si requête valide.

        """

        # URL pour la requête de calcul d'isochrone de Geoplateforme
        url = 'https://data.geopf.fr/navigation/isochrone'
  
        # Envoie de la requête avec les paramètres d'entrée
        r = requests.get(url, self.dico)
        
        # création d'une instance de la classe Reponse
        response = Reponse(r.status_code, r.json())
        return response
    
    