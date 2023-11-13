import tkinter as tk
from tkinter import ttk
import serial
import threading
import time

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Valores de Giroscopio")

        self.label = ttk.Label(root, text="Valores del Giroscopio:")
        self.label.pack(pady=10)

        self.x_label = ttk.Label(root, text="Eje X: ")
        self.x_label.pack()

        self.y_label = ttk.Label(root, text="Eje Y: ")
        self.y_label.pack()

        self.z_label = ttk.Label(root, text="Eje Z: ")
        self.z_label.pack()

        self.serial_port = serial.Serial('COM3', 9600, timeout=1)  # Ajusta el nombre del puerto COM según tu configuración
        if not self.serial_port:
            print("--- Error en la conexión ---")
            return

        # Iniciar un hilo para la lectura del puerto serial
        self.thread = threading.Thread(target=self.read_data)
        self.thread.start()

    def read_data(self):
        while True:
            try:
                # Leer una línea de datos desde el puerto serial
                line = self.serial_port.readline().decode('utf-8').strip()

                # Verificar si la línea no está vacía antes de procesar
                if line:
                    # Dividir la línea en valores para cada eje
                    values = line.split(',')

                    # Verificar si hay suficientes valores
                    if len(values) == 3:
                        x, y, z = map(int, values)

                        # Actualizar las etiquetas con los valores
                        self.x_label.config(text=f"Eje X: {x}")
                        self.y_label.config(text=f"Eje Y: {y}")
                        self.z_label.config(text=f"Eje Z: {z}")

            except Exception as e:
                print(f"Error: {type(e).__name__} - {e}")

            # Esperar un breve momento antes de la próxima lectura
            time.sleep(0.1)

if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()
