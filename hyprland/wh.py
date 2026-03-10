#!/usr/bin/env python

import json
import requests

WEATHER_CODES = {
    0: '☀️ ',
    1: '⛅ ',
    2: '⛅ ',
    3: '☁️ ',
    45: '☁️ ',
    48: '🌧️',
    51: '🌧️',
    53: '🌧️',
    55: '🌧️',
    61: '🌧️',
    63: '🌧️',
    65: '🌧️',
    80: '🌧️',
    81: '🌧️',
    82: '🌧️',
}


weather = requests.get("https://api.open-meteo.com/v1/forecast?latitude=43.60&longitude=39.73&current_weather=true").json()

data = {}
weather_condition = '🌅'
if weather['current_weather']['weathercode'] in WEATHER_CODES:
	weather_condition = weather['current_weather']['weathercode']

if(weather):
	data["text"] = f"Sochi {WEATHER_CODES[weather_condition]} {weather['current_weather']['temperature']}C°"

print(json.dumps(data))
