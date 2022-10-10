import math

from shapes.Shape import Shape
from shapes.Trajectory import Trajectory
from shapes.Point import Point

class Line(Trajectory, Shape):
    def __init__(self, x1, y1, x2, y2):
        self.p1 = Point(x1, y1)
        self.p2 = Point(x2, y2)
        self.distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        self.distance_x = abs(self.p1.x - self.p2.x)
        self.distance_y = abs(self.p1.y - self.p2.y)

        self.m = self.dy() / self.dx() if self.p1.x != self.p2.x else None
        self.b = self.p1.y - self.m * self.p1.x

    def min_x(self): return min(self.p1.x, self.p2.x)
    def min_y(self): return min(self.p1.y, self.p2.y)
    def max_x(self): return max(self.p1.x, self.p2.x)
    def max_y(self): return max(self.p1.y, self.p2.y)

    def dx(self): return self.p2.x - self.p1.x
    def dy(self): return self.p2.y - self.p1.y

    def eqation(self, x):
        return self.m * x + self.b

    def animator(self, step, direction=1):
        step = abs(step)
        p1 = self.p1
        p2 = self.p2
        if direction < 0:
             p1, p2 = p2, p1

        ratio = step / self.distance
        xstep = ratio * self.distance_x
        ystep = ratio * self.distance_y

        if p1.x > p2.x: xstep *= -1
        if p1.y > p2.y: ystep *= -1

        x, y = p1.x, p1.y
        dist_left = self.distance
        yield x, y
        while dist_left > step:
            x += xstep
            y += ystep
            dist_left -= step
            yield x, y

        if x != self.p2.x:
            yield self.p2.x, self.p2.y




