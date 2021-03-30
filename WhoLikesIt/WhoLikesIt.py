'''
'likes' is the most efficient algorithm made to solve such a problem and this is done via taking help
    of another Warrior from CodeWars,

'likes1', however is my first attempt EVER for this question from 2 years ago. 
Please don't do what I did 2 years ago!


tests for both methods are available in the next file
'''

def likes(names):
    number_of_names = len(names)
    d = {
        0 : 'no one likes this',
        1 : '{} likes this',
        2 : '{} and {} like this',
        3 : '{}, {} and {} like this',
        4 : '{}, {} and {remaining} others like this'  
        }

    sentence = d[min(4,number_of_names)]
    sentence_formatting = sentence.format(*names[:3], remaining = number_of_names-2)
    return sentence_formatting

def likes1(sec):
    while None in sec:
        sec.remove(None)    
    if sec == []:
        return "no one likes this"    
    for x in sec:
        if len(sec) == 1:
            return x + " likes this"
        elif len(sec) == 2:
            return sec[0] +" and "+ sec[1]+ " like this"
        elif len(sec) == 3:
            return sec[0]+ ", "+ sec[1] + " and " + sec[2] + " like this"
        elif len(sec) >= 4:
            return sec[0]+ ", "+ sec[1] + " and " + (str(len(sec[2:]))) + " others like this"

