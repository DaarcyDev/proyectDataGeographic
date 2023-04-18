import tkinter as tk
import customtkinter
from tkintermapview import TkinterMapView
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import requests

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

root = customtkinter.CTk()  # create CTk window like you do with the Tk window
root.geometry("1350x700")

#frames
frame1 = customtkinter.CTkFrame(root, width = 400, height=650)
frame1.grid(row=0, column=0, sticky="ew", padx=(30,0), pady=40)

frame2 = customtkinter.CTkFrame(root, width = 900, height=650)
frame2.grid(row=0, column=1, sticky="ew", padx=(30,30), pady=40)

dataFrame = customtkinter.CTkFrame(frame1,width=300,height=280)
dataFrame.grid(row=0,column=0, padx=(30,30), pady=(30,0))
dataFrame.grid_propagate(False)
dataFrame.grid_rowconfigure(0, weight=1)
dataFrame.grid_columnconfigure(0, weight=1)


graphicFrame = customtkinter.CTkFrame(frame1,width=300,height=280)
graphicFrame.grid(row=1,column=0, padx=(30,30), pady=(30,30))
graphicFrame.grid_propagate(False)

searchFrame = customtkinter.CTkFrame(frame2,width=850,height=100)
searchFrame.grid(row=0,column=0, padx=(30,30), pady=(30,0))
searchFrame.grid_propagate(False)

mapFrame = customtkinter.CTkFrame(frame2,width=850,height=450)
mapFrame.grid(row=1,column=0, padx=(30,30), pady=(30,30))
mapFrame.grid_propagate(False)
mapFrame.grid_rowconfigure(0, weight=1)
mapFrame.grid_columnconfigure(0, weight=1)

customFontLabel = ("Helvetica", 20)
customFontEntry = ("Helvetica", 18)

entry = customtkinter.CTkEntry(searchFrame, placeholder_text="Type Address", width=700,height=50, font=customFontEntry)
entry.grid(row=0, column=1, padx=(20, 0), pady=(20, 20), sticky="nsew")

mapa = TkinterMapView(mapFrame, width=800, height=350)
mapa.grid(   sticky="nsew")
mapa.set_address("Mexico")


# Configura los parámetros de la API
url = 'https://api.openweathermap.org/data/2.5/weather'
ciudad = 'Mexico'  # Cambia esto por la ciudad que deseas obtener el pronóstico
clave_api = '814f3db12a3dd435f4d9cee7679e6c58'  # Reemplaza con tu clave de API de OpenWeatherMap

# Realiza la solicitud a la API
params = {
    'q': ciudad,
    'appid': clave_api,
    'units': 'metric'  # Cambia a 'imperial' si deseas obtener los datos en unidades imperiales
}

ciudad = entry.get()
urlRest = f"https://restcountries.com/v3.1/name/mexico"
response = requests.get(urlRest)
datos_pais = response.json()
poblacion = datos_pais[0]["population"]

ciudades = ["Mexico"]
poblaciones = [poblacion]

response = requests.get(url, params=params)
data = response.json()

label_text = tk.StringVar()
label_text.set(f'El clima en {data["name"]}, \n\n-Temperatura actual: {data["main"]["temp"]}°C\n\n-Humedad: {data["main"]["humidity"]}%\n\n-Presión atmosférica: {data["main"]["pressure"]} hPa\n\n-Velocidad del viento: {data["wind"]["speed"]} m/s\n\n-Dirección del viento: {data["wind"]["deg"]}°')


def actualizar_grafica():
    ax.clear()
    ax.bar(ciudades, poblaciones)
    canvas.draw()
    print(poblaciones, ciudades)


def asignar_ciudad(ciudad):
    global ciudades, poblaciones
    mapa.set_address(entry.get())
    params = {
        'q': ciudad,
        'appid': clave_api,
        'units': 'metric'  # Cambia a 'imperial' si deseas obtener los datos en unidades imperiales
    }
    response = requests.get(url, params=params)
    data = response.json()
    ciudad = entry.get()
    urlRest = f"https://restcountries.com/v3.1/name/{entry.get()}"
    response = requests.get(urlRest)
    datos_pais = response.json()
    poblacion = datos_pais[0]["population"]
    if ciudad:
        label_text.set(f'El clima en {data["name"]}, \n\n-Temperatura actual: {data["main"]["temp"]}°C\n\n-Humedad: {data["main"]["humidity"]}%\n\n-Presión atmosférica: {data["main"]["pressure"]} hPa\n\n-Velocidad del viento: {data["wind"]["speed"]} m/s\n\n-Dirección del viento: {data["wind"]["deg"]}°')    
        ciudades.append(ciudad)
        poblacion = datos_pais[0]["population"]
        poblaciones.append(poblacion)
        print(ciudad, poblacion)
        if len(poblaciones) >= 5:
            poblaciones.pop(0)
            ciudades.pop(0) 
        actualizar_grafica()


dataLabel = customtkinter.CTkLabel(dataFrame, textvariable=label_text, font=customFontLabel)
dataLabel.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

fig = Figure(figsize=(3, 3), dpi=100)
ax = fig.add_subplot(111)
ax.bar(ciudades, poblaciones)

# Crear un lienzo de Matplotlib para tkinter
canvas = FigureCanvasTkAgg(fig, graphicFrame)
canvas.draw()
canvas.get_tk_widget().pack()

button_5 = customtkinter.CTkButton(searchFrame,text="Search",width=90,height=40,command=lambda:asignar_ciudad(entry.get()))
button_5.grid(row=0, column=2, sticky="e", padx=15)

root.mainloop()