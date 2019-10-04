import pygame 
import random
from grafica import *


'''
Rama : b1_2dir
Autor: Nicolas Mesa Serna
Descripcion: Movimiento en 2 direcciones rivales

'''
ANCHO = 640
ALTO = 480

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([40,50])
        self.image.fill(VERDE)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = ALTO - self.rect.height
        self.velx = 0

    def update(self):
        self.rect.x += self.velx


class Rival(pygame.sprite.Sprite):
    def __init__(self):
        '''Constructor rival'''
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([40,50])
        self.image.fill(ROSADO)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 200
        self.velx = 5
        self.vely = 0
        self.disparar = False
        self.temp = random.randrange(150)

    def Pos(self):
        '''Retorna posicion del jugador'''
        p = [self.rect.centerx,self.rect.y]
        return p

    def update(self):
        '''Actualizar obejto'''
        self.rect.x += self.velx
        if self.rect.x > (ANCHO - self.rect.width):
            self.velx = -5
        if self.rect.x < 0:
            self.velx = +5
        self.temp-= 1        


if __name__ == '__main__':
    #Seccion de variables

    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO,ALTO])
    
    #Inicializar grupos
    jugadores = pygame.sprite.Group()
    rivales  = pygame.sprite.Group()
    

    j = Jugador()
    jugadores.add(j)


    #Inicializar rivales
    n = 10 
    for i in range(n):
        r = Rival()
        r.rect.x = random.randrange(ANCHO)
        r.rect.y = random.randrange(ALTO - 100)
        rivales.add(r)

    reloj = pygame.time.Clock()
    fin = False
    #Ciclo principal
    while not fin:
        #Gestion de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.KEYDOWN:
                #Gestion de teclas
                if event.key == pygame.K_RIGHT:
                    j.velx += 5
                        
                if event.key == pygame.K_LEFT:
                    j.velx += -5

            if event.type == pygame.KEYUP:
                #Objeto se detiene al liberar
                j.velx = 0


        #Gestion de control

        #Control de limites del jugador
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

        #Gestion de rivales
        for r in rivales:

            if r in rivales:
                if r.temp == 0:
                    r.disparar = True
            if r.disparar:
                r.disparar = False
                r.temp = random.randrange(150)



        #Gestion pantalla
        jugadores.update()
        rivales.update()

        #Despeglegar graficos
        pantalla.fill(NEGRO)
        rivales.draw(pantalla)
        jugadores.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)
