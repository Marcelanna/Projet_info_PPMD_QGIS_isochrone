# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 09:17:02 2025

@author: ANNA
"""

class Reponse():
    def __init__(self, code, response):

        # code pour vérifier que la requête à bien abouti
        self.code = code

        # créer un attribut pour chaque clé du dictionnaire
        # 'point', 'resource', 'resourceVersion', 'costType', 'costValue', 
        # 'timeUnit', 'profile', 'direction', 'crs', 'geometry', 'constraints'
        for key, value in response.items():
            setattr(self, key, value)
        
        # pour récupérer le json de la geometry de sortie, utiliser le .geometry
