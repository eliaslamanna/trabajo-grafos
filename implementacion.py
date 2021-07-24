from biblioteca import *
from math import inf

class Implementacion:
    def __init__(self,grafo):
        self.grafo = grafo
        
    def _min_seguimientos(self, origen, destino):
        if not (self.grafo.esta_presente(origen) and self.grafo.esta_presente(destino)):
            #print("Seguimiento imposible")
            return None
        padres, orden = camino_minimo(self.grafo, origen, destino)
        if(destino not in padres):
            #print("Seguimiento imposible")
            return None
        camino = []
        vertice = destino
        camino.append(vertice)
        while(padres[vertice] != None):
            camino.append(padres[vertice])
            vertice = padres[vertice]
        return camino[::-1]

    def min_seguimientos(self, origen, destino):
        camino2 = self._min_seguimientos(origen, destino)
        if(camino2 == None): return print("Seguimiento imposible")
        self.mostrar_resultado(camino2," -> ") # aca se puede hacer solo camino[::-1]
        
    def mas_imp(self, cant):
        mas_importantes = centralidad(self.grafo)
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
        self.mostrar_resultado(delincuentes[:cant], ", ")
        
    def persecucion(self, l_delicuentes, k):
        del_mas_imp = self.page_rank_calcular(k)
        camino_menos_largo = []
        camino_menos_largo_tam = inf
        for i in range(0, len(l_delicuentes)):
            for w in del_mas_imp:
                p_camino = self._min_seguimientos(l_delicuentes[i], w)
                if (p_camino and len(p_camino) < camino_menos_largo_tam):
                    camino_menos_largo = p_camino
                    camino_menos_largo_tam = len(p_camino)
                # if not p_camino: continue
                # if not camino:
                #     camino = p_camino
                # elif len(p_camino) < len(camino):
                #     camino = p_camino
                # elif len(p_camino) == len(camino):
                #     for delicuente in del_mas_imp:
                #         if delicuente == p_camino[-1]:
                #             camino = p_camino
                #             break
                #         elif delicuente == camino[-1]:
                #             break
        self.mostrar_resultado(camino_menos_largo, " -> ")
        
    def comunidades(self,n):
        lista = label_propagation(self.grafo, 5)
        contador = 1
        for i in lista:
            if(len(lista[i]) >= n):
                print("Comunidad", contador, ":", lista[i])
            contador+=1
            
    def divulgar(self,delincuente,n):
        visitados = set()
        orden = {}
        q = Cola()
        visitados.add(delincuente)
        orden[delincuente] = 0
        q.encolar(delincuente)
        lista = []
        while not q.esta_vacia():
            v = q.desencolar()
            for w in self.grafo.adyacentes(v):
                if(orden[v] + 1 > n):
                	self.mostrar_resultado(lista, ", ")
                	return
                if w not in visitados:
                	visitados.add(w)
                	orden[w] = orden[v] + 1
                	q.encolar(w)
                	lista.append(w)

        
    def divulgar_ciclo(self, origen, largo):
        visitados = []
        visitados.append(origen)
        if divulgar_ciclo_(self.grafo, origen, origen, largo, visitados, 1):
            self.mostrar_resultado(visitados, " -> ")
            return
        print("No se encontro recorrido")
        
    def cfc(self):
        visitados = set()
        orden = {}
        p = Pila()
        s = Pila()
        cfcs = []
        en_cfs = set()
        for v in self.grafo.nodos:
            if v not in visitados:
                orden[v] = 0
                dfs_cfc(self.grafo, v, visitados, orden, p, s, cfcs, en_cfs)
        contador = 1
        for i in cfcs:
            print("CFC", contador, end = ": ")
            self.mostrar_resultado(i, ", ")
            contador+=1
 
    def mostrar_resultado(self, resultado, union):
            for elemento in resultado[:-1]:
                print("{}".format(elemento), end = union)
            print(resultado[-1])

    def page_rank_calcular(self, cant):
        rank = pageRank(self.grafo)
        dic = {}    # clave: pRank ; valor: vertice
        for elem in rank:
            dic[rank[elem]] = elem
        lista = sorted(rank.values())
        mas_imp = []
        for elem in lista[:-(cant+1):-1]:
            mas_imp.append(dic[elem])
        return mas_imp

    def page_rank_visualizar(self, cant):
        mas_imp = self.page_rank_calcular(cant)
        self.mostrar_resultado(mas_imp,", ")