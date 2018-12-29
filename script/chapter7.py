import math
print('------7.3')

def print_n(s, n):
    while n > 0:
        print(s)
        n = n - 1

print_n('test', 3)

print('------7.9')
print('--------1')

def mysqrt (a):
    x = a / 2.0
    epsilon = 0.001
    while True:
        y = (x + a/x) / 2.0
        if abs(y - x) < epsilon:
            break
        x = y
    return x

print('mysqrt(3)',mysqrt(3))

def test_square_root(n):
    print('a', 'mysqrt(a)' ,'math.sqrt(a)', 'diff')
    print('-', '---------' ,'------------', '----')

    for i in range(1, n + 1):
        mysqrt_i = mysqrt(i)
        math_sqrt_i = math.sqrt(i)
        diff = abs(mysqrt_i- math_sqrt_i)
        print(i, mysqrt_i, math_sqrt_i, diff)

test_square_root(10)


print('--------2')
def eval_loop():
    while True:
        ans = 0
        str = input('> ')
        if str == 'done':
            return ans
        ans = eval(str)
        print('>',ans)

answer = eval_loop()
