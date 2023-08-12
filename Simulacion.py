import pygame

class Simulacion:
    def __init__(self, v0, a, t):
        self.v0 = v0
        self.a = a
        self.t = t
        self.posicion = 0
        self.velocidad = v0
        self.aceleracion = a
        self.tiempo = 0
        self.pausado = True

    def iniciar_simulacion(self):
        pygame.init()

        pantalla_ancho = 800
        pantalla_alto = 600
        pantalla = pygame.display.set_mode((pantalla_ancho, pantalla_alto))
        pygame.display.set_caption("Simulación MRUV")

        fuente = pygame.font.Font(None, 46)

        reloj = pygame.time.Clock()

        corriendo = True
        while corriendo:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    corriendo = False
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    self.pausado = not self.pausado

            tiempo_transcurrido = reloj.tick(60)/100 

            if not self.pausado:
                self.tiempo += tiempo_transcurrido
                self.posicion = self.v0 * self.tiempo + 0.5 * self.a * self.tiempo ** 2
                self.velocidad = self.v0 + self.a * self.tiempo
                

            pantalla.fill((255, 255, 255))
            pygame.draw.circle(pantalla, (0, 0, 255), (int(self.posicion), pantalla_alto // 2), 10)

            # Mostrar velocidad, distancia recorrida y tiempo en tiempo real
            velocidad_texto = fuente.render(f"Velocidad: {self.velocidad:.2f} m/s", True, (0, 0, 0))
            pantalla.blit(velocidad_texto, (10, 10))

            distancia_texto = fuente.render(f"Distancia: {self.posicion:.2f} metros", True, (0, 0, 0))
            pantalla.blit(distancia_texto, (10, 50))

            tiempo_texto = fuente.render(f"Tiempo: {self.tiempo:.2f} segundos", True, (0, 0, 0))
            pantalla.blit(tiempo_texto, (10, 90))
            
            aceleracion_texto = fuente.render(f"Aceleración: {self.aceleracion:.2f} m/s²", True, (0, 0, 0))
            pantalla.blit(aceleracion_texto, (10, 130))
            
            
            
            
            
            pygame.display.flip()

        pygame.quit()