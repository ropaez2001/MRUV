import numpy as np
import matplotlib.pyplot as plt

def crear_graficos(v0, a, t):
    tiempo = np.linspace(0, t, 10)
    velocidad = v0 + a * tiempo
    distancia = v0 * tiempo + 0.5 * a * tiempo ** 2
    aceleracion = np.full_like(tiempo, a)

    plt.figure(figsize=(15, 5))

   
    plt.subplot(1, 3, 1)
    plt.plot(tiempo, velocidad)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Velocidad (m/s)')
    plt.grid(True)
    plt.title('Gráfico de Velocidad en funcion del tiempo')
    
    plt.subplot(1, 3, 2)
    plt.plot(tiempo, distancia)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Distancia (m)')
    plt.grid(True)
    plt.title('Gráfico de Distancia Recorrida en funcion del tiempo')


    plt.subplot(1, 3, 3)
    plt.plot(tiempo, aceleracion)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Aceleración (m/s^2)')
    plt.title('Gráfico de Aceleración en funcion del tiempo')

    plt.tight_layout()
    plt.show()