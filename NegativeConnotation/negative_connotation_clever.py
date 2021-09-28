# these are the solutions made by others - considered the best possible solutions.


def connotation_1(s):
    # As Python can equate to alphabets.
    # A list of booleans can be considered 1s and 0s therefore a sum can be done.
    # The length of list is divided by 2 and then the sum compared.
    lst = s.upper().split()
    return sum('A'<=w[0]<='M' for w in lst) >= len(lst)/2

def connotation_2(s):
    return sum(1 if w[0] <= 'm' else -1 for w in s.lower().split()) >= 0