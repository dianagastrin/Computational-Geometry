'''
Implementation of the pseudocode from [Page Number 3::Chapter 1::Section 1.1]
of "Computational Geometry" book by Mark de Berg, Otfried Cheong, Marc van Kreveld,
Mark Overmars
By Diana Gastrin \\ gastrindiana@gmail.com
'''
class Point:
    def __init__(cls, x, y):
        cls.x = x
        cls.y = y
    
    def __str__(cls):
        return "(" +  str(cls.x) +", " + str(cls.y) + ")"
    
class Line:
    def __init__(cls, p1, p2):
        cls.p1 = p1
        cls.p2 = p2

    def __radd__(self, other):
            return other + (self.p1 , self.p2)

    @staticmethod
    def cross_product(a, b):
        p = a.p1
        p1 = a.p2
        p2 = b.p2
        return  (p.y - p2.y) * (p.x - p1.x) - (p.y - p1.y) * (p.x - p2.x)   

def turn_right(pts):
    p1, p2, p3 = pts
    l1 = Line(p2, p1)
    l2 = Line(p2, p3)
    return Line.cross_product(l1, l2) < 0

def iter(p):
    l_ul = p[0:2]
    
    for p in p[2:]:
        l_ul.append(p)
        while(len(l_ul)>2 and not turn_right(l_ul[-3:])):
            ind =  int(len(l_ul)/2)
            l_ul = l_ul[0:ind] + l_ul[ind+1:] # remove the middle
    return l_ul

def convex_hull(P):
    # sort by x-coordinate
    sorted_p = sorted(P, key=lambda p: p.x)
    reverse_sorted_p = sorted_p[::-1]
    l_upper = iter(sorted_p)
    l_lower = iter(reverse_sorted_p)
    l_lower = l_lower[1:]
    l_lower = l_lower[:-1]
    return l_lower + l_upper

'''
Test
'''

import matplotlib.pyplot as plt
import numpy as np
from operator import itemgetter, attrgetter, methodcaller

pts = [Point(3,4), Point(5,6), Point(2.5, 4), Point(4,2), Point(4.5, 5)]

P = convex_hull(pts)

x_ch = [p.x for p in P] + [P[0].x]
y_ch = [p.y for p in P] + [P[0].y]

x= [p.x for p in pts]
y = [p.y for p in pts]

plt.plot(x_ch, y_ch, "--", label="convexHull")
plt.plot(x,y, "ro", label="all pts")
plt.grid()
plt.legend()
plt.show()