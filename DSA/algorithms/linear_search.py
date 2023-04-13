# Linear Searching

# Sequential search:
# Loop to a list
# Check element by element until match
# Going one by one until find what we're looking for

# Best Case O(1), Worst case O(n)

from performance import timer

beasts = ["Centaur", "Godzilla", "Mozura", "Minotaur", "Hydra", "Nessie"]

beast_to_find = "Nessie"


# Looping
with timer("linear Algorithm with looping"):
    for index, beast in enumerate(beasts):
        if beast == beast_to_find:
            print (index) 
            break


with timer("linear Algorithm with find"):
    print(beasts.index(beast_to_find))


with timer("linear Algorithm with in"):
    print(beast_to_find in beasts)
