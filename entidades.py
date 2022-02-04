import pygame as pg
from __init__ import *

class Tablero():
    def __init__(self):
        self.casilla = (25, 25)

    def tablero(self, pantalla):
        super().__init__()
        self.casillas = []
        for casilla in range((pantalla)/self.casilla):
            casilla += 0
            self.casillas.append(casilla)
        return self.casillas

