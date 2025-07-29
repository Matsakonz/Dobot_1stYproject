pi = 3.14
def circ_area(pi,radius):
    if radius > 0:
        return pi*radius**2
    else:
        return -321
    
assert circ_area(pi,5) == 78.5
assert circ_area(pi,2) == 12.56