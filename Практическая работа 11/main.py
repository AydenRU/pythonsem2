import urllib.request
import re
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
city_find = input('Введите город :')
data = urllib.request.urlopen(f"https://api.openweathermap.org/data/2.5/weather?q={city_find}&units=metric&lang=ru&appid=c341e34f9b7c327502cde34aa7817c5f").read().decode()
print(data)
city_pattern = r'(?:name":")([^"]+)'
temp_pattern = r'(?:temp":)([^.]+)'
desc_pattern = r'(?:description":")([^"]+)'
humid_pattern = r'(?:humidity":)([^,}]+)'
speed_pattern = r'(?:speed":)([^,]+)'
pressure_pattern = r'(?:pressure":)([^,]+)'

city = re.findall(city_pattern, data)
temp = re.findall(temp_pattern, data)
desc = re.findall(desc_pattern, data)
humid = re.findall(humid_pattern, data)
speed = re.findall(speed_pattern, data)
pressure = re.findall(pressure_pattern, data)

print(f'[{current_time}] Запрос погоды в горде: {city}\n'
      f'Температура: {temp} °C, {desc}\n'
      f'Влажность воздуха: {humid}%\n'
      f'Скорость ветра: {speed} м/с\n'
      f'Атмосферное давление: {pressure}ммм рт.ст.')

#{"coord":{"lon":37.6156,"lat":55.7522},"weather":[{"id":803,"main":"Clouds","description":"облачно с прояснениями","icon":"04d"}],
# "base":"stations","main":{"temp":13.57,"feels_like":12.18,"temp_min":12.53,"temp_max":14.24,"pressure":1014,"humidity":46,"sea_level":1014,"grnd_level":997},
# "visibility":10000,"wind":{"speed":3.63,"deg":296,"gust":4.67},"clouds":{"all":77},"dt":1696249784,"sys":{"type":2,"id":2000314,"country":"RU","sunrise":1696217588,
# "sunset":1696259088},"timezone":10800,"id":524901,"name":"Москва","cod":200}