import sys
import random
import pygame
from tkinter import *
from tkinter import messagebox
pygame.init()
 
#Variables Globales
tablero = [[0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0]]
repetir = [3,7,13]
jugadores = []
turno = dado =  0
probabilidades = [0,1,1,1,2,2,2,3,3,4]
fondo = pygame.image.load("Imagenes/tablero.png")
lanzar = pygame.image.load("Imagenes/botonLanzar.png")
lanzar2 = pygame.image.load("Imagenes/botonLanzar_2.png")
pilaBlanca = pygame.image.load("Imagenes/pila-blanca.png")
pilaNegra = pygame.image.load("Imagenes/pila-negra.png")
isDado = True

#---------------------------Logica del programa---------------------------
class Cursor(pygame.Rect):          
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
    def update(self):
        self.left,self.top=pygame.mouse.get_pos()
        
class Boton(pygame.sprite.Sprite):  
    def __init__(self,imagen1,imagen2,x,y):
        self.imagen_normal=imagen1
        self.imagen_seleccion=imagen2
        self.imagen_actual=self.imagen_normal
        self.rect=self.imagen_actual.get_rect()
        self.rect.left,self.rect.top=(x,y)

    def update(self,pantalla,cursor):
        if cursor.colliderect(self.rect):
            self.imagen_actual=self.imagen_seleccion
        else: self.imagen_actual=self.imagen_normal        
        pantalla.blit(self.imagen_actual,self.rect)  

class cuadro:    
    def __init__(self, cuadro):
        self.cuadro=cuadro

class Square:
    def __init__(self, x, y, w, h, board, mn):
        self.rect = pygame.Rect(x, y, w, h)
        m,n = mn
        self.val = board[m][n]
        self.x = x
        self.y = y
        self.visible = False
        self.bandera = False

class Jugador:
    def __init__(self, nombre, movimientos):
        self.nombre = nombre
        self.fichas = 7
        self.fichasGanadoras = 0
        self.movimientos = movimientos
        
    def sumarFichaGanadora(self):
        self.fichasGanadoras += 1
    
    def agregarFicha(self):
        self.fichas -= 1
    
    def quitarFicha(self):
        self.fichas += 1    

def TirarDado():
    global probabilidades 
    return (random.choice(probabilidades))
    

#Funcion que ejecuta el movimiento en el tablero
def Mover(ficha):
    result = False
    global jugadores, tablero, repetir, turno, dado
    if 0 <= ficha + dado <= 14:
        if ficha + dado == 14:
            tablero[turno%2][ficha] = 0
            jugadores[turno%2].sumarFichaGanadora()
            result = True
        elif tablero[turno%2][ficha + dado] == 0 and (ficha + dado != 7 or tablero[(turno+1) % 2][7] == 0):
            if (3 < ficha + dado < 12 and tablero[(turno+1) % 2 ][ficha + dado] == 1):  # se come ficha
                tablero[turno%2][ficha + dado] = 1
                tablero[(turno+1) % 2][ficha + dado] = 0
                jugadores[(turno+1) % 2].quitarFicha()
            else:
                tablero[turno%2][ficha + dado] = 1
                    
            if ficha != -1: 
                tablero[turno%2][ficha] = 0
            else:
                jugadores[turno%2].agregarFicha()        
            result = True
    return result   

def CambiarTurno():
    global turno
    turno += 1

def MovimientoJugador(parX, parY, pantalla):   
    global isDado, tablero, jugadores  
    if (parX, parY) in jugadores[turno%2].movimientos and not isDado:
        ficha = jugadores[turno%2].movimientos.index((parX,parY))
        if tablero[turno%2][ficha] == 1: 
            MoverFicha(ficha, pantalla)
            
def MoverFicha(ficha, pantalla):
    isMove = Mover(ficha)
    if (isMove):
        if (jugadores[(turno-1)%2].fichasGanadoras == 7):
            MostrarGanador()
        isRepeat = ficha + dado in repetir    
        if not isRepeat:
            CambiarTurno()
        pintarFichas(pantalla)
        isDado = True    
        
def MostrarGanador():
    Tk().wm_withdraw() #to hide the main window
    messagebox.showinfo('Ha habido un ganador','Jugador' + str(turno%2 + 1) + ' ha ganado')
    
def Iniciar():
    global turno, jugadores
    j1 = Jugador("Jugador1", [(3,0),(2,0),(1,0),(0,0),(0,1),(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1),(7,0),(6,0)])
    j2 = Jugador("Jugador2", [(3,2),(2,2),(1,2),(0,2),(0,1),(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1),(7,2),(6,2)])
    jugadores = [j1, j2]

def pintarDado(pantalla):
        nombre = "dado" + str(dado)
        numDado = pygame.image.load("Imagenes/" + nombre + ".png")
        pantalla.blit(numDado,(1320,390))
        
def pintarFichas(pantalla):
    pantalla.blit(fondo,(0,140))
    for m in range(0,len(tablero)):
        for n in range(0,len(tablero[m])):
            if tablero[m][n] == 1:
                imagen = pygame.image.load("Imagenes/ficha"+ str(m + 1) + ".png")
                pantalla.blit(imagen,(jugadores[m].movimientos[n][0] * 162 + 30, jugadores[m].movimientos[n][1] * 162 + 180))
    
def Pantalla(): 
    global dado, jugadores, turno, isDado 
    Iniciar()
    btnLanzar = Boton(lanzar,lanzar2,1300, 500)
    btnPilaBlanca = Boton(pilaBlanca,pilaBlanca,480, -10)
    btnPilaNegra = Boton(pilaNegra, pilaNegra,480, 635)
    
    pantalla = pygame.display.set_mode((1500,800))
    pantalla.blit(fondo,(0,140))    
    cursor=Cursor()
                 
    matriz=cuadro([[1,1,1],[1,1,1],[1,1,1],[1,1,1],[0,1,0],[0,1,0],[1,1,1],[1,1,1]])
    lista = [[] for m in range(8)]        
    for m in range(0, 8 * 162, 162):
        for n in range(0, 3*162, 162):
            lista[m//162]+=[Square(m + 30,n + 180,162,162,matriz.cuadro,(m//162,n//162))]
    
    corriendo = True
    while corriendo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo = False
                pygame.quit()
            
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for m in lista:
                    for n in m:
                        r = pygame.Rect(pygame.mouse.get_pos(), (1, 1))
                        if n.rect.colliderect(r):
                            MovimientoJugador((n.x-30)//162, (n.y-180) // 162, pantalla)
                print ("Turno " + str(turno%2))
                if cursor.colliderect(btnLanzar.rect):
                    if(isDado):
                        dado = TirarDado()
                        pintarDado(pantalla)
                        isDado = False
                    if dado == 0:
                        CambiarTurno()
                if cursor.colliderect(btnPilaBlanca.rect) and turno%2 == 0 and not isDado:
                    MoverFicha(-1, pantalla)
                if cursor.colliderect(btnPilaNegra.rect) and turno%2 == 1 and not isDado:
                    MoverFicha(-1, pantalla)
        cursor.update()
        imagen = pygame.image.load("Imagenes/ficha"+ str(turno%2 + 1) + ".png")
        pantalla.blit(imagen,(1350, 100))
        btnLanzar.update(pantalla,cursor)
        btnPilaBlanca.update(pantalla,cursor)
        btnPilaNegra.update(pantalla,cursor)
        pygame.display.update()
    
    
    corriendo = True
    while corriendo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo = False
                pygame.quit()
    
Pantalla()