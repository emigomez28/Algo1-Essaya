def es_par(num):
    return num % 2
class _Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox
    
    def __str__(self):
        return f"Nodo({self.dato})"

class ListaEnlazada:
    def __init__(self):
        self.prim = None
        self.cant = 0
    def append(self, dato):
        nuevo = _Nodo(dato, None)
        if self.prim is None:
            self.prim = nuevo
        else:
            act = self.prim
            while act.prox != None:
                act = act.prox
            act.prox = nuevo
        self.cant += 1
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

    def filter(self, funcion):
        resultado = ListaEnlazada()
        actual = self.prim
        actual_resultado = None
        while actual != None:
            if funcion(actual.dato):
                nodo = _Nodo(actual.dato, None)
                if not actual_resultado:
                    resultado.prim = nodo
                else:
                    actual_resultado.prox = nodo
                actual_resultado = nodo
            actual = actual.prox
        return resultado

    def map(self, funcion):
        resultado = ListaEnlazada()
        actual = self.prim
        actual_resultado = None
        while actual != None:
            valor = funcion(actual.dato)
            nodo = _Nodo(valor)
            if not actual_resultado:
                resultado.prim = nodo
            else:
                actual_resultado.prox = nodo
            actual_resultado = nodo
            actual = actual.prox
        return resultado
    
    def rotar(self, N):
        if not self.prim or not self.prim.prox:
            return
        N = N % self.cant
        if N == 0:
            return
        
        ant = None
        act = None
        ult = self.prim
        for i in range(self.cant - 1):        
            if i == N - 1:
                ant = ult
                act = ant.prox
            ult = ult.prox

        ant.prox = None
        ult.prox = self.prim
        self.prim = act

def main():
    le = ListaEnlazada()
    le.append(1)
    le.append(2)
    le.append(3)
    le.append(4)
    le.append(5)
    le.append(6)
    print(le)
    le.rotar(3)
    print(le)

main()