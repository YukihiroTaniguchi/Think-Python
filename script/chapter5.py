#-*- coding: utf-8 -*-
import time
import turtle

def print_n(s, n):
    if n <= 0:
        return

    print(s)
    print_n(s, n-1)

print_n('test', 5)


def do_n(f, n):
    if n <= 0:
        return
    do_n(f, n-1)

print('-----5.14')
print('-----1')
proceeded_time = time.time()
a_sec = 1
a_min =  a_sec * 60
an_hour = a_min * 60
a_day = an_hour * 60
days = proceeded_time // a_day
now_hour = (proceeded_time - days * a_day) // an_hour
now_min = (proceeded_time - days * a_day - now_hour * an_hour) // a_min
now_sec = (proceeded_time - days * a_day - now_hour * an_hour - now_min * a_min) // a_sec
print(int(days), int(now_hour), int(now_min), int(now_sec))


print('-----2')

def check_fermat(a, b, c, n):
    fermat = a ** n + b ** n  == c ** n
    if n > 2 and fermat:
        print('おやまあ、フェルマーは間違ってる')
    else:
        print('だめだ、なりたたない')


def input_fermat():
    a = int(input('type first number\n'))
    b = int(input('type second number\n'))
    c = int(input('type third number\n'))
    n = int(input('type multiplication number\n'))
    check_fermat(a, b, c, n)

# input_fermat()

print('-----3')

def get_max(a, b, c):
    max = a
    if b >= max:
        max = b
    if c >= max:
        max = c
    return max

def get_min(a, b, c):
    min = a
    if b <= min:
        min = b
    if c <= min:
        min = c
    return min


def get_middle(a, b, c):
    min = get_min(a, b, c)
    max = get_max(a, b, c)
    middle = a
    if not(b == min or b == max):
        middle = b
    if not(c == min or c == max):
        middle = c
    return middle


def is_triangle(a, b, c):
    max = get_max(a, b, c)
    min = get_min(a, b, c)
    middle = get_middle(a, b, c)
    print("max : ",max)
    print("min : ",min)
    print("middle : ",middle)
    if(max <= min + middle):
        print('yes')
    else:
        print('no')

def check_triangle():
    a = int(input('type first number\n'))
    b = int(input('type second number\n'))
    c = int(input('type third number\n'))
    is_triangle(a, b, c)

# check_triangle()

print('-----4')

def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)

recurse(3, 0)

print('-----5')

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length * n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2 * angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length * n)

# bob = turtle.Turtle()
# draw(bob, 10, 10)

print('-----6')

def koch(turtle, n):
    if n<8:
        fd(turtle, n)
        return
    for angle in [-60, 120, -60, 0]:
        koch(turtle, n/3.0)
        rt(turtle, angle)

def snowflake(turtle):
    for i in range(3):
        koch(turtle, 300)
        rt(turtle, 120)

bob = turtle.Turtle()
bob.delay = 0
bob.pu()
bob.bk(150)
bob.lt()
bob.fd(90)
bob.rt()
bob.pd()
snowflake(bob)
