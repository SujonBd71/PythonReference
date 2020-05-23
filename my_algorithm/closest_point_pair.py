
#to test with online judge set
#https://www.urionlinejudge.com.br/judge/problems/view/1295

#references
#https://algs4.cs.princeton.edu/99hull/ClosestPair.java.html

import sys
from operator import itemgetter, attrgetter
import math
from datetime import datetime


def dist(p1, p2):
    d= math.pow(p1[0] - p2[0], 2)
    d = d +  math.pow(p1[1] - p2[1], 2)
    return math.sqrt(d)

def closest_point_naive(points):
    n = len(points)
    mn = sys.maxsize >> 1
    for i in range(0, n-1):
        for j in range(i+1, n):
            mn = min(mn, dist(points[i], points[j]))
    return mn

def closest_point_opt(points):
    xp = sorted(points, key = itemgetter(0))
    yp = sorted(points, key = itemgetter(1))

    def find_closest_point(xp, yp):
        n = len(xp)
        if (n <= 1):
            return sys.maxsize
        if (n == 2):
            return dist(xp[0], xp[1])
        
        m = (len(xp) - 1) >> 1
        xl = xp[0:m+1]
        xr = xp[m+1:]
        yl = []
        yr = []

        for p in yp:
            if p[0] <= xp[m][0]:
                yl.append(p)
            else:
                yr.append(p)
        
        dl = find_closest_point(xl, yl)
        dr = find_closest_point(xr,yr)
        d = min(dl, dr)

        mid_points = []
        for p in yp:
            if (abs (xp[m][0] - p[0]) < d):
                mid_points.append(p)

        total = len(mid_points)
        for i in range(total-1):
            for j in range(i+1, min(i + 9, total)):
                cur = dist(mid_points[j], mid_points[i])
                d = min(d, cur)
        
        return d

    start = datetime.now()
    min_dist = closest_point_naive(points)
    t_delta = datetime.now() - start
    print('Time: ', t_delta.total_seconds())
    print(min_dist)

    start = datetime.now()
    min_dist = find_closest_point(xp, yp)
    t_delta = datetime.now() - start
    print('Time: ', t_delta.total_seconds())
    print(min_dist)


def Test():
    import random
    points = [ [random.randrange(-25000,25000), random.randrange(-25000,25000)] 
            for i in range(1000) ]

    # print(points)
    closest_point_opt(points)

Test()
