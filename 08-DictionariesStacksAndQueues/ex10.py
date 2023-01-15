countries = [
    {"name": "Poland", "population": 38000000},
    {"name": "France", "population": 67000000},
    {"name": "Germany", "population": 83000000},
    {"name": "USA", "population": 331000000},
    {"name": "China", "population": 1412000000}
]

i = 0
while i < len(countries):
    print(countries[i]["name"], ":", countries[i]["population"])
    i += 1