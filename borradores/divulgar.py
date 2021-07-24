from grafo import *
from biblioteca import *
from cola import *

def divulgar(grafo,delincuente,n):
    visitados = set()
    orden = {}
    q = Cola()
    visitados.add(delincuente)
    orden[delincuente] = 0
    q.encolar(delincuente)
    lista = []
    while not q.esta_vacia():
        v = q.desencolar()
        for w in grafo.adyacentes(v):
            if(orden[v] + 1 > n):
                print(lista)
                return
            if w not in visitados:
                visitados.add(w)
                orden[w] = orden[v] + 1
                q.encolar(w)
                lista.append(w)
