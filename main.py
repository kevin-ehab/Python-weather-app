#getting API data:
import requests

#ipinfo.io API:
ip_info = requests.get("https://ipinfo.io/").json()

location = [float(x) for x in ip_info["loc"].split(",")]

#setting up the latitude and longitude
latitude, longitude = location[0], location[1]

#open-meteo API:
weather_info = requests.get("https://api.open-meteo.com/v1/forecast?"
                            rf"latitude={latitude}&longitude={longitude}"
                            "&current_weather=true").json()

current_weather = weather_info["current_weather"]
temperature = current_weather["temperature"]

print(f'{temperature}°C')

#code translator:

weather_state_codes = {
    0: "☀️ Clear sky",
    1: "🌤️ Mainly clear",
    2: "⛅ Partly cloudy",
    3: "☁️ Overcast",
    45: "🌫️ Fog",
    48: "🌫️ Rime fog",
    51: "🌦️ Light drizzle",
    53: "🌦️ Moderate drizzle",
    55: "🌧️ Dense drizzle",
    61: "🌦️ Slight rain",
    63: "🌧️ Moderate rain",
    65: "🌧️ Heavy rain",
    71: "🌨️ Slight snowfall",
    73: "🌨️ Moderate snowfall",
    75: "❄️ Heavy snowfall",
    80: "🌧️ Rain showers",
    81: "🌧️ Moderate rain showers",
    82: "🌧️ Violent rain showers",
    95: "⛈️ Thunderstorm",
    96: "⛈️ Thunderstorm with hail",
}

weather_state = weather_state_codes[current_weather["weathercode"]][3:]
weather_state_emoji = weather_state_codes[current_weather["weathercode"]][0]

print(weather_state)
print(weather_state_emoji)

#html templating:
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("."))
template = env.get_template("template.html")
data = {
    "latitude": latitude,
    "longitude": longitude,
    "weather_state_emoji": weather_state_emoji,
    "temperature": f'{temperature}°C',
    "weather_state": weather_state
}

html = template.render(data)

#interface launch:
import webview

webview.create_window("Weather App", html=html)
webview.start()