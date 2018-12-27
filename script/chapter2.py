import turtle
from numpy import pi

print('-----4.3')
print('------1')



def square(t, length):
    for i in range(4):
        t.fd(length)
        t.rt(90)


def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.rt(angle)

def circle(t, r):
    length = 2 * pi * r
    n = 50
    polygon(t, n, length)

def arc(t, angle):
    r = 30
    n = int(50 * angle / 360)
    length = 2 * pi * r
    for i in range(n):
        t.fd(length / n)
        t.rt(angle/n)

bob = turtle.Turtle()
print(bob)
arc(bob, 270)
