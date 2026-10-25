import requests
import time

url = "https://official-joke-api.appspot.com/random_joke"
response = requests.get(url)
if response.status_code == 200:
    joke = response.json()
    print(f"{joke['setup']}")
    time.sleep(2.5)
    print(f"{joke['punchline']}")