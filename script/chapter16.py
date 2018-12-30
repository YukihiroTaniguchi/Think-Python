class Point(object):
    """Represents a point in 2-D space."""

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%d, %d)" % (self.x, self.y)

    def __add__(self, other):
        if isinstance(other, Point):
            return self.add_point(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        return self.__add__(other)

    def add_point(self, other):
        p = Point(self.x + other.x, self.y + other.y)
        return p

    def increment(self, arr_t):
        p = Point(self.x + arr_t[0], self.y + arr_t[1])
        return p

class Time(object):
    """Represents the time fo dayself.

    attributes: hour, munute, secod
    """
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def print_time(self):
        print("%.2d:%.2d:%.2d" % (self.hour, self.minute, self.second))

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

def print_attributes(obj):
    for attr in vars(obj):
        print(attr, getattr(obj, attr))
