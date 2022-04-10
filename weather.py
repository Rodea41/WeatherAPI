from json.tool import main
from urllib import response
import requests
import logins # Must import login.py file so I can access the API credentials

#* API key to access OpenWeatherMap is imported from logins.py file
#* The key is not included directly in main file because it is sensitive data, and should not be committed to public repository.
API_KEY = logins.api_key 

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")

#* Request URL is created by concatenating the base URL with the API key and the city name that the user entered.
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json() # Gets the data within the response object and converts it to a Python dictionary
    weather = data['weather'] # Isolate the info listed within the 'weather' key
    temp = data['main'] # Isolate the info listed within the 'main' key

    description = weather[0]['description'] # Access 1st element of the weather array which is a dictionary, and the accessed the description key
    print(f"The weather description for {city} is : {description}")

    temperature = temp['temp'] 
    temp_fahrenheit = round((int(temperature) - 273.15)*2 + 30, 2) # No need to put an index (like in the 'description' var above) because the temperature is the only key in the 'temp' dictionary
    print(f"The temperature in {city} is currently {temp_fahrenheit} degrees Fahrenheit")



else:
    print("Error: ", response.status_code)