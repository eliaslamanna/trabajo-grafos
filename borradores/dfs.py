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

def dfs(grafo, v , visitados, padre, orden):
    visitados.agregar(v)
    for w in grafo.adyacentes(v):
        if w not in visitados:
            padre[w] = v
            orden[w] = orden[v] + 1
            dfs(grafo, w, visitados, padre, orden)
