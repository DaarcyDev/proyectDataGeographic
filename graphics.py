import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

root = tk.Tk()
root.title("Ejemplo de Matplotlib en Tkinter")
root.geometry("400x300")

# Crear una figura de Matplotlib
fig = Figure(figsize=(4, 3), dpi=100)
ax = fig.add_subplot(111)
datos = [3, 7, 5, 8, 12]
nombres = ["A", "B", "C", "D", "E"]
ax.bar(nombres, datos)

# Crear un lienzo de Matplotlib para tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack()

# Ejecutar el bucle principal de tkinter
root.mainloop()
