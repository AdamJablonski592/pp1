import json

movie = {
    "name":"Dune",
    "year": 2020,
    "director": "Denis Villenvue",
    "in_cinema": False,
    "money_earned": 300000000
}

with open('favourite.json', 'w') as f:
    json.dump(movie, f, indent=4)

