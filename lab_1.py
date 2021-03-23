# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 16:10:32 2021

@author: pepo
"""

import random as rnd
import numpy as np

cartas=int(input('Cantidad de cartas: '))

p1=0
p2=0

L=list(range(1,cartas+1))
L=L*2
rnd.shuffle(L)

oculto=['*']*len(L)
oculto=np.array_split(oculto,len(oculto)/10 )
oculto=np.array(oculto)

Tablero=np.array_split(L,len(L)/10 )
Tablero=np.array(Tablero)

for i in oculto:
    print(*i)
    