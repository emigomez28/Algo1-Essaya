class _Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox
    def __str__(self):
        return f"{self.dato}"
class Cola:
    '''Representa a una cola, con operaciones de encolar y 
       desencolar. El primero en ser encolado es también el primero
       en ser desencolado.'''

    def __init__(self):
        '''Crea una cola vacía'''
        self.frente = None
        self.ultimo = None

    def encolar(self, dato):
        '''Agrega el elemento x como último de la cola.'''
        nodo = _Nodo(dato)
        if self.esta_vacia():
            self.frente = nodo
        else:
            self.ultimo.prox = nodo
        self.ultimo = nodo

    def desencolar(self):
        '''Desencola el primer elemento y devuelve su valor
           Pre: la cola NO está vacía.
           Pos: el nuevo frente es el que estaba siguiente al frente anterior'''
        if self.esta_vacia():
            raise ValueError("Cola vacía")
        dato = self.frente.dato
        self.frente = self.frente.prox
        if self.frente is None:
            self.ultimo = None
        return dato

    def ver_frente(self):
        '''Devuelve el elemento que está en el frente de la cola.
           Pre: la cola NO está vacía.'''
        if self.esta_vacia():
            raise ValueError("Cola vacía")
        return self.frente.dato

    def esta_vacia(self):
        '''Devuelve True o False según si la cola está vacía o no'''
        return self.frente is None
    
    def __str__(self):
        res = ""
        if self.frente == None:
            return
        else:
            actual = self.frente
            while actual != None:
                res += str(actual)
                if actual.prox != None:
                    res += ", "
                actual = actual.prox
        return res
class TorreDeControl:
    def __init__(self):
        self.arribos = Cola()
        self.partida = Cola()

    def nuevo_arribo(self, avion):
        self.arribos.encolar(avion)

    def nueva_partida(self, avion):
        self.partida.encolar(avion)
    
    def ver_estado(self):
        arribos = f"Vuelos esperando para aterrizar: {self.arribos}"
        partida = f"Vuelos esperando para despegar: {self.partida}"
        print(arribos)
        print(partida)

    def asignar_pista(self):
        if not self.arribos.esta_vacia():
            arribo_asignado = self.arribos.desencolar()
            return f"El vuelo {arribo_asignado} aterrizó con éxito"
        if not self.partida.esta_vacia():
            partida_asignada = self.partida.desencolar()
            return f"El vuelo {partida_asignada} despegó con éxito"
        else:
            print("No hay vuelos en espera")
