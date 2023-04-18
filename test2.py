import tkinter as tk

import customtkinter
from tkintermapview import TkinterMapView
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import requests

root = tk.Tk()
root.title("Ejemplo de Matplotlib en Tkinter")
root.geometry("800x600")

frame2 = customtkinter.CTkFrame(root, width = 400, height=250)
frame2.grid(row=0, column=1, sticky="ew", padx=(30,30), pady=40)


searchFrame = customtkinter.CTkFrame(frame2,width=300,height=100)
searchFrame.grid(row=0,column=0, padx=(30,30), pady=(30,0))
searchFrame.grid_propagate(False)

graphicFrame = customtkinter.CTkFrame(frame2,width=300,height=280)
graphicFrame.grid(row=1,column=0, padx=(30,30), pady=(30,30))
graphicFrame.grid_propagate(False)


entry = customtkinter.CTkEntry(searchFrame, placeholder_text="Type Address", width=150,height=50)
entry.grid(row=0, column=1, padx=(20, 0), pady=(20, 20), sticky="nsew")

ciudad="mexico"

poblacion1=0
poblacion2=0
poblacion3=0
poblacion4=0

def asignar_ciudad(ciudad):

    if ciudad:
        if(poblacion1 == 0):
            poblacion1 = ciudad
        elif(poblacion2 == 0):
            poblacion2 = ciudad
        elif(poblacion3 == 0):
            poblacion3 = ciudad
        elif(poblacion4 == 0):
            poblacion4 = ciudad





# urlRest = f"https://restcountries.com/v3.1/name/{ciudad}"
# response = requests.get(urlRest)
# datos_pais = response.json()
# poblacion = datos_pais[0]["population"]




fig = Figure(figsize=(4, 3), dpi=100)
ax = fig.add_subplot(111)
datos = [poblacion1,poblacion2, poblacion3, poblacion4]
nombres = ["p1","p2","p3","p4"]
ax.bar(nombres, datos)

# Crear un lienzo de Matplotlib para tkinter
canvas = FigureCanvasTkAgg(fig, graphicFrame)
canvas.draw()
canvas.get_tk_widget().pack()
button_5 = customtkinter.CTkButton(searchFrame,text="Search",width=90,height=40,command=lambda:asignar_ciudad(entry.get()))
button_5.grid(row=0, column=2, sticky="e", padx=15)


# Ejecutar el bucle principal de tkinter
root.mainloop()
