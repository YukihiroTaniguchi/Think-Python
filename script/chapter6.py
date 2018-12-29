from math import sqrt

print('-----6.3')

def hypotenuse(x, y):
    sq_z = x ** 2 + y ** 2
    z = sqrt(sq_z)
    return z


hypo = hypotenuse(1, 2)
print('hypo is', hypo)


print('-----6.4')

def is_between(x, y, z):
    return (x <= y <= z)

if is_between(1, 2, 3):
    print('x <= y <= z')


print('-----6.11')
print('--------2')

def ack(m, n):
    if not (isinstance(m, int) and isinstance(n, int)):
        print('number are not int')
        return None
    if not(n >= 0 and m >= 0):
        print('number are not positive')
        return None

    if m == 0:
        return n + 1
    elif n == 0:
        return ack(m-1, 1)
    else:
        return ack(m-1, ack(m, n-1))


print('ack(3, 4) is', ack(3, 4))

print('--------4')

def is_power(a, b):
    if a == b:
        return True
    if a % b == 0 and is_power(a / b, b):
        return True
    return False


print('is_power(9, 3) is', is_power(9, 3))


print('--------5')

def gcd(a, b):
    if a % b == 0:
        return b
    gcd_num = gcd(b, a % b)
    return gcd_num

print('gcd(1649, 221)', gcd(1649, 221))
