import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
import pygame


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

class MRUVApp:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("MRUV Calculator")
        self.ventana.geometry("400x350")
        self.ventana.config(bg="lightblue")

        self.v0_label = tk.Label(self.ventana, text="Velocidad Inicial (m/s):", bg="white")
        self.v0_label.pack()
        self.v0_entry = tk.Entry(self.ventana)
        self.v0_entry.pack()

        self.a_label = tk.Label(self.ventana, text="Aceleración (m/s^2):", bg="yellow")
        self.a_label.pack()
        self.a_entry = tk.Entry(self.ventana)
        self.a_entry.pack()

        self.t_label = tk.Label(self.ventana, text="Tiempo (s):", bg="pink")
        self.t_label.pack()
        self.t_entry = tk.Entry(self.ventana)
        self.t_entry.pack()

        self.calcular_btn = tk.Button(self.ventana, text="Calcular", command=self.calcular_mruv, bg="orange")
        self.calcular_btn.pack()

        self.resultados_label = tk.Label(self.ventana, text="", bg="white")
        self.resultados_label.pack()
        

    def calcular_mruv(self):
        try:
            v0 = float(self.v0_entry.get())
            a = float(self.a_entry.get())
            t = float(self.t_entry.get())

            if v0 < 0 or t < 0:
                messagebox.showerror("Error", "La velocidad inicial y el tiempo no pueden ser negativos.")
                return

            mruv = MRUV(v0, a, t)
            distancia = mruv.calcular_distancia_recorrida()
            velocidad_final = mruv.calcular_velocidad_final()

            resultado_texto = f"Distancia Recorrida: {distancia:.2f} metros\nVelocidad Final: {velocidad_final:.2f} m/s"
            self.resultados_label.config(text=resultado_texto)
            self.resultados_label.config(font=("Helvetica", 16, "bold"), fg="blue")

            self.crear_graficos(v0, a, t)
            simulacion = Simulacion(v0, a, t)
            simulacion.iniciar_simulacion()

        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos.")
    def crear_graficos(self, v0, a, t):
        tiempo = np.linspace(0, t, 100)
        distancia = v0 * tiempo + 0.5 * a * tiempo ** 2
        velocidad = v0 + a * tiempo
        aceleracion = np.full_like(tiempo, a)

        plt.figure(figsize=(15, 5))

        plt.subplot(1, 3, 1)
        plt.plot(tiempo, distancia)
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Distancia (m)')
        plt.grid(True)
        plt.title('Distancia Recorrida en función del tiempo')

        plt.subplot(1, 3, 2)
        plt.plot(tiempo, velocidad)
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Velocidad (m/s)')
        plt.grid(True)
        plt.title('Velocidad en función del tiempo')

        plt.subplot(1, 3, 3)
        plt.plot(tiempo, aceleracion)
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Aceleración (m/s^2)')
        plt.title('Aceleración en función del tiempo')

        plt.tight_layout()
        plt.show()        
            
class Simulacion:
    def __init__(self, v0, a, t):
        self.v0 = v0
        self.a = a
        self.t = t
        self.posicion = 0
        self.velocidad = v0
        self.tiempo = 0
        self.pausado = False

    def iniciar_simulacion(self):
        pygame.init()

        pantalla_ancho = 800
        pantalla_alto = 600
        pantalla = pygame.display.set_mode((pantalla_ancho, pantalla_alto))
        pygame.display.set_caption("Simulación MRUV")

        fuente = pygame.font.Font(None, 36)

        reloj = pygame.time.Clock()

        corriendo = True
        while corriendo:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    corriendo = False
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    self.pausado = not self.pausado

            tiempo_transcurrido = reloj.tick(60) / 100

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

            pygame.display.flip()

        pygame.quit()        

    

if __name__ == "__main__":
    ventana_principal = tk.Tk()             
    app = MRUVApp(ventana_principal) 
    ventana_principal.mainloop()
    
    
    
    
    