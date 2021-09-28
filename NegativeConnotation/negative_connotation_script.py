# make using basic method
# make using decorator
# make using class

# string with a set of characters and separated by spaces.

# way 1 using lists and dicts
# optimized implicit way
# optimized explicit way
# recursive decorator please. DO THE CALC and then use decorator to return
# Using odd or even


def connotation(string):

    first = {x:1 for x in "abcdefghijklm"}
    last = {x:-1 for x in "nopqrstuvwxyz"}
    letter_value_ = lambda x : first.get(x, 0) + last.get(x, 0)

    total = sum (
        [
            letter_value_(word[0].lower()) 
            if len(word) != 0 else 0 
            for word in string.split(" ") 
            if len(string) != 0
        ]
                )
    return True if total >= 0 else False
    
