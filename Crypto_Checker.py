import requests
crypto_Name = input("Which crypto currency price would you like to check? \n").lower()
api_key = "CG-HzTBG6eH41o5FfPKFVG1i1FX"
url = f"https://api.coingecko.com/api/v3/simple/price?vs_currencies=usd&ids={crypto_Name}&x_cg_demo_api_key={api_key}"
response = requests.get(url)
if response.status_code == 200:
    crypto_data = response.json()
    price = crypto_data[crypto_Name]['usd']
    print(f"The current price of {crypto_Name} is ${price} USD")
else:
    print(f"Failed to access data: Error code: {response.status_code}")