import pygame as pg
from __init__ import ALTO, ANCHO
from escenas import Portada, Partida

pg.init()

class Game():
    def __init__(self):
        pantalla = pg.display.set_mode((ANCHO, ALTO))
        self.escenas = [Portada(pantalla), Partida(pantalla)]

    def launch(self):
        i = 0

        while True:
            self.escenas[i].bucle_principal()
            i += 1
            if i == len(self.escenas):
                i = 0
