from functools import reduce

# Reduce returns 0 if there is no element in the list for y when lambda x:y is used.
# When there is a list [1] used for lambda x:y, it will return 1.

def last_survivor(string, coords):
    return reduce(lambda str_,index_:f'{str_[0:index_]}{str_[index_ + 1:]}',[string]+coords)
    