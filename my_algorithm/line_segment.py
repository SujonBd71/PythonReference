

#cross prodict of p0p1 and p0p2 tells in which direction p1 is from p2
#if pos : p1 is clockwise from p2

# we can use the concecpt to check segment p1p2 and p3p4
#need to check 4 directions 
#p3 from p1p2 and p4 from p1p2 
#p1 from p3p4 and p2 from p3p4

class Line():

    class Point():
        def __init__(self, x, y):
            self.x = x
            self.y = y

    def __init__(self, x1,y1, x2,y2):
        self.p1 = Line.Point(x1, y1)
        self.p2 = Line.Point(x2, y2)


    # get direction of point Pk from line Segment PiPj
    #which is done by
    #  d = PiPk X PiPk
    #  
      
    # basic cros product
    # p1 X p2 = |x1, y1 |
    #           |x2, y2 | 

    #       = x1y2 - x2y1
    
    # (p1 - p0) * (p2 - p0) =  (x1 - x0) * (y2-y0) - (x2- x0) * (y1-y0)
    #
    # PiPk X PiPj =  [Xj, Yj ]
    #              = [Xk, Yk]


def  is_colinear(Pi, Pj, Pk):
    x_range =  (Pk.x >= min(Pi.x, Pj.x)) and (Pk.x <= max(Pj.x, Pi.x)) 
    y_range =  (Pk.y >= min(Pi.y, Pj.y)) and (Pk.y <= max(Pi.y, Pj.y))
    return x_range and y_range

def get_dir(Pi, Pj, Pk):
    return (Pj.x - Pi.x) * (Pk.y - Pi.y) - (Pk.x - Pi.x) * (Pj.y - Pi.y)

def does_line_interseact(line1, line2):
    d1 = get_dir(line1.p1, line1.p2, line2.p1)
    d2 = get_dir(line1.p1, line1.p2, line2.p2)

    d3 = get_dir(line2.p1, line2.p2, line1.p1)
    d4 = get_dir(line2.p1, line2.p2, line1.p2)

    # ideal case intersection
    if ( ( d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0) ) and  ( ( d3 > 0 and d4 < 0) or (d3 < 0 and d4 > 0) ):
        return True

    if d1 == 0 and   is_colinear(line1.p1, line1.p2, line2.p1):
        return True
    elif d2 == 0 and is_colinear(line1.p1, line1.p2, line2.p2):
        return True
    elif d3 == 0 and is_colinear(line2.p1, line2.p2, line1.p1):
        return True
    elif d4 == 0 and is_colinear(line2.p1, line2.p2, line1.p2):
        return True

    return False


def Test():
    line1 = Line(2,2, 5, 5) 
    line2 = Line(4,3, 4, 5) 
    res = does_line_interseact(line1, line2)
    print(res)

    line1 = Line(1,1, 10, 1) 
    line2 = Line(1,2, 10, 2) 
    res = does_line_interseact(line1, line2)
    print(res)

    line1 = Line(10,0, 0, 10) 
    line2 = Line(0,0, 10, 10) 
    res = does_line_interseact(line1, line2)
    print(res)

    line1 = Line(-5,-5, 0, 0) 
    line2 = Line(1,1, 10, 10) 
    res = does_line_interseact(line1, line2)
    print(res)

Test()
