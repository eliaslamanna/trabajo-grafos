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
