from comp_fuertemente_conexas import *
from grafo import *
from biblioteca import *

def cfc2(grafo):
    cfcs = cfc(grafo)
    contador = 1
    for i in cfcs:
        print("CFC", contador, ":", i)
        contador += 1
