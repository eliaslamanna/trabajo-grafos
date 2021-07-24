from grafo import *
from biblioteca import *

def _divulgar_ciclo(grafo, origen, actual, largo, visitados, n):
    if largo == n:
        if origen in grafo.adyacentes(actual):
            visitados.append(origen)
            return True
        return False
    for elemento in grafo.adyacentes(actual):
        if(elemento == origen):
            return False
        if elemento not in visitados:
            visitados.append(elemento)
            if(not _divulgar_ciclo(grafo, origen, elemento, largo, visitados, n + 1)):
                visitados.pop()
            else:
                return True
            
    return False

def divulgar_ciclo(grafo, origen, largo):
    visitados = []
    visitados.append(origen)
    if(_divulgar_ciclo(grafo, origen, origen, largo, visitados, 1)):
        flecha = ""
        for elemento in visitados:
            print("{} {}".format(flecha, elemento), end = " ")
            flecha = "->"
        return True
    print("No se encontro recorrido")
    return False