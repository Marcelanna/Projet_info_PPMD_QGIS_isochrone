# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 09:17:02 2025

@author: ANNA
"""

import requests
# https://github.com/IGNF/gpf-filtered-getcapabilities/blob/main/main.py
from reponse import Reponse

class Requete():
    
    def __init__(self, x, y,resource,costValue,costType,profile,direction,distanceUnit,timeUnit,crs,constraints = []):
        self.point = f"{x},{y}" # à voir s'il faut créer ne classe à part
        self.resource = resource # trois possibilités : bdtopo-valhalla, bdtopo-osrm, pgrouting
        self.costValue = costValue # distance en m ou temps en s de l'isochrone
        self.costType = costType # time ou distance
        self.profile = profile # pedestrian ou car
        self.direction = direction # departure ou arrival
        self.constraints = constraints # vide à voir plus tard
        self.distanceUnit = distanceUnit # meter fixe ?
        self.timeUnit = timeUnit # second fixe ?
        self.crs = crs # EPSG:4326 ou fixe ?
        self.dico = {"point":self.point,"resource":self.resource,"resourceVersion":"2025-09-25","costType":self.costType,"costValue":self.costValue,"timeUnit":self.timeUnit,"profile":self.profile,"direction":self.direction,"crs":self.crs}

    def send(self):
        # URL pour la requête de calcul d'isochrone de Geoportail
        url = 'https://data.geopf.fr/navigation/isochrone'
  
        # Envoie de la requête avec les paramètres d'entrée
        r = requests.get(url, self.dico)
        
        # création d'une instance de la classe Reponse
        response = Reponse(r.status_code, r.json())
        return response
    

if __name__ == '__main__':

    req = Requete(55.31671488583523, -20.944842285775835, "bdtopo-valhalla", 240, "time", "car", "departure", "m", "second", "EPSG:4326")
    r  = req.send()
    
    print("Code : ", r.code)
    print("Json : ", r.geometry)
    
    ### Stock de var au cas où
    # url = 'https://data.geopf.fr/navigation/isochrone'
    # dico = req.dico

    # r = requests.get(url, dico)
    # # check status code for response received
    # # success code - 200
    # print(r)

    # # print content of request
    # print(r.content)

    #https://data.geopf.fr/navigation/isochrone?gp-access-lib=3.4.2&resource=bdtopo-valhalla&point=55.31671488583523,-20.944842285775835&direction=departure&costType=time&costValue=240&profile=car&timeUnit=second&distanceUnit=meter&crs=EPSG:4326&constraints={%22constraintType%22:%22banned%22,%22key%22:%22wayType%22,%22operator%22:%22=%22,%22value%22:%22autoroute%22}|{%22constraintType%22:%22banned%22,%22key%22:%22wayType%22,%22operator%22:%22=%22,%22value%22:%22pont%22}
    # r = requests.get('https://data.geopf.fr/navigation/isochrone', dico)
    #dico = {"point":"55.31671488583523,-20.944842285775835","resource":"bdtopo-valhalla","resourceVersion":"2025-09-25","costType":"time","costValue":240,"timeUnit":"second","profile":"car","direction":"departure","crs":"EPSG:4326"}
