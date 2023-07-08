class Fraccion():
    def __init__(self, dividendo, divisor):
        self.dividendo = dividendo
        self.divisor = divisor
    
    def __str__(self):
        return f"{self.dividendo}/{self.divisor}"

   # def __add__(self, dividendo, divisor):
        
