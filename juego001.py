import pygame
import random
from grafica import *


'''
Rama :
Autor: Nicolas Mesa Serna
Descripcion: Implementacion de barra de vida

'''
ANCHO = 640
ALTO = 480

class Jugador(pygame.sprite.Sprite):
    '''Clase jugador'''
    def __init__(self):
        '''Constructor'''
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([40,50])
        self.image.fill(VERDE)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = ALTO - self.rect.height
        self.velx = 0
        self.vidas = 3


    def Pos(self):
        '''Retorna posicion del jugador'''
        p = [self.rect.centerx,self.rect.y]
        return p

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

class Bala(pygame.sprite.Sprite):
    def __init__(self,pos,cl = ROSADO):
        '''Constructor'''
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([5,30])
        self.image.fill(cl)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.vely = -7

    def update(self):
        '''Actualizar objeto'''
        self.rect.y+=self.vely


if __name__ == '__main__':
    #Seccion de variables

    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO,ALTO])

    fuente = pygame.font.Font(None,32)
    #Inicializar jugador
    jugadores = pygame.sprite.Group()
    rivales  = pygame.sprite.Group()
    balas = pygame.sprite.Group()
    balasR = pygame.sprite.Group()

    j = Jugador()
    vidas = j.vidas
    jugadores.add(j)
    rivales  = pygame.sprite.Group()

    #Inicializar rivales
    n = 10
    for i in range(n):
        r = Rival()
        r.rect.x = random.randrange(ANCHO)
        r.rect.y = random.randrange(ALTO - 100)
        rivales.add(r)

    fin_juego = False
    reloj = pygame.time.Clock()
    fin = False
    #Ciclo principal
    while (not fin) and (not fin_juego):
        #Gestion de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.KEYDOWN:
                #Gestion de teclas
                if event.key == pygame.K_RIGHT:
                    j.velx = 5

                if event.key == pygame.K_LEFT:
                    j.velx = -5

            if event.type == pygame.KEYUP:
                #Objeto se detiene al liberar
                j.velx = 0


            if event.type == pygame.MOUSEBUTTONDOWN:
                b = Bala(j.Pos())
                balas.add(b)




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


        #Gestion colisiones balas
        for b in balas:
            ls = pygame.sprite.spritecollide(b,rivales,True)
            for e in ls:
                balas.remove(b)

            #Control de limites
            if b.rect.y < -30:
                balas.remove(b)

        #Gestion de rivales
        for r in rivales:
            if r.temp == 0:
                r.disparar = True
            if r.disparar:
                b = Bala(r.Pos(),AZUL)
                b.vely = 7
                balasR.add(b)
                r.disparar = False
                r.temp = random.randrange(150)

        #Gestion balas rivales
        for b in balasR:
            ls = pygame.sprite.spritecollide(b,jugadores,True)
            for e in ls:
                balasR.remove(b)
                vidas-=1
                j = Jugador()
                j.vidas = vidas
                jugadores.add(j)
            if b.rect.y > ALTO:
                balasR.remove(b)

        if vidas < 0:
            fin_juego = True
        #Actualizar objetos
        jugadores.update()
        rivales.update()

        #






        balas.update()
        balasR.update()
        #Gestion pantalla
        texto = 'Vidas:'+str(j.vidas)
        info = fuente.render(texto,True,BLANCO)

        #Desplegar graficos
        pantalla.fill(NEGRO)
        pantalla.blit(info,[50,10])
        jugadores.draw(pantalla)
        rivales.draw(pantalla)
        balas.draw(pantalla)
        balasR.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)

    fuente = pygame.font.Font(None,38)
    texto = 'Fin de juego'
    info = fuente.render(texto,True,MORADO)
    pantalla.fill(NEGRO)
    pantalla.blit(info,[150,150])
    pygame.display.flip()
    
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
