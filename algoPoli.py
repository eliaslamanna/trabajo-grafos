#!/usr/bin/python3
from implementacion import *
from sys import argv

opciones = ['min_seguimientos', 'mas_imp', 'persecucion', 'comunidades', 'divulgar','divulgar_ciclo', 'cfc']

def principal(implementacion):
    respuesta, parametros = control_respuesta()
    while (respuesta):
        if(respuesta in opciones):
            
            if (respuesta == opciones[0]):
                """Minimo Seguimiento"""
                origen = parametros[0]
                destino = parametros[1]
                implementacion.min_seguimientos(origen, destino) #ANDA

            elif (respuesta == opciones[1]):
                """Delincuentes más importantes"""
                cant = int(parametros[0])
                implementacion.page_rank_visualizar(cant) #ANDA

            elif (respuesta == opciones[2]):
                """Persecución rápida"""
                encubiertos = parametros[0].split(",")
                k = int(parametros[1])
                implementacion.persecucion(encubiertos, k) #ANDA

            elif (respuesta == opciones[3]):
                """Comunidades"""
                min_integrantes = int(parametros[0])
                implementacion.comunidades(min_integrantes)

            elif (respuesta == opciones[4]):
                """Divulgación de rumor"""
                delincuente = parametros[0]
                n = int(parametros[1])
                implementacion.divulgar(delincuente, n) #ANDA

            elif (respuesta == opciones[5]):
                """Ciclo de largo n"""
                delincuente = parametros[0]
                largo = int(parametros[1])
                implementacion.divulgar_ciclo(delincuente, largo) #ANDA

            elif (respuesta == opciones[6]):
                """Componentes Fuertemente Conexas"""
                implementacion.cfc()

        respuesta, parametros = control_respuesta()
        
        
def control_respuesta():
    try:
        respuesta = input()
    except EOFError:
        respuesta = None
    if(not respuesta): return None, None
    operacion = respuesta.split(' ')
    comando = operacion[0]
    parametros = operacion[1:]
    return comando, parametros
        
        
def main(argv):
    if (len(argv)) != 1:
        print("Cantidad erronea de parametros")
        return
    grafo = crear_grafo_desde_archivo(argv[0])
    implementacion = Implementacion(grafo)
    principal(implementacion)
    

main(argv[1:])