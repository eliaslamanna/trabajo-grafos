from grafo import *

class ArchivoNoEncontradoError(Exception):
    pass


class Pila:
    def __init__(self):
        self.items = []
        
    def apilar(self,objeto):
        self.items.append(objeto)
        
    def desapilar(self):
        if self.items == []:
            raise IndexError("La pila está vacía")
        return self.items.pop()
        
    def esta_vacia(self):
        return self.items == []
    
    def ver_tope(self):
        if self.items == []:
            raise IndexError("La pila está vacía")
        return self.items[-1]
    

class Cola:
    def __init__(self):
        self.items = []
        
    def encolar(self,objeto):
        self.items.insert(0, objeto)
            
    def desencolar(self):
        if self.items == []:
            raise IndexError("La cola está vacia")
        return self.items.pop()
    
    def esta_vacia(self):
        return self.items == []
    
    def ver_prim(self):
        if self.items == []:
            raise IndexError("La cola está vacia")
        return self.items[0]


def crear_grafo_desde_archivo(n_arch):
    graf = Grafo()
    try:
        with open(n_arch, 'r') as archivo:
            for linea in archivo:
                delincuente1, delincuente2 = linea.strip('\n').split("\t")
                graf.agregar_enlace(delincuente1,delincuente2)
    except IOError:
        raise ArchivoNoEncontradoError("El archivo no existe en el directorio")
    return graf

def recorrido_dfs_completo(grafo):
    visitados = set()
    padre = {}
    orden = {}
    for v in grafo:
        if v not in visitados:
            orden[v] = 0
            padre[v] = none
            dfs(grafo, v, visitados, padre, orden)
    return padre, orden


def bfs(grafo, origen):
    visitados = set()
    padre = {}
    orden = {}
    q = cola()
    visitados.agregar(origen)
    padre[origen] = none
    orden[origen] = 0
    q.encolar(origen)
    while not q.esta_vacia():
        v = q.desencolar()
        for w in grafo.adyacentes(v):
            if w not in visitados:
                visitados.agregar(w)
                padre[w] = v
                orden[w] = orden[v] + 1
                q.encolar(w)
    return padre, orden


def dfs(grafo, v , visitados, padre, orden):
    visitados.agregar(v)
    for w in grafo.adyacentes(v):
        if w not in visitados:
            padre[w] = v
            orden[w] = orden[v] + 1
            dfs(grafo, w, visitados, padre, orden)
            


def dfs_cfc(grafo, v, visitados, orden, p, s, cfcs, en_cfs):
    visitados.add(v)
    s.apilar(v)
    p.apilar(v)
    for w in grafo.adyacentes(v):
        if w not in visitados:
            orden[w] = orden[v] + 1
            dfs_cfc(grafo, w, visitados, orden, p, s, cfcs, en_cfs)
        elif w not in en_cfs:
            while not p.esta_vacia() and orden[p.ver_tope()] > orden[w]:
                p.desapilar()

    if not p.esta_vacia() and p.ver_tope() == v:
        p.desapilar()
        z = None
        nueva_cfc = []
        while z != v:
            z = s.desapilar()
            en_cfs.add(z)
            nueva_cfc.append(z)
        cfcs.append(nueva_cfc)


def dijkstra(grafo, origen):
    dist = {}
    padre = {}
    for v in grafo:
        dist[v] = infinito
    dist[origen] = 0
    padre[origen] = none
    q = heap_crear()
    q.encolar(origen, 0)
    while not q.esta_vacio():
        v = q.desencolar()
        #Aca va if v == .... return.... si quiero que haga el recorrido hasta cierto vertice
        for w in grafo.adyacentes(v):
            if (dist[v] + grafo.peso(v, w) ) < dist[w]:
                dist[w] = dist[v] + grafo.peso(v, w)
                padre[w] = v
                q.encolar(w, dist[w])
    return padre, dist

def maximo(dic):
    lista = []
    for elemento in dic:
        mini_lista = []
        mini_lista.append(elemento)
        mini_lista.append(dic[elemento])
        lista.append(mini_lista)
    lista.sort(key = lambda lista:lista[1])
    return lista[-1][0]

def label_propagation(grafo, n): #la n es para que mejor la aproximacion repitiendo varias veces lo mismo
    dic = {}
    i = 0
    for v in grafo.nodos:
        dic[v] = i
        i += 1
    for x in range(n):
        for v in grafo.nodos:
            mas_repetido = {}
            for w in grafo.adyacentes(v):
                if dic[w] not in mas_repetido:
                    mas_repetido[dic[w]] = 1
                else:
                    mas_repetido[dic[w]] += 1
            mayor = maximo(mas_repetido)
            dic[v] = mayor
    comunidades = {}
    for elemento in dic:
        if dic[elemento] not in comunidades:
            lista = [elemento]
            comunidades[dic[elemento]] = lista
        else:
            comunidades[dic[elemento]].append(elemento)
    return comunidades

def camino_minimo(grafo, origen, destino = None):
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
        if(destino and v == destino):
            return padre, orden
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
            if vertice in distancia:
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


def divulgar_ciclo_(grafo, origen, actual, largo, visitados, n):
    if largo == n:
        if origen in grafo.adyacentes(actual):
            visitados.append(origen)
            return True
        return False
    for elemento in grafo.adyacentes(actual):
        if elemento not in visitados:
            visitados.append(elemento)
            if(not divulgar_ciclo_(grafo, origen, elemento, largo, visitados, n + 1)):
                visitados.pop()
            else:
                return True
    return False

def pageRank(grafo):
    pRank = {}
    for vertice in grafo.nodos:
        pRank[vertice] = 1
    for i in range(3):
        for vertice in grafo.nodos:
            if(len(grafo.adyacentes(vertice)) > 1):
                valorAsumar = pRank[vertice]/len(grafo.adyacentes(vertice))
            else:
                valorAsumar = pRank[vertice]
            for adyacente in grafo.adyacentes(vertice):
                pRank[adyacente] += valorAsumar
    return pRank