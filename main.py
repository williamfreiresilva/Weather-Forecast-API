# since Open Weather Map requires longitude and latitude input, you can use geocoding to get that info
# City names and codes: http://bulk.openweathermap.org/sample/city.list.json.gz
# API link: https://openweathermap.org/api/geocoding-api
# create a function that receives city, metric, and your API key.
# API key should be insertid in the function as default
# get your API key at: https://openweathermap.org/api

import requests

def get_weather(city, units='metric', api_key='d1dae41af2003eafdb561323098db3b6'):
  url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}"
  r = requests.get(url)
  content = r.json()
# best way to understand the API is by including a return statment and placing a break point to execute the debugger.
  with open('data.txt', 'a') as file:
    city_name = content['city']['name']
    for item in content['list']:
      file.write(f"{city_name},{item['dt_txt']}, {item['main']['temp']}, {item['weather'][0]['description']}\n")

print(get_weather(city='Brasília'))


