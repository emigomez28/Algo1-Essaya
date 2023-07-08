class _Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

class PilaConMaximo:
    def __init__(self):
        self.tope = None
        self.max = 0
    def apilar(self, valor):
        nodo = _Nodo(valor)
        if nodo.dato > self.max:
            self.max = nodo.dato
        self.tope = nodo
    
    def desapilar(self):
        if self.tope == None:
            return
        valor = self.tope.dato
        self.tope = self.tope.prox
        return valor
    def obtener_maximo(self):
        return self.max