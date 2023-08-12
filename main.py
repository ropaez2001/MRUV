import tkinter as tk
from tkinter import messagebox
import calculos
import graficos
from Simulacion import Simulacion


class MRUVA:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("MRUV Calculator")
        self.ventana.geometry("800x400")
        self.ventana.config(bg="lightblue")

        self.crear_interfaz()

    def crear_interfaz(self):
        datos_frame = tk.Frame(self.ventana, bg="lightblue")
        datos_frame.pack(padx=20, pady=20)

        tk.Label(datos_frame, text="Velocidad Inicial (m/s):").grid(row=0, column=0)
        self.v0_var = tk.DoubleVar()
        tk.Entry(datos_frame, textvariable=self.v0_var).grid(row=0, column=1)
        

        tk.Label(datos_frame, text="Aceleración (m/s^2):").grid(row=1, column=0)
        self.a_var = tk.DoubleVar()
        tk.Entry(datos_frame, textvariable=self.a_var).grid(row=1, column=1)

        tk.Label(datos_frame, text="Tiempo (s):").grid(row=2, column=0)
        self.t_var = tk.DoubleVar()
        tk.Entry(datos_frame, textvariable=self.t_var).grid(row=2, column=1)

        calcular_button = tk.Button(self.ventana, text="Calcular", command=self.calcular_mr_uv, bg="green")
        calcular_button.pack(pady=20)

        self.resultados_label = tk.Label(self.ventana, text="", bg="lightblue")
        self.resultados_label.pack()
    def calcular_mr_uv(self):
    
        v0 = self.v0_var.get()
        a = self.a_var.get()
        t = self.t_var.get()    



        if v0 < 0 or t < 0:
         
          messagebox.showerror("Error", "La velocidad inicial y el tiempo deben ser no valores positivos.")
          return

        mruv = calculos.MRUV(v0, a, t)
        distancia = mruv.calcular_distancia_recorrida()
        velocidad_final = mruv.calcular_velocidad_final()
        self.resultados_label.config(text=f"Distancia recorrida: {distancia:.2f} metros\nVelocidad final: {velocidad_final:.2f} m/s")

        graficos.crear_graficos(v0, a, t)
        simulacion = Simulacion(v0, a, t)
        simulacion.iniciar_simulacion() 
       
if __name__ == "__main__":
    ventana= tk.Tk()             
    app = MRUVA(ventana) 
    ventana.mainloop()

       