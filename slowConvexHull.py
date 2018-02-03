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

    def contain(cls, p):
        return cls.p1 == p or cls.p1 == p

    def __str__(cls):
        return str(cls.p1) + "->" + str(cls.p2)

def possible_lines(P):
    return [Line(p,q) for q in P for p in P if p != q]
    
def slow_convex_hull(P):
    E = list()

    for line in possible_lines(P):
        valid = True
        for p in P:
            if not line.contain(p):
                tmp_line = Line(line.p1, p)
                if Line.cross_product(line, tmp_line) > 0:
                    valid = False
        if valid:
            E.append(line)

    return E

def construct_convex_hull(E):
    output = []
    for line in E:
        for line2 in E :
            if line != line2 and line.p2 == line2.p1:
                output.append(line)
                E.remove(line)
    return output + E

'''
Test
'''
import matplotlib.pyplot as plt
import numpy as np

pts = [Point(3,4), Point(5,6), Point(2.5, 4), Point(4,2), Point(4.5, 5)]

E = slow_convex_hull(pts)
L_EDGS = construct_convex_hull(E)
L_PTS = list(sum(L_EDGS, ()))

x_ch = [p.x for p in L_PTS]
y_ch = [p.y for p in L_PTS]

x= [p.x for p in pts]
y = [p.y for p in pts]

plt.plot(x_ch, y_ch, "--", label="convexHull")
plt.plot(x,y, "ro", label="all pts")
plt.grid()
plt.legend()
plt.show()