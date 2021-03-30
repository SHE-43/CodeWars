def fortune(f0, p, c0, n, i):
    data = [[] for x in range(n)]     
    data[0] = [f0, c0]  
    for j in range(1, n):
        f = data[j-1][0] * (1 + p / 100) - data[j-1][1]
        c = data[j-1][1] * (1 + i / 100)
        data[j] = [f,c]
        if f < 0:
            return False        
    return True
