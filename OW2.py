import requests

# Especifica la URL base de la API de OpenWeatherMap
url = 'https://api.openweathermap.org/data/2.5/onecall/timemachine'

# Especifica los parámetros de la solicitud, incluyendo la ubicación geográfica, la fecha y tu clave de API
params = {
    'q': "Mexico",
    'dt': 1649998800,  # Reemplaza con el timestamp del día anterior en formato UNIX (ejemplo: 1649998800 para el 13 de abril de 2023)
    'appid': "814f3db12a3dd435f4d9cee7679e6c58",  # Reemplaza con tu clave de API de OpenWeatherMap
}

# Hacer la solicitud a la API
response = requests.get(url, params=params)

# Verificar el código de respuesta de la solicitud
if response.status_code == 200:
    # Procesar los datos de respuesta (en formato JSON)
    datos_clima = response.json()
    # Acceder a los datos del clima del día anterior desde la respuesta
    datos_del_dia_anterior = datos_clima['hourly']
    # Procesar los datos como desees (por ejemplo, extraer la temperatura, la precipitación, etc.)
else:
    print('Error en la solicitud: ', response.status_code)
