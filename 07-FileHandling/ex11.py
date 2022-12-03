film_titles = ["Dune", "LOTR", "Batman", "Avatar", "Avengers"]
f = open('films.txt', 'w')
for item in film_titles:
    f.writelines([item, "\n"])

f.close()