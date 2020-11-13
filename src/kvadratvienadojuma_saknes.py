import math
def kvadratvienadojums(a,b,c):
    if a==0 and b==0:
        return None
    
    if a==0:
        return b/c
    
    diskrim = b ** 2 + 4 * a * c
    saknes=[]
    if diskrim>0:
        saknes1 = (0-b+math.sqrt(diskrim))/(2*a)
        saknes2 = (0-b-math.sqrt(diskrim))/(2*a)
        saknes = [saknes1, saknes2]

    elif diskrim == 0:
        saknes1 = (0-b)/(2*a)
        saknes = [saknes1]
    
    else:
        saknes = None

    return saknes


