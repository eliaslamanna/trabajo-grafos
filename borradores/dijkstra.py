from heapq import*
import math

def dijkstra(grafo, origen, destino):
    dist = {}
    padre = {}
    for v in grafo.nodos:
        dist[v] = math.inf
    dist[origen] = 0
    padre[origen] = None
    q = Heapq()
    q.heappush(origen, 0)
    while not q.esta_vacio():
        v = q.heappop()
        if v == destino:
            return padre, dist
        for w in grafo.adyacentes(v):
            if (dist[v] + grafo.peso(v, w) ) < dist[w]:
                dist[w] = dist[v] + grafo.peso(v, w)
                padre[w] = v
                q.heappush(w, dist[w])
    return padre, dist