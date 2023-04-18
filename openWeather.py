import requests

# Configura los parámetros de la API
url = 'https://api.openweathermap.org/data/2.5/weather'
ciudad = 'Lima,pe'  # Cambia esto por la ciudad que deseas obtener el pronóstico
clave_api = '814f3db12a3dd435f4d9cee7679e6c58'  # Reemplaza con tu clave de API de OpenWeatherMap

# Realiza la solicitud a la API
params = {
    'q': ciudad,
    'appid': clave_api,
    'units': 'metric'  # Cambia a 'imperial' si deseas obtener los datos en unidades imperiales
}
response = requests.get(url, params=params)
data = response.json()

# Procesa los datos de respuesta
if response.status_code == 200:
    # Los datos se obtuvieron exitosamente
    print(f'El clima en {data["name"]}, {data["sys"]["country"]} es {data["weather"][0]["description"]}.')
    print(f'Temperatura actual: {data["main"]["temp"]}°C')
    print(f'Humedad: {data["main"]["humidity"]}%')
    print(f'Presión atmosférica: {data["main"]["pressure"]} hPa')
    print(f'Temperatura mínima: {data["main"]["temp_min"]}°C')
    print(f'Temperatura máxima: {data["main"]["temp_max"]}°C')
    print(f'Velocidad del viento: {data["wind"]["speed"]} m/s')
    print(f'Dirección del viento: {data["wind"]["deg"]}°')
    print(f'Visibilidad: {data["visibility"]} metros')
    print(f'Nubosidad: {data["clouds"]["all"]}%')
    print(f'Hora de la salida del sol: {data["sys"]["sunrise"]}')
    print(f'Hora de la puesta del sol: {data["sys"]["sunset"]}')
else:
    # Hubo un error al obtener los datos
    print('Error al obtener el pronóstico del clima:', data["message"])
