import requests
word_selection = input("Enter word: \n").lower()
url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word_selection}"
answer = requests.get(url)
if answer.status_code == 200:
    word_info = answer.json()
    definition = word_info[0]['meanings'][0]['definitions'][0]['definition']
    print(f"Definition: {definition}")
else:
     print(f"Failed to find word. Error code: {answer.status_code}")
