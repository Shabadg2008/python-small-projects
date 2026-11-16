import requests
print("Movie Finder")
print()
movie = input("What movie are you looking for? \n").capitalize()
api = "b6bebf4ade9bd9983923f24d017d0b5d"
url = "https://api.themoviedb.org/3/search/movie"
params = {
    "query": movie,
    "api_key": api
}
response = requests.get(url, params = params)
if response.status_code == 200:
    movie_data = response.json()
    info = movie_data['results']
    print(f"Name: {info[0]['title']}")
    print(f"About: {info[0]['overview']}")
    print(f"Release: {info[0]['release_date']}")
    print(f"Rating: {info[0]['vote_average']}")
