class _Nodo:
    def __init__(self, dato, prox):
        self.dato = dato
        self.prox = prox
    
    def __str__(self):
        return f"Nodo({self.dato})"

class ListaEnlazada:
    def __init__(self):
        self.prim = None

    def append(self, dato):
        nuevo = _Nodo(dato, None)
        if self.prim is None:
            self.prim = nuevo
        else:
            act = self.prim
            while act.prox != None:
                act = act.prox
            act.prox = nuevo
    
    def __str__(self):
        res = "["
        actual = self.prim
        while actual:
            res += str(actual.dato)
            if actual.prox != None:
                res += ","
            actual = actual.prox
        res += "]"
        return res
    
    def extend(self, otro):
        actual = self.prim
        while actual:
            actual = actual.prox
        actual = otro.prim

    def remove(self, valor):
        actual = self.prim
        anterior = None
        if actual.dato == valor:
            self.prim = actual.prox
            return
        while actual != None:
            if actual.dato == valor:
                anterior.prox = actual.prox
                return
            anterior = actual
            actual = actual.prox
        raise ValueError('El elemento no se encuentra en la lista')
