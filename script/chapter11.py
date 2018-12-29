from pprint import pprint

def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d

print('histogram(\'brontosaurus\')', histogram('brontosaurus'))

known = {0:0, 1:1}

def fibonacci(n):
    if n in known:
        return known[n]
    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res

print('fibonacci(100)', fibonacci(100))

print('----11.10')
print('--------1')

words_dict = dict()
words_dir = 'others/words.txt'
def create_words_dict(dir):
    fin = open(dir)
    for line in fin:
        word = line.strip()
        words_dict[word] = 0
    print('finish')


create_words_dict(words_dir)

def check_dict(word):
    if words_dict.get(word, 1) == 0:
        return True
    return False

print('check_dict(\'test\')', check_dict('test'))
