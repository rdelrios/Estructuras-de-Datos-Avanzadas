# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import hashlib as hl
import random as rnd
import matplotlib.pyplot as plt
from decimal import Decimal
import matplotlib.pyplot as plt

class BloomFilter:
    def __init__(self,size,k):
        self.k=k
        self.bloom=np.array([False for i in range(size)], dtype=bool)
        self.size=size
        self.cont=0


    def regresaHash(self,dato): #cuidado con que se necesiten mas de 128 bits, mas de 32 caracteres
        hash = hl.md5(dato.encode('utf-8')).hexdigest()
        bits = int(np.ceil(np.log(self.size)/np.log(2)))
        hexa = int(np.ceil(bits/4))
        nMd5 = int(np.ceil(self.k+hexa/32))
        for i in range(nMd5-1):
            hash += hl.md5(hash.encode('utf-8')).hexdigest()
        res = []
        for i in range(0,hexa*self.k,hexa):
            res.append(int(hash[i:i+hexa],16)%self.size)
        return res
    
    def inserta(self, dato):
        posiciones=self.regresaHash(dato)
        for i in posiciones:
            self.bloom[i]=True
        self.cont+=1
        
    def busca(self, dato):
        posiciones=self.regresaHash(dato)
        i=0
        band = True
        while(band and i<len(posiciones)):
            if not self.bloom[posiciones[i]]:
                band=False
            i+=1
        return band

def getEff(ndatos):
    dicc={}
    for z in range(1,10):
        m=ndatos*(z*2)
        dicc[m]={}
        for i in range(2,10):
            bf=BloomFilter(m,i)
            cont=0
            for j in range(ndatos+1):
                bf.inserta(str(j))
            for k in range(ndatos+1,ndatos*2+1):
                falsoPos=bf.busca(str(k))
                if falsoPos==True:
                    cont+=1
            fe=float(cont/ndatos)
            if(fe>1):
                fe=1
            dicc[m][i]=fe
    return dicc 

prueba=getEff(500)
x=list(prueba[1000].keys())

for k in prueba.keys():
    y=list(prueba[k].values())
    plt.plot(x, y) 
    plt.xlabel("Tamaño k") 
    plt.ylabel("% de falsos positivos") 
    plt.title("Tamaño arreglo " + str(k)+ " con 500 datos")
    plt.show()
