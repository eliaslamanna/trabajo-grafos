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
