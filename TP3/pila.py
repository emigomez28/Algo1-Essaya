class Pila:
    def __init__(self):
        '''
        Inicializa una nueva pila, vacía
        '''
        self.tope = None

    def apilar(self, dato):
        '''
        Agrega un nuevo elemento a la pila
        '''
        nodo = _Nodo(dato, self.tope)
        self.tope = nodo

    def desapilar(self):
        '''
        Desapila el elemento que está en el tope de la pila
        y lo devuelve.
        Pre: la pila NO está vacía.
        Pos: el nuevo tope es el que estaba abajo del tope anterior
        '''
        if self.esta_vacia():
            raise ValueError("pila vacía")
        dato = self.tope.dato
        self.tope = self.tope.prox
        return dato

    def ver_tope(self):
        '''
        Devuelve el elemento que está en el tope de la pila.
        Pre: la pila NO está vacía.
        '''
        if self.esta_vacia():
            raise ValueError("pila vacía")
        return self.tope.dato

    def esta_vacia(self):
        '''
        Devuelve True o False según si la pila está vacía o no
        '''
        return self.tope is None
    
    def __str__(self):
        if self.esta_vacia():
            return f'tope | |'
        else:
            act = self.desapilar()
            pila_aux = Pila()
            res = "tope | "
            while act:
                res += str(act)
                res += " | "
                pila_aux.apilar(act)
                if self.esta_vacia():
                    break
                act = self.desapilar()
            res += "fondo"
            while not pila_aux.esta_vacia():
                dato = pila_aux.desapilar()
                self.apilar(dato)
        return res

class _Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox
