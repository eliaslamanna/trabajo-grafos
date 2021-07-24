class NodoRepetidoError(Exception):
    pass

class EnlaceRepetidoError(Exception):
    pass

class NodoInexistenteError(Exception):
    pass

class EnlaceInexistenteError(Exception):
    pass
    
class Nodo:
    def __init__(self, dirigido, nombre_nodo,dato = None):
        self.nombre = nombre_nodo
        self.dato = dato
        self.enlaces = {}
        self.dirigido = dirigido
        
    def agregar_enlace(self, nodo, peso_enlace = None):
        """Crea un enlace entre el nodo actual y el recibido, y le asigna un peso.
        Si el grafo no es dirigido, crea el enlace en el recibido tambien"""
        if nodo.nombre in self.enlaces:
            raise EnlaceRepetidoError("Ya existe un enlace entre {} y {}".format(self.nombre,nodo.nombre))
        self.enlaces[nodo.nombre] = peso_enlace
        if not self.dirigido:
            nodo.enlaces[self.nombre] = peso_enlace
            
    def quitar_enlace(self, nodo):
        """Elimina el enlace entre el nodo actual y el recibido.
        Si el grafo no es dirigido, elimina el enlace en el recibido tambien"""
        if nodo.nombre not in self.enlaces:
            raise EnlaceInexistenteError
        peso = self.enlaces.pop(nodo.nombre)
        if not self.dirigido:
            nodo.enlaces.pop(self.nombre)
        return peso
    
    def obtener_peso_enlace(self,nodo):
        """Devuelve el peso del enlace entre el actual y el recibido"""
        if nodo.nombre not in self.enlaces:
            raise EnlaceInexistenteError
        return self.enlaces[nodo.nombre]
    
    def esta_enlazado(self,nodo):
        """Devueltre True si el actual y el recibido estan conectados"""
        return(nodo.nombre in self.enlaces)
    
    def obtener_nombre(self):
        """Devuelve el nombre del nodo"""
        return self.nombre
    
    def obtener_peso(self):
        """Devuelve el peso del nodo"""
        return self.dato
    
    def obtener_enlaces(self):
        """Devuelve una lista de los nodos enlazados al actual"""
        return self.enlaces
    
    def cantidad_enlaces(self):
        """Devuelve la cantidad de enlaces que tiene el actual"""
        return len(self.enlaces)
   



class Grafo:
    def __init__(self, dirigido = False):
        self.dirigido = dirigido
        self.nodos = {}
        self.n_nodos = 0
        self.n_enlaces = 0
        
    def agregar_nodo(self, nombre_nodo, peso = None):
        """Crea un nodo para el grafo, con el peso indicado o None.
           Que sea dirigido o no, depende de si el grafo lo es o no."""
        if nombre_nodo in self.nodos:
            raise NodoRepetidoError("El nodo {} ya existe en el grafo".format(nombre_nodo))
        self.nodos[nombre_nodo] = Nodo(self.dirigido, nombre_nodo, peso)
        self.n_nodos += 1
        
    def quitar_nodo(self,nombre_nodo):
        """Quita el nodo del grafo.
           Si el nodo tenia enlaces, estos tambien son eliminados"""
        if nombre_nodo not in self.nodos:
            raise NodoInexistenteError("El nodo {} no existe en el grafo".format(nodo))
        nodo_borrar = self.nodos.pop(nombre_nodo)
        for nodo_vecino in self.nodos:
            try:
                self.nodos[nodo_vecino].quitar_enlace(nodo_borrar)
                self.n_enlaces-= 1
            except EnlaceInexistenteError:
                pass
        self.n_enlaces -= nodo_borrar.cantidad_enlaces()
        self.n_nodos -= 1

    def agregar_enlace(self, nombre_nodo_inicio, nombre_nodo_fin, peso = None):
        """Crea un enlace entre los 2 nodos dados con el peso recibido o None"""
        for nodo in (nombre_nodo_inicio,nombre_nodo_fin):
            try:
                self.nodos[nodo]
            except KeyError:
                raise NodoInexistenteError("El nodo '{}' no existe en el grafo".format(nodo))
        self.nodos[nombre_nodo_inicio].agregar_enlace(self.nodos[nombre_nodo_fin], peso)
        self.n_enlaces += 1

    def quitar_enlace(self, nombre_nodo_inicio, nombre_nodo_fin):
        """Elimina el enlace entre los nodos recibidos"""
        if not self.nodos[nombre_nodo_inicio].esta_enlazado(self.nodos[nombre_nodo_fin]):
            raise EnlaceInexistenteError("No existe un enlace entre {} y {}".format(self.nombre,nodo.nombre))
        self.nodos[nombre_nodo_inicio].quitar_enlace(self.nodos[nombre_nodo_fin])
        self.n_enlaces -= 1

    def obtener_peso_nodo(self, nombre_nodo):
        """Devuelve el peso del nodo recibido"""
        try:
            self.nodos[nodo]
        except KeyError:
            raise NodoInexistenteError("El nodo '{}' no existe en el grafo".format(nodo))
        return self.nodos[nombre_nodo].obtener_peso()
    
    def obtener_peso_enlace(self, nombre_nodo_inicio, nombre_nodo_fin):
        """Devuelve el peso del enlace de los nodos recibidos"""
        for nodo in (nombre_nodo_inicio,nombre_nodo_fin):
            try:
                self.nodos[nodo]
            except KeyError:
                raise NodoInexistenteError("El nodo '{}' no existe en el grafo".format(nodo))
        if not self.nodos[nombre_nodo_inicio].esta_enlazado(self.nodos[nombre_nodo_fin]):
            raise EnlaceInexistenteError("No existe un enlace entre {} y {}".format(self.nombre,nodo.nombre))
        return self.nodos[nombre_nodo_inicio].obtener_peso_enlace(self.nodos[nombre_nodo_fin])

    def cantidad_enlaces(self):
        """Devuelve la cantidad de enlaces en el grafo"""
        return self.n_enlaces

    def cantidad_nodos(self):
        """Devuelve la cantidad de nodos en el grafo"""
        return len(self.nodos)
    
    def esta_presente(self, nombre_nodo):
        """Devuelve True si el nombre dado esta en el grafo"""
        try:
            self.nodos[nombre_nodo]
            return True
        except KeyError:
            return False
        
    def obtener_nodo(self, n_nodo):
        if not self.esta_presente(n_nodo):
            raise NodoInexistenteError("El nodo '{}' no existe en el grafo".format(nodo))
        return self.nodos[n_nodo]
    
    def adyacentes(self, n_nodo):
        """Devuelve una lista de los nodos enlazados al actual"""
        try:
            return self.nodos[n_nodo].enlaces
        except KeyError:
            raise NodoInexistenteError("El nodo '{}' no existe en el grafo".format(nodo))
    
        
        
    
