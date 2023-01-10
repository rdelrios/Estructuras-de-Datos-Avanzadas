#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  9 12:27:34 2022

@author: robertodelriosalgado
"""

class NodoTrie:
    def __init__(self):
        self.flag=False
        self.sim={}
    

        
class Trie:
    def __init__(self):
        self.raiz=NodoTrie()
        self.cont=0
        self.raiz.flag=True
    
    def inserta(self,dato):
        aux=self.raiz
        for k in dato:
            if k in aux.sim.keys():
                aux=aux.sim[k]
            else:
                aux.sim[k]=NodoTrie()
                aux=aux.sim[k]
        aux.flag=True
        self.cont+=1
        
    def busca(self, dato):
        aux=self.raiz
        flag = True
        while(flag):
            for k in dato:
                if k in aux.sim.keys():
                    aux=aux.sim[k]
                else:
                    flag = False
                    break
        return aux.flag
    
    def _recorre(self, actual, lista, cad):
        if (actual.flag):
            lista.append(cad)
        for k in actual.sim.keys():
            self._recorre(actual.sim[k], lista ,cad+k)
    
    def recorre(self):
        lista=[]
        cad=""
        aux=self.raiz
        self._recorre(aux,lista,cad)
        return lista

trie = Trie()
trie.inserta("hola")
trie.inserta("roberto")

print(trie.recorre())