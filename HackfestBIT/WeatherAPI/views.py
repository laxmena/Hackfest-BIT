# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import urllib
import json
import requests
import ast

def home(request):
	return render(request, 'WeatherAPI/home.html')
	
# Create your views here.
def weather(request):
	city = request.GET['city']
	url = 'http://api.openweathermap.org/data/2.5/find' 
	
	params = {'q': city, 'appid': 'eb9f4a9ff962b78534f73457352b4093'}
	r = requests.get('http://api.openweathermap.org/data/2.5/find', params=params)
	data = r.json()
	# data = {u'count': 1, u'message': u'accurate', u'list': [{u'clouds': {u'all': 20}, u'name': u'Coimbatore', u'snow': None, u'coord': {u'lat': 11, u'lon': 76.9667}, u'sys': {u'country': u'IN'}, u'weather': [{u'main': u'Clouds', u'id': 801, u'icon': u'02d', u'description': u'few clouds'}], u'rain': None, u'dt': 1504081800, u'main': {u'pressure': 1007, u'temp_min': 305.15, u'temp_max': 305.15, u'temp': 305.15, u'humidity': 59}, u'id': 1273865, u'wind': {u'gust': 9.3, u'speed': 4.1, u'deg': 180}}], u'cod': u'200'} 
	# city = data['list'][0]['name']
	description = data['list'][0]['weather'][0]['description']
	mainWeather = data['list'][0]['weather'][0]['main']
	pressure = data['list'][0]['main']['pressure']
	humidity = data['list'][0]['main']['humidity']
	temp_max = data['list'][0]['main']['temp_max']
	temp_min = data['list'][0]['main']['temp_min']
	temp = data['list'][0]['main']['temp']

	context = {
		'data': data,
		'city': city,
		'description': description,
		'main': mainWeather,
		'pressure': pressure,
		'humidity': humidity,
		'temp': temp,
		'temp_max': temp_max,
		'temp_min': temp_min,
	}
	return render(request, 'WeatherAPI/weather.html',context)

	