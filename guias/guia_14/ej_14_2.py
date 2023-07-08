

class _Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox
    def __str__(self):
        return f"{self.dato}"

class Cola:
    def __init__(self):
        self.frente = None
    
    def esta_vacia(self):
        '''Devuelve True o False según si la cola está vacía o no'''
        return self.frente is None

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
    
    def largo(self):
        if self.frente is None:
            return 0
        else:
            len = 0
            act = self.frente
            while act:
                act = act.prox
                len += 1
        return len

class Impresora:
    def __init__(self, nombre, cant_max_tinta):
        self.nombre = str(nombre)
        self.tinta_max = float(cant_max_tinta)
        self.tinta_actual = float(cant_max_tinta) 
        self.documentos = Cola()
    
    def encolar(self, nombre_docu):
        self.documentos.encolar(nombre_docu)

    def imprimir(self):
        if self.documentos.esta_vacia():
            print("No hay documentos para imprimir")
        if self.tinta_actual == 0:
            print("No tengo tinta suficiente")
        else:
            impreso = self.documentos.desencolar()
            print(f"{impreso} impreso")
            self.tinta_actual -= 1
    
    def cargar_tinta(self):
        self.tinta_actual = self.tinta_max

class Oficina:
    def __init__(self):
        self.impresoras = dict()
    
    def agregar_impresora(self, impresora):
        self.impresoras[impresora.nombre] = impresora

    def impresora(self, nombre):
        imp = self.impresoras.get(nombre, None)
        return imp
    
    def quitar_impresora(self, nombre):
        sacar = self.impresoras.get(nombre, None)
        if sacar is not None:
            self.impresoras.popitem(sacar)
        else:
            print('No puedo sacar una impresora que no está en la oficina')
    
    def obtener_impresora_libre(self):
        menor = 100000
        for key in self.impresoras.keys():
            impresora_actual = self.impresoras[key]
            if impresora_actual.largo() < menor:
                menor = len(self.impresoras[key])
        return menor
            

    