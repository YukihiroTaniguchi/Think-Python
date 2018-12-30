import math
import copy

class Point(object):
    """Represents a point in 2-D space."""

def distance_between_points(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

class Rectangle(object):
    """Representes a rectangle

    attributes: width, height, corner
    """

def move_rectangle(rect, dx, dy):
    rect_cp = copy.deepcopy(rect)
    rect_cp.corner.x += dx
    rect_cp.corner.y += dy
    return rect_cp


class Circle(object):
    """
    attributes: center -> Point
               ,radius -> float
               """


def point_in_circle(cir, p):
    
