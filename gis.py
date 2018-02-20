# Импорт модуля для работы с API сайта погоды
# -*- coding: utf-8 -*-

import pyowm

owm = pyowm.OWM('f264aeb8ca0f3f986f6ab19c7b7c0184')

print ("Консольный Гисметео")
def gis():
	city = input("Город: ")
	observation = owm.weather_at_place(city)
	w = observation.get_weather()
	time = w.get_reference_time(timeformat='iso')
	print(time)
	rain = w.get_rain()
	print("Осадки", str(rain))
	status = w.get_detailed_status()
	print ("Небо: ",str(status))
	wind = w.get_wind()['speed']                 # {'speed': 4.6, 'deg': 330}
	print ("Скорость ветра: ", str(wind), 'м/с')
	t = w.get_temperature('celsius')['temp']  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
	print("Температура: ",str(t), 'градусов')
	sunrise = w.get_sunrise_time('iso')
	print("Восход:", sunrise)
	sunset = w.get_sunset_time('iso')
	print("Закат:",sunset) 

choice = "y"
 
while choice.lower() == "y":
	gis()
	choice = input("Для продолжения нажмите Y, а для выхода любую другую клавишу: ")
print("Работа программы завешена")
