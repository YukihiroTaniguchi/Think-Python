print('----13.2')

import random

for I in range(10):
    x = random.random()
    print(x)

print(random.randint(5, 10))

print('----13.5')

def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d
