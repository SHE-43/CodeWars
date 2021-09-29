def last_survivor(letters, coords): 
    print(letters, coords)
    if len(letters) == 0 or len(coords) == 0:
        print(letters)
        return letters
    
    for x in coords:

        L = list(letters)
        del L[x]
        letters = "".join(L)

    print(letters)
    return letters

"""'abc', [1, 1]), 'a'"""

string = 'abc'

last_survivor(string, [])