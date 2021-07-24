from grafo import *
from biblioteca import *
from betweeness_centrality import*

def mas_importantes(grafo, cant):
    mas_importantes = centralidad(grafo)
    lista = []
    for i in mas_importantes:
        mini_lista = []
        mini_lista.append(i)
        mini_lista.append(mas_importantes[i])
        lista.append(mini_lista)
    lista.sort(key = lambda x:x[1], reverse = True)
    delincuentes = []
    for elemento in lista:
        delincuentes.append(elemento[0])
    print(delincuentes[:cant])
    return delincuentes[:cant]
    

grafo = crear_grafo_desde_archivo("minimo.tsv")
mas_importantes(grafo, 10)
