import tkinter as tk
import customtkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import requests

root = tk.Tk()
root.title("Ejemplo de Matplotlib en Tkinter")
root.geometry("800x600")

frame2 = customtkinter.CTkFrame(root, width=400, height=250)
frame2.grid(row=0, column=1, sticky="ew", padx=(30,30), pady=40)

searchFrame = customtkinter.CTkFrame(frame2, width=300, height=100)
searchFrame.grid(row=0, column=0, padx=(30,30), pady=(30,0))
searchFrame.grid_propagate(False)

graphicFrame = customtkinter.CTkFrame(frame2, width=300, height=280)
graphicFrame.grid(row=1, column=0, padx=(30,30), pady=(30,30))
graphicFrame.grid_propagate(False)

entry = customtkinter.CTkEntry(searchFrame, placeholder_text="Type Address", width=150, height=50)
entry.grid(row=0, column=1, padx=(20, 0), pady=(20, 20), sticky="nsew")

ciudades = []
poblaciones = []

def actualizar_grafica():
    ax.clear()
    ax.bar(ciudades, poblaciones)
    canvas.draw()
    print(poblaciones, ciudades)

def asignar_ciudad():
    global ciudades, poblaciones
    ciudad = entry.get()
    urlRest = f"https://restcountries.com/v3.1/name/{entry.get()}"
    response = requests.get(urlRest)
    datos_pais = response.json()
    poblacion = datos_pais[0]["population"]

    if ciudad:
        ciudades.append(ciudad)
        poblacion = datos_pais[0]["population"]
        poblaciones.append(poblacion)
        if len(poblaciones) >= 4:
            poblaciones.pop(0)
            ciudades.pop(0)  # Eliminar el primer valor de ciudades también
        actualizar_grafica()

print(poblaciones, ciudades)

fig = Figure(figsize=(4, 3), dpi=100)
ax = fig.add_subplot(111)
ax.bar(ciudades, poblaciones)

# Crear un lienzo de Matplotlib para tkinter
canvas = FigureCanvasTkAgg(fig, graphicFrame)
canvas.draw()
canvas.get_tk_widget().pack()

button_5 = customtkinter.CTkButton(searchFrame, text="Search", width=90, height=40, command=asignar_ciudad)
button_5.grid(row=0, column=2, sticky="e", padx=15)

# Ejecutar el bucle principal de tkinter
root.mainloop()
