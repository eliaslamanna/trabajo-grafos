class Cola:
    def __init__(self):
        self.items = []
        
    def encolar(self,objeto):
        self.items.append(objeto)
            
    def desencolar(self):
        if self.items == []:
            raise IndexError("La cola está vacia")
        return self.items.pop(0)
    
    def esta_vacia(self):
        return self.items == []
    
    def ver_prim(self):
        if self.items == []:
            raise IndexError("La cola está vacia")
        return self.items[0]