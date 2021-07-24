from grafo import *

def crear_grafo_desde_archivo(n_arch):
    datos = {}
    with open(n_arch) as archivo:
        linea = archivo.readline().rstrip('\n')
        while linea:
            linea = linea.rstrip('\n').split("\t")
            if linea[0] not in datos:
                datos[linea[0]] = {}
            if linea[1] not in datos[linea[0]]:
                datos[linea[0]][linea[1]] = 0
            else:
                datos[linea[0]][linea[1]] += 1
            linea = next(archivo, None)
    
    graf = Grafo(True)
    for miembro in datos:
        if not graf.esta_presente(miembro):
            graf.agregar_nodo(miembro)
        for vecino in datos[miembro]:
            if not graf.esta_presente(vecino):
                graf.agregar_nodo(vecino)
            graf.agregar_enlace(miembro, vecino)

    return graf
