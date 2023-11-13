import matplotlib.pyplot as plt
import matplotlib.animation as animation
from serial import Serial

# Configura el puerto serie según tu entorno
ser = Serial('COM3', 9600)

# Número de datos a mostrar en la gráfica
num_data_points = 50
data_x = []
data_y = []

# Creamos una figura y ejes
fig, ax = plt.subplots()
line, = ax.plot([], [])

# Inicialización de la gráfica
def init():
    line.set_data([], [])
    return line,

# Función de actualización de la gráfica
def update(frame):
    try:
        # Lee una línea del puerto serie y divide los datos
        line = ser.readline().decode('utf-8').strip()
        x, y, z = map(int, line.split(','))

        # Actualiza los datos
        data_x.append(x)
        data_y.append(y)

        # Limita la cantidad de datos mostrados
        data_x = data_x[-num_data_points:]
        data_y = data_y[-num_data_points:]

        # Actualiza la gráfica
        line.set_data(data_x, data_y)

        return line,
    except ValueError as e:
        print(f"Error de conversión: {e}")
        return None

# Configuración de la animación
#ani = animation.FuncAnimation(fig, update, init_func=init, blit=True)
#ani = animation.FuncAnimation(fig, update, init_func=init, cache_frame_data=False)
ani = animation.FuncAnimation(fig, update, init_func=init, blit=True, interval=100,cache_frame_data=False)



# Mostrar la gráfica
plt.show()
