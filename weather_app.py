import requests, json

api_key = "416941b8dfc144c9984ba1ea09520439"
city_name = ""
def get_weather(city_name, api_key):
    print("Welcome to Simple Weather App!")
    city_name = input("Enter city name: ")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        print(f"Weather in {city_name}:")
        print(f"- Temperature: {data['main']['temp']} °C")
        print(f"- Condition: {data['weather'][0]['main']}")
    else:
        print("No data available")

get_weather(city_name, api_key)
