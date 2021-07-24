from label_propagation import *
from grafo import *
from biblioteca import *

def comunidades(grafo,n):
    lista = label_propagation(grafo, 5)
    contador = 1
    for i in lista:
        if(len(lista[i] >= n)):
            print("Comunidad", contador, ":", lista[i])
            contador += 1
