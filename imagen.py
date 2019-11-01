import pygame
import random
from grafica import *

ANCHO = 640
ALTO = 480

ANCHOIMAGEN = 12
ALTOIMAGEN = 8

def Recortar(imagen,a,b):
    info = imagen.get_rect()
    c = info[2]/a #Se le asigna la cantidad fila y la columna
    d = info[3]/b
    m = []
    x = 0
    while x < info[2]:
        y = 0
        ls = []
        while y < info[3]:
            cuadro = imagen.subsurface(x,y,c,d)
            ls.append(cuadro)
            y += d
        m.append(ls)
        x +=c
    return m

class Jugador(pygame.sprite.Sprite):
    def __init__(self,m):
        pygame.sprite.Sprite.__init__(self)
        self.m = m
        self.direccion = 0
        self.con = 0
        self.image = self.m[self.con][self.direccion]
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 100
        self.velx = 0
        self.vely = 0

    def update(self):
        self.rect.x += self.velx
        self.rect.y += self.vely
        self.image = self.m[self.con][self.direccion]
        if self.con < 2:
            self.con += 1
        else:
            self.con = 0

class Bloque(pygame.sprite.Sprite):
    def __init__(self,pto):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([60,60])
        self.image.fill(MORADO)
        self.rect = self.image.get_rect()
        self.rect.x = pto[0]
        self.rect.y = pto[1]

if __name__ == '__main__':
    '''Programa principal'''
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO,ALTO])

    jugadores = pygame.sprite.Group()
    bloques = pygame.sprite.Group()

    imagen = pygame.image.load('animals.png')
    m = Recortar(imagen,12,8)
    j = Jugador(m)
    jugadores.add(j)

    b = Bloque([300,200])
    bloques.add(b)

    fin = False
    reloj = pygame.time.Clock()
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    j.direccion = 3
                    j.velx = 0
                    j.vely = -5
                if event.key == pygame.K_DOWN:
                    j.direccion = 0
                    j.velx = 0
                    j.vely = 5
                if event.key == pygame.K_LEFT:
                    j.direccion = 1
                    j.velx = -5
                    j.vely = 0
                if event.key == pygame.K_RIGHT:
                    j.direccion = 2
                    j.velx = 5
                    j.vely = 0
            if event.type == pygame.KEYUP:
                j.velx = 0
                j.vely = 0

            '''Colision'''
            ls_col = pygame.sprite.spritecollide(j,bloques,False)
            for b in ls_col:

                if j.velx > 0:
                    print j.velx,j.rect.right,b.rect.left
                    if j.rect.right > b.rect.left:
                        j.rect.right = b.rect.left
                        j.velx = 0
                elif j.velx < 0:
                    if j.rect.left < b.rect.right:
                        j.rect.left = b.rect.right
                        j.velx = 0
                elif j.vely > 0:
                    if j.rect.top > b.rect.bottom:
                        j.rect.top = b.rect.bottom
                        j.vely = 0
                elif j.vely < 0:
                    if j.rect.bottom < b.rect.top:
                        j.rect.bottom = b.rect.top
                        j.vely = 0





        jugadores.update()
        pantalla.fill(NEGRO)
        jugadores.draw(pantalla)
        bloques.draw(pantalla)
        pygame.display.flip()
        reloj.tick(10)
