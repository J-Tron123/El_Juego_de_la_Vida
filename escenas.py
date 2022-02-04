from turtle import width
import pygame as pg
from __init__ import *
import numpy as np
import time

class Escena():
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.reloj = pg.time.Clock()
    
    def bucle_principal(self):
        pass

class Portada(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        self.logo = pg.image.load("resources/images/portada.png")
        fuente = pg.font.Font("resources/fonts/CabinSketch-Bold.ttf", 45)
        self.textito = fuente.render("Press <SPC> to start", True, (0,0,0))
        self.anchoTexto = self.textito.get_width()

    def bucle_principal(self):
        game_over = False
        while not game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    exit()
                    
                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_SPACE:
                        game_over = True

            self.pantalla.fill((41, 50, 49))
            self.pantalla.blit(self.logo, (150, 250))
            self.pantalla.blit(self.textito, ((ANCHO - self.anchoTexto) // 2, 640))
            pg.display.set_caption("El Juego de la Vida")
            pg.display.flip()

class Partida(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        self.celula = np.zeros((NXC, NYC)) 
        self.reloj = pg.time.Clock()

    def bucle_principal(self):
        pausa = False
        while True:
            self.nueva_celula = np.copy(self.celula)
            time.sleep(0.1)
            posX = pg.mouse.get_pos()
            posY = pg.mouse.get_pos()
            celda_x = int(posX[0] / NXC)
            celda_y = int(posY[1] / NYC)
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    exit()
                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_SPACE:
                        not pausa
                if evento.type == pg.MOUSEBUTTONDOWN:
                    if sum(pg.mouse.get_pressed()) > 0:
                        self.nueva_celula[celda_x, celda_y] = 1
            
            for x in range(0, NYC):
                for y in range (0, NXC):
                    if not pausa:
                        vecinas =   self.celula[(x - 1) % NXC, (y - 1)  % NYC] + \
                                    self.celula[(x)     % NXC, (y - 1)  % NYC] + \
                                    self.celula[(x + 1) % NXC, (y - 1)  % NYC] + \
                                    self.celula[(x - 1) % NXC, (y)      % NYC] + \
                                    self.celula[(x + 1) % NXC, (y)      % NYC] + \
                                    self.celula[(x - 1) % NXC, (y + 1)  % NYC] + \
                                    self.celula[(x)     % NXC, (y + 1)  % NYC] + \
                                    self.celula[(x + 1) % NXC, (y + 1)  % NYC]
            
            poly = [((x)   * celda_x, y * celda_y),
            ((x+1) * celda_x, y * celda_y),
            ((x+1) * celda_x, (y+1) * celda_y),
            ((x)   * celda_x, (y+1) * celda_y)]

            if self.nueva_celula[x, y] == 0:
                pg.draw.polygon(self.pantalla, (40, 40, 40), poly, 1)
            else:
                pg.draw.polygon(self.pantalla, (200, 100, 100), poly, 0)

            if self.celula[x, y] == 0 and vecinas == 3:
                self.celula[x, y] = 1

            if self.celula[x, y] == 1 and vecinas < 2:
                self.celula[x, y] = 0
            
            if self.celula[x, y] == 1 and vecinas > 3:
                self.celula[x, y] = 0

            self.celula = np.copy(self.nueva_celula)
            pg.display.set_caption("El Juego de la Vida")
            pg.display.flip()

