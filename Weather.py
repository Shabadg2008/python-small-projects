import requests
city = input("What city or location would you like to know about? \n")
api_key = "663d21a6edbf098f1903cfbf7c2991ce"
base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"
response = requests.get(base_url)
if response.status_code == 200:
    city_data = response.json()
    print(f"Current Temperature: {city_data['main']['temp']}F")
    print(f"Feels Like: {city_data['main']['feels_like']}F")
    print(f"Todays Low: {city_data['main']['temp_min']}F")
    print(f"Todays Max: {city_data['main']['temp_max']}F")
    print(f"Wind Speed: {city_data['wind']['speed']} mph")
else:
    print(f"Failed to access data: Error Code {response.status_code}")