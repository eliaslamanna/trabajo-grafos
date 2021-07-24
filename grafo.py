class Nodo:
    def __init__(self, nombre_nodo):
        self.nombre = nombre_nodo
        self.enlaces = {}
        
    def agregar_enlace(self, nodo, peso_enlace = None):
        """Crea un enlace entre el nodo actual y el recibido, y le asigna un peso"""
        self.enlaces[nodo.nombre] = peso_enlace
    
    def esta_enlazado(self,nodo):
        """Devueltre True si el actual y el recibido estan conectados"""
        return(nodo.nombre in self.enlaces)
    
    def obtener_nombre(self):
        """Devuelve el nombre del nodo"""
        return self.nombre
    
    def obtener_enlaces(self):
        """Devuelve una lista de los nodos enlazados al actual"""
        return self.enlaces
   

class Grafo:
    def __init__(self):
        self.nodos = {}
        
    def agregar_nodo(self, nombre_nodo):
        """Crea un nodo para el grafo, con el peso indicado o None"""
        self.nodos[nombre_nodo] = Nodo(nombre_nodo)


    def agregar_enlace(self, nombre_nodo_inicio, nombre_nodo_fin):
        """Crea un enlace entre los 2 nodos dados con el peso recibido o None"""
        for nodo in (nombre_nodo_inicio, nombre_nodo_fin):
            if nodo not in self.nodos:
                self.agregar_nodo(nodo)
        self.nodos[nombre_nodo_inicio].agregar_enlace(self.nodos[nombre_nodo_fin])

    def esta_presente(self, nombre_nodo):
        """Devuelve True si el nombre dado esta en el grafo"""
        try:
            self.nodos[nombre_nodo]
            return True
        except KeyError:
            return False

        
    def obtener_nodo(self, n_nodo):
        return self.nodos[n_nodo]
    
    def adyacentes(self, n_nodo):
        """Devuelve una lista de los nodos enlazados al actual"""
        return self.nodos[n_nodo].enlaces