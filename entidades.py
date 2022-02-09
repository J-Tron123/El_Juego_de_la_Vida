import pygame as pg, numpy as np
from __init__ import *

class Tablero():
    def __init__(self):
        self.celda_ancho = ANCHO / NXC
        self.celda_alto = ALTO / NYC

    def vecinas(self, x, y, celula):
        super().__init__()
        vecinas =   celula[(x - 1) % NXC, (y - 1)  % NYC] + \
                    celula[(x)     % NXC, (y - 1)  % NYC] + \
                    celula[(x + 1) % NXC, (y - 1)  % NYC] + \
                    celula[(x - 1) % NXC, (y)      % NYC] + \
                    celula[(x + 1) % NXC, (y)      % NYC] + \
                    celula[(x - 1) % NXC, (y + 1)  % NYC] + \
                    celula[(x)     % NXC, (y + 1)  % NYC] + \
                    celula[(x + 1) % NXC, (y + 1)  % NYC]
        return vecinas

    def casillas(self, x, y):
        super().__init__()
        casillas = [((x)   * self.celda_ancho, y * self.celda_alto),
                ((x+1) * self.celda_ancho, y * self.celda_alto),
                ((x+1) * self.celda_ancho, (y+1) * self.celda_alto),
                ((x)   * self.celda_ancho, (y+1) * self.celda_alto)]
        return casillas

class Celulas(Tablero):
    def comportamineto(self, x, y, vecinas, celula, nueva_celula):
        if celula[x, y] == 0 and vecinas == 3:
            nueva_celula[x, y] = 1

        elif celula[x, y] == 1 and (vecinas < 2 or vecinas > 3):
            nueva_celula[x, y] = 0  

    def oscilador(self, celula):
        # Oscilador
        celula[38, 20] = 1
        celula[39, 20] = 1
        celula[40, 20] = 1

    def serpiente(self, celula):
        # Serpiente
        celula[30, 20] = 1
        celula[31, 20] = 1
        celula[32, 20] = 1
        celula[32, 19] = 1
        celula[33, 19] = 1
        celula[34, 19] = 1

    def corredor(self, celula):
        # Corredor
        celula[10, 5] = 1
        celula[12, 5] = 1
        celula[11, 6] = 1
        celula[12, 6] = 1
        celula[11, 7] = 1
    
    # Alguna otra que quieras añadir a partir de aquí