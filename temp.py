import requests


name = "IncePtion"
movie = requests.get("http://www.omdbapi.com/?apikey=93d3f0f7-2b32-4b37-9ec6-2b5dc6714043&t=" + name +"&y=&plot=full&r=json")

all_inf =  movie.json()

print all_inf["imdbRating"]
