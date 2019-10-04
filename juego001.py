import pygame 
from grafica import *

ANCHO = 640
ALTO = 480

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([40,50])
        self.image.fill(VERDE)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 200
        self.velx = 0
        self.vely = 0

    def update(self):
        self.rect.x += self.velx
        self.rect.y +=self.vely


if __name__ == '__main__':
    #Seccion de variables

    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO,ALTO])
    jugadores = pygame.sprite.Group()

    j = Jugador()
    jugadores.add(j)

    reloj = pygame.time.Clock()
    fin = False
    #Ciclo principal
    while not fin:
        #Gestion de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    j.velx += 5
                    j.vely = 0
                if event.key == pygame.K_LEFT:
                    j.velx += -5
                    j.vely = 0
                if event.key == pygame.K_UP:
                    j.velx = 0
                    j.vely += 5
                if event.key == pygame.K_DOWN:
                    j.velx = 0
                    j.vely += -5


        #Gestion de control
        if j.rect.x < 0:
            j.rect.x = 0
            j.velx=0
        if j.rect.x > (ANCHO - j.rect.width):
            j.rect.x = ANCHO - j.rect.width
            j.velx=0
        if j.rect.y < 0:
            j.rect.y = 0
            j.vely=0
        if j.rect.y > (ALTO - j.rect.height):
            j.rect.y = ALTO - j.rect.height
            j.vely=0
        

        #Gestion pantalla
        jugadores.update()
        pantalla.fill(NEGRO)
        jugadores.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)
