class Intervalo():
    def __init__(self, desde, hasta):
        self.desde = int(desde)
        self.hasta = int(hasta)
    
    def duracion(self, desde, hasta):
        return (self.desde + self.hasta)/60
         
