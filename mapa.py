import tkinter as tk
from tkintermapview import TkinterMapView
# import _sqlite3

# Función para cerrar la aplicación
def cerrar_app():
    ventana.destroy()

# Crear ventana
ventana = tk.Tk()
ventana.title("Aplicación con Mapa")

# Crear instancia de TkinterMapView
mapa = TkinterMapView(ventana)
mapa.pack(fill=tk.BOTH, expand=True)

# Botón para cerrar la aplicación
btn_cerrar = tk.Button(ventana, text="Cerrar", command=cerrar_app)
btn_cerrar.pack(pady=10)

# Iniciar bucle de eventos de Tkinter
ventana.mainloop()
