

class MRUV:
    def __init__(self, v0, a, t):
        self.v0 = v0
        self.a = a
        self.t = t

    def calcular_distancia_recorrida(self):
        distancia = self.v0 * self.t + 0.5 * self.a * self.t ** 2
        return distancia

    def calcular_velocidad_final(self):
        velocidad_final = self.v0 + self.a * self.t
        return velocidad_final
    
    



