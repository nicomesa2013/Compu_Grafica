import pygame
import math

AZUL = [0,0,255]
VERDE = [0,255,0]
ROJO = [255,0,0]
BLANCO = [255,255,255]
NEGRO = [0,0,0]
ROSADO = [255,0,128]
MORADO = [183,28,239]

def Punto (p, pos, cl = BLANCO):
    pygame.draw.circle(p,cl,pos,2)
    pygame.display.flip()

def prod_escalar(a,pto):
    res = []
    for e in pto:
        res.append(a * e)
    return res    

def Cart_pant(pto,origen):
    xp = pto[0] + origen[0]
    yp = -pto[1] + origen[1]
    return [xp,yp]

def Pant_cart(pto,origen):
    x = pto[0] - origen[0]
    y = -pto[1] + origen[1] 
    return [x,y]

def Polar(r,Angulo):
    R = math.radians(Angulo)
    xp = r*math.cos(R)
    yp = r*math.sin(R)
    return [int(xp),int(yp)]
def Escalar(pto,s):
    xp = pto[0]*s[0]
    yp = pto[1]*s[1]
    return [int(xp),int(yp)]

def Trasladar(pto,a):
    xt = pto[0] + a[0]
    yt = pto[1] + a[1]
    return [xt,yt]

def Rotar(pto,Angulo):
    R = math.radians(Angulo)
    x = pto[0]
    y = pto[1]
    pto[0] = (x*math.cos(R)) - (y*math.sin(R))
    pto[1] = (x*math.sin(R)) + (y*math.cos(R))
    return [int(pto[0]),int(pto[1])]

def RotarF(ls,con):
    #Declaramos el punto fijo
    pf = ls[0]

    #Se multiplica por producto escalar para llevar a origen
    t = prod_escalar(-1,pf)

    #Se traslada al origen
    lsO = []
    for i in ls:
        lsO.append(Trasladar(i,t))

    #Rotar en el origen
    lsR = []
    for i in lsO:
        lsR.append(Rotar(i,con))
    
    #Trasladar de nuevo al punto fijo
    t = pf
    lsF = []
    for i in lsO:
        lsF.append(Trasladar(i,t))
    return lsF