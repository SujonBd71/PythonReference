
#https://www.sanfoundry.com/cpp-program-implement-graham-scan-algorithm-find-convex-hull/
from operator import itemgetter, attrgetter

def cmp_to_key(mycmp):
    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
    return K

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return ("({0},{1})".format(self.x, self.y))

def find_convex_hull(points):    
    start = points[0]
    def distance(p1):
        p0 = start
        d = (p0.x - p1.x) * (p0.x - p1.x) 
        d = d + (p0.y - p1.y) * (p0.y - p1.y) 
        return d
    
    #get direction of p2 from PoP1
    # can be find from cross prdct of PoP2 X PoP1
    def get_dir(p0, p1, p2):
        #is p2 anti-clockwise form p1
        #  
        #  PoP2 X PoP1=  [ p2.x - p0.x  p2.y - p0.y]
        #                [ p1.x - p0.x  p1.y - po.y]

        mag1 = (p2.x - p0.x) * (p1.y - p0.y) 
        mag2 = (p1.x - p0.x) * (p2.y - p0.y)
        return mag1 - mag2

    def my_cmp(p1, p2):
        dir = get_dir(start, p1, p2)
        if dir != 0:
            return dir
        return distance(p1) - distance(p2)
        
    minp = min(points, key=attrgetter("y"))
    min_index = points.index(minp)

    points[0], points[min_index] = points[min_index], points[0]
    start = points[0]
    points.sort(key=cmp_to_key(my_cmp))
   
    # iterate all points
    stk = []
    stk.append(points[0])
    stk.append(points[1])
    stk.append(points[2])

    n = len(points)
    for i in range(3, n):
        p2 = points[i]
        while (len(stk) > 0):
            p1 = stk[-1]
            p0 = stk[-2]
            dir = get_dir(p0,p1, p2)
            if (dir > 0):
                stk.pop()
            else:
                stk.append(p2)
                break

    print("\nConvex Hull:")
    for p in stk:
        print(p)


def Test():

    def make_points_and_test(pl):
        points = []
        for p in pl:
            points.append(Point(p[0], p[1]))
        find_convex_hull(points)


    pl = [ [ 0, 3 ], [ 1, 1 ], [ 2, 2 ], [ 4, 4 ], [ 0, 0 ],
           [ 1, 2 ], [ 3, 1 ], [ 3, 3 ] ]
    make_points_and_test(pl)

    pl = [[0, 0], [1, 1], [2, 2], [3, -1]]
    make_points_and_test(pl)

    pl = [[16,3], [12,17], [0,6], [-4,-6], [16,6], [16,-7], [16,-3], [17,-4], [5,19], 
    [19,-8], [3,16], [12,13], [3,-4], [17,5], [-3,15], [-3,-9], [0,11], [-9,-3], [-4,-2], 
    [12,10]]

    make_points_and_test(pl)
    

Test()