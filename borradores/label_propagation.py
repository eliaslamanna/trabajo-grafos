def max(dic):
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
            mayor = max(mas_repetido)
            dic[v] = mayor
    comunidades = {}
    for elemento in dic:
        if dic[elemento] not in comunidades:
            lista = [elemento]
            comunidades[dic[elemento]] = lista
        else:
            comunidades[dic[elemento]].append(elemento)
    return comunidades
