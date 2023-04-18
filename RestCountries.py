import requests

# Reemplazar con tu propia clave de API


# URL base de la API de REST Countries
BASE_URL = "https://restcountries.com/v3.1"

# Nombre del país del cual deseas obtener información
nombre_pais = "Estados Unidos"

# Hacer la solicitud a la API
response = requests.get(f"{BASE_URL}/name/{nombre_pais}")

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Obtener los datos en formato JSON
    datos_pais = response.json()
    
    # Procesar los datos y obtener la información demográfica específica
    poblacion = datos_pais[0]["population"]
    area = datos_pais[0]["area"]
    capital = datos_pais[0]["capital"]
    idiomas = datos_pais[0]["languages"]
    
    # Imprimir la información demográfica del país
    print(f"País: {nombre_pais}")
    print(f"Población: {poblacion}")
    print(f"Área: {area}")
    print(f"Capital: {capital}")
    print(f"Idiomas: {idiomas}")
else:
    print("Error en la solicitud:", response.status_code)
