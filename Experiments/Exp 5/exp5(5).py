n = int(input("Enter number of movies: "))
movies = {}

for i in range(n):
    name = input("Movie name: ")
    year = int(input("Year: "))
    director = input("Director: ")
    cost = float(input("Production cost: "))
    collection = float(input("Collection: "))

    movies[name] = {
        "year": year,
        "director": director,
        "cost": cost,
        "collection": collection
    }

print("\nAll movie details:")
for m in movies:
    print(m, movies[m])

print("\nMovies before 2015:")
for m in movies:
    if movies[m]["year"] < 2015:
        print(m)

print("\nMovies with profit:")
for m in movies:
    if movies[m]["collection"] > movies[m]["cost"]:
        print(m)

dname = input("\nEnter director name: ")
print("Movies by director:")
for m in movies:
    if movies[m]["director"] == dname:
        print(m)