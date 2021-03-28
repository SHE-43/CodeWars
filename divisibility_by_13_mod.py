'''

Author: hMak

Upload on GitHub
New folder - Level 6 Codewars

6 kyu
A Rule of Divisibility by 13


'''
def thirt(a):
    list_1 = [a]
    b= 1
    while b == 1:    
        list_1.append(
            sum([(int(letter) * ((10 ** power) % 13)) 
                    for power, letter in enumerate(str(list_1[-1])[-1::-1])]))   
        if list_1[-1] == list_1[-2]:
            return list_1[-1]

    
print(thirt(1234567))


    




