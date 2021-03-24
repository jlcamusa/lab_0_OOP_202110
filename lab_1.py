# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 16:10:32 2021

@author: pepo
"""

import random as rnd
import numpy as np

def division(L):
    if len(L)<=10:
        return L
    else:
        L1=[]
        L=np.array_split(L,len(L)/10 )
        
        for i in L:
            L1.append(list(i))

        return L1





cartas=int(input('Cantidad de cartas: '))

p1=0
p2=0

L=list(range(1,cartas+1))
L=L*2
rnd.shuffle(L)

oculto=['*']*len(L)
oculto=division(oculto)

Tablero=L
Tablero=division(Tablero)

for i in oculto:
        print(*i)
    
while cartas>0:
    print('Turno p1')
    fila=int(input('Seleccione una fila: '))-1
    columna=int(input('Seleccione una columna: '))-1
    
    oculto[fila][columna]=Tablero[fila][columna]
    
    for i in oculto:
        print(*i)
        
    fila2=int(input('Seleccione una fila: '))-1
    columna2=int(input('Seleccione una columna: '))-1
    
    oculto[fila2][columna2]=Tablero[fila2][columna2]
    
    for i in oculto:
        print(*i)
        
    if Tablero[fila][columna]==Tablero[fila2][columna2]:
        p1+=1
        cartas-=1
        
        oculto[fila][columna]=' '
        oculto[fila2][columna2]=' '
        
    else:
        oculto[fila][columna]='*'
        oculto[fila2][columna2]='*'
        
    if cartas>0:
        print('Turno p2')
        fila=int(input('Seleccione una fila: '))-1
        columna=int(input('Seleccione una columna: '))-1
    
        oculto[fila][columna]=Tablero[fila][columna]
    
        for i in oculto:
            print(*i)
        
        fila2=int(input('Seleccione una fila: '))-1
        columna2=int(input('Seleccione una columna: '))-1
    
        oculto[fila2][columna2]=Tablero[fila2][columna2]
    
        for i in oculto:
            print(*i)
        
        if Tablero[fila][columna]==Tablero[fila2][columna2]:
            p2+=1
            cartas-=1
        
            oculto[fila][columna]=' '
            oculto[fila2][columna2]=' '
            
        else:
            oculto[fila][columna]='*'
            oculto[fila2][columna2]='*'
    
    
    
    
    
    
    