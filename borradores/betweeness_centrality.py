from cola import *
import math

def camino_minimo(grafo, origen):
    visitados = set()
    padre = {}
    orden = {}
    q = Cola()
    visitados.add(origen)
    padre[origen] = None
    orden[origen] = 0
    q.encolar(origen)
    while not q.esta_vacia():
        v = q.desencolar()
        for w in grafo.adyacentes(v):
            if w not in visitados:
                visitados.add(w)
                padre[w] = v
                orden[w] = orden[v] + 1
                q.encolar(w)
    return padre, orden

def centralidad(grafo):
    cent = {}
    for v in grafo.nodos:
        cent[v] = 0
    for v in grafo.nodos:
        # hacia todos los demas vertices
        padre, distancia = camino_minimo(grafo, v)
        cent_aux = {}
        for w in grafo.nodos:
            cent_aux[w] = 0
        # Aca filtramos (de ser necesario) los vertices a distancia infinita, 
        # y ordenamos de mayor a menor
        lista = []
        for vertice in grafo.nodos:
            mini_lista = [vertice, distancia[vertice]]
            lista.append(mini_lista)
        lista.sort(key = lambda x:x[1], reverse = True)
        vertices_ordenados = []
        for elemento in lista:
            vertices_ordenados.append(elemento[0])
        for w in vertices_ordenados:
            if padre[w] != None:
                cent_aux[padre[w]] += cent_aux[w] + 1
        # le sumamos 1 a la centralidad de todos los vertices que se encuentren en 
        # el medio del camino
        for w in grafo.nodos:
            if w == v: continue
            cent[w] += cent_aux[w]
    return cent


#Hay una version que mejora los tiempos, esta es la standard. Cualquier cosa lo cambio.
