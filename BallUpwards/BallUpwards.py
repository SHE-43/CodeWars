# 2 solutions - first one belongs to me, and the next one is the best (most clever) solution available.

def max_ball(v) -> "Convert to m/s":
    t = 0; h = 0 
    while True:
        height = (((v * 1000) / 3600) * t) - (0.5 * 9.81 * t * t)
        if height < h:
            return round((t*10) - 1)
        t += 0.1; h = height

def max_ball_best(v0): # Most clever solution found on CodeWars
    return round(10*v0/9.81/3.6)