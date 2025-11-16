# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 09:17:02 2025

@author: ANNA
"""

class Reponse():
    """
    Format de réponse à une requête
    """
    def __init__(self, code, response):
        """
        

        Parameters
        ----------
        code : str
            Code de statut de la réponse de la requête.
        response : dict
            Réponse à la requête sous format dictionnaire (json converti).

        Returns
        -------
        None.

        """

        dict_error = {200:"Opération réussie",400:"Paramètres invalides",403:"Non autorisé", 404:"Non trouvé"}

        # code pour vérifier que la requête à bien abouti
        self.code = code
        self.message = dict_error[code]

        # Création d'un attribut pour chaque clé du dictionnaire : 
        # 'point', 'resource', 'resourceVersion', 'costType', 'costValue', 
        # 'timeUnit', 'profile', 'direction', 'crs', 'geometry', 'constraints'
        for key, value in response.items():
            setattr(self, key, value)
        
        # pour récupérer le json de la geometrie de sortie, utiliser le .geometry
