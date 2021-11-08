# -*- coding: utf-8 -*-

import csv
from collections import namedtuple
from datetime import datetime


Pokemon = namedtuple('Pokemon','p,Name,Type_1,Type_2,HP,Attack,Defense,Sp_Atk,Sp_Def,Speed,Generation,Legendary,Date')

# Bloque 1:

def leer_pokemons(fichero):
    res = []
    with open(fichero,encoding = "utf-8") as f:
        lector = csv.reader(f)
        next(lector)
        for e in lector:
            res.append(Pokemon(int(e[0]),e[1],e[2],e[3],int(e[4]),int(e[5]),int(e[6]),int(e[7]),int(e[8]),int(e[9]),int(e[10]),e[11],datetime.strptime(e[12], "%d-%m-%y")))
    return res

# Bloque 2:
def filtrar_pokemon_tipo (pokemon, tipo):

    res = []
    for e in pokemon:
        if e.Type_1 == tipo or e.Type_2 == tipo:
            res.append(e.Name)
    return res

def conjunto_de_tipos (pokemon):

    res = set()
    for e in pokemon:
        res.add(e.Type_1)
        res.add(e.Type_2)
    return res

#Bloque 3:

