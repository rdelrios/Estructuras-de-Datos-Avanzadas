#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 11:33:57 2022

@author: robertodelriosalgado
"""

import networkx as nx
import numpy as np
import heapdict as hd 
# goodnotes o Notability

class Grafo:
  def __init__(self):
    self.G={}
    self.visitados={}

  def insertaNodo(self,v1):
    if v1 not in self.G:
      self.G[v1]={}

  def insertaDirigido(self,v1,v2,peso=None):

    if v1 not in self.G:
      self.G[v1]={v2:peso}
    else:   
        self.G[v1][v2]=peso
    if v2 not in self.G:
      self.G[v2]={}

  def inserta(self,v1,v2,peso=None):
    self.insertaDirigido(v1,v2,peso)
    self.insertaDirigido(v2,v1,peso)


  def _recorreDFS(self,actual,lista):

    self.visitados[actual]=True
    lista.append(actual)
    for v in self.G[actual]:
      if not self.visitados[v]:
        self._recorreDFS(v,lista)

  def DFS(self): #Depth First Search, recorrido a profundida
    # inicializar el visitados
    for v in self.G:
      self.visitados[v]=False
    lista=[]
    for v in self.G:
      if not self.visitados[v]:
        self._recorreDFS(v,lista)
    return lista


  def BFS(self):
    for v in self.G:
      self.visitados[v]=False
    lista=[]
    for v in self.G:
      if not self.visitados[v]:
        self._recorreBFS(v,lista)
    return lista

  def _recorreBFS(self,actual,lista):
    cola=[]
    self.visitados[actual]=True
    cola.append(actual)
    while len(cola)!=0:
      actual=cola.pop(0)
      lista.append(actual)
      for vecino in self.G[actual].keys():
        if not self.visitados[vecino]:
          self.visitados[vecino]=True
          cola.append(vecino)


  def Prim(self,v_ini):
    key=hd.heapdict()
    papa={}
    for v in self.G:
      key[v]=np.inf
      papa[v]=None
    key[v_ini]=0
    while len(key)>0:
      actual,costo=key.popitem()
      for vecino in self.G[actual]:
        if vecino in key and self.G[actual][vecino] < key[vecino]:
          key[vecino]=self.G[actual][vecino]
          papa[vecino]=actual

    return papa


  def Dijkstra(self,v_ini):
    key=hd.heapdict()
    papa={}
    for v in self.G:
      key[v]=np.inf
      papa[v]=None
    key[v_ini]=0
    while len(key)>0:
      actual,costo=key.popitem()
      for vecino in self.G[actual]:
        if vecino in key and costo+self.G[actual][vecino] < key[vecino]:
          key[vecino]=costo+self.G[actual][vecino]
          papa[vecino]=actual

    return papa


g2=Grafo()

g2.inserta("a","b",4)
g2.inserta("a","h",8)
g2.inserta("b","c",8)
g2.inserta("b","h",11)
g2.inserta("c","d",7)
g2.inserta("c","f",4)
g2.inserta("c","i",2)
g2.inserta("d","e",9)
g2.inserta("d","f",14)
g2.inserta("e","f",10)
g2.inserta("f","g",2)
g2.inserta("g","h",1)
g2.inserta("g","i",6)
g2.inserta("h","i",7)

g2.G

gr1 = nx.Graph(g2.G)

lay=nx.spring_layout(gr1) # escoger un layout, como poner los vértices (puede ser en círculo, etc)
#lay=nx.circular_layout(gr1)
# network x necesita un diccionario donde la llave es una pareja de vértices y el valor el peso de esa arista. La creamos de nuestera estrucutura usando un dict comprehension
# que es como un list comprehension pero con diccionario
edge_labels={(u,v):g2.G[u][v] for u,v in gr1.edges}
nx.draw_networkx_edge_labels(gr1,lay,edge_labels=edge_labels)

nx.draw(gr1,lay, with_labels=True) # dibuja el grafo de networkx usando el layout que escogimos y que le ponga nombre a los vértices