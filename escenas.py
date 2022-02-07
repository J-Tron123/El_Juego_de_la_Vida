import pygame as pg
from __init__ import *
import numpy as np
import time

class Escena():
    def __init__(self, pantalla):
        self.pantalla = pantalla
    
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
        # Oscilador
        self.celula[38, 20] = 1
        self.celula[39, 20] = 1
        self.celula[40, 20] = 1

        # Serpiente
        self.celula[30, 20] = 1
        self.celula[31, 20] = 1
        self.celula[32, 20] = 1
        self.celula[32, 19] = 1
        self.celula[33, 19] = 1
        self.celula[34, 19] = 1
        
        # Corredor
        self.celula[10, 5] = 1
        self.celula[12, 5] = 1
        self.celula[11, 6] = 1
        self.celula[12, 6] = 1
        self.celula[11, 7] = 1

        # Alguna otra que quieras añadir a partir de aquí, debe ser parte del __init__

    def bucle_principal(self):
        pausa = False
        celda_ancho = ANCHO / NXC
        celda_alto = ALTO / NYC
        while True:
            self.nueva_celula = np.copy(self.celula)
            time.sleep(0.1)
            self.pantalla.fill((30, 30, 30))

            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    exit()
                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_0:
                        exit()
                    if evento.key == pg.K_SPACE:
                        pausa = not pausa
                if sum(pg.mouse.get_pressed()) > 0:
                    posX = pg.mouse.get_pos()
                    posY = pg.mouse.get_pos()
                    celda_x = int(posX[0] / celda_ancho)
                    celda_y = int(posY[1] / celda_alto)
                    self.nueva_celula[celda_x, celda_y] = 1
            
            for y in range(0, NYC):
                for x in range (0, NXC):
                    if not pausa:
                        vecinas =   self.celula[(x - 1) % NXC, (y - 1)  % NYC] + \
                                    self.celula[(x)     % NXC, (y - 1)  % NYC] + \
                                    self.celula[(x + 1) % NXC, (y - 1)  % NYC] + \
                                    self.celula[(x - 1) % NXC, (y)      % NYC] + \
                                    self.celula[(x + 1) % NXC, (y)      % NYC] + \
                                    self.celula[(x - 1) % NXC, (y + 1)  % NYC] + \
                                    self.celula[(x)     % NXC, (y + 1)  % NYC] + \
                                    self.celula[(x + 1) % NXC, (y + 1)  % NYC]

                        if self.celula[x, y] == 0 and vecinas == 3:
                            self.nueva_celula[x, y] = 1

                        elif self.celula[x, y] == 1 and (vecinas < 2 or vecinas > 3):
                            self.nueva_celula[x, y] = 0                    
                        
                    poly = [((x)   * celda_ancho, y * celda_alto),
                    ((x+1) * celda_ancho, y * celda_alto),
                    ((x+1) * celda_ancho, (y+1) * celda_alto),
                    ((x)   * celda_ancho, (y+1) * celda_alto)]

                    if self.nueva_celula[x, y] == 0:
                        pg.draw.polygon(self.pantalla, (40, 40, 40), poly, 1)
                    else:
                        pg.draw.polygon(self.pantalla, (200, 200, 200), poly, 0)

            self.celula = np.copy(self.nueva_celula)
            pg.display.set_caption("El Juego de la Vida")
            pg.display.flip()

