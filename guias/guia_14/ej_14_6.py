class _Nodo:
    def __init__(self, valor, prox = None):
        self.valor = valor
        self.prox = prox
class Pila:
    def __init__(self):
        self.tope = None

    def apilar(self, dato):
        nodo = _Nodo(dato, self.tope)
        self.tope = nodo
    
    def desapilar(self):
        if self.esta_vacia():
            return
        dato = self.tope.valor
        self.tope = self.tope.prox
        return dato

    def esta_vacia(self):
        return self.tope is None

def bien_balanceado(cadena):
    pila_parentesis = Pila()
    pila_corchetes = Pila()
    pila_llaves = Pila()
    for c in cadena:
        if c == "(":
            pila_parentesis.apilar(c)
        if c == ")":
            if pila_parentesis.esta_vacia():
                return False
            pila_parentesis.desapilar()
        if c == "[":
            pila_corchetes.apilar(c)
        if c == "]":
            if pila_corchetes.esta_vacia():
                return False
            pila_corchetes.desapilar()
        if c == "{":
            pila_llaves.apilar(c)
        if c == "}":
            if pila_llaves.esta_vacia():
                return False
            pila_llaves.desapilar()
    return pila_llaves.esta_vacia() and pila_corchetes.esta_vacia() and pila_parentesis.esta_vacia()

print(bien_balanceado('(x+y)/2')) #True
print(bien_balanceado('[8*4(x+y)]+{2/5}')) #True
print(bien_balanceado('(x+y]/2')) #False
print(bien_balanceado('1+)2(+3')) #False
        