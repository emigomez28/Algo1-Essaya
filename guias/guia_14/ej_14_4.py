class _Nodo:
    def __init__(self, dato, prox = None):
        self.dato = dato
        self.prox = prox

class Pila:
    def __init__(self):
        self.tope = None
    def apilar(self, valor):
        nuevo = _Nodo(valor, self.tope)
        self.tope = nuevo
    
    def desapilar(self):
        if self.esta_vacia():
            raise ValueError('No se puede desapilar una pila vacia')
        dato = self.tope.dato
        self.tope = self.tope.prox
        return dato
            
    def esta_vacia(self):
        return self.tope == None 
    def ver_tope(self):
        if self.esta_vacia():
            raise ValueError("pila vacía")
        return self.tope.dato
class SolitarioSpiderException(Exception):
    pass
class Carta:
    def __init__(self, palo, valor):
        self.palo = str(palo)
        self.valor = int(valor)
class Solitario:
    def __init__(self):
        self.pila_de_cartas = Pila()
    def apilar_carta(self, carta):
        if self.pila_de_cartas.esta_vacia():
            self.pila_de_cartas.apilar(carta)
        else:
            ultima_carta = self.pila_de_cartas.ver_tope()
            if ultima_carta.valor == carta.valor + 1 and ultima_carta.palo != carta.palo:
                self.pila_de_cartas.apilar(carta)
            else:
                raise SolitarioSpiderException("No se puede apilar esa carta")