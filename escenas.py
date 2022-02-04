import pygame as pg
from __init__ import *
from entidades import *

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
            pg.display.flip()

class Partida(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        self.tablero = Tablero()

    def bucle_principal(self):
        while True:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    exit()

            self.pantalla.fill((41, 50, 49))
            self.tablero.show(self.pantalla)
            pg.display.flip()
