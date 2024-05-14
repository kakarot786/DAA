def euclid(x,y):
    if x < y:
        x, y = y, x
    if y == 0:
        return x
    else:
        return euclid(y, x % y)