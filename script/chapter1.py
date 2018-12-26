print('------3.1')
def right_justify(sentence):
    spaces_num = 70 - len(sentence)
    return spaces_num * ' ' + sentence

def do_twice(f,sentence):
    f(sentence)
    f(sentence)

def print_twice(sentence):
    print(sentence)

do_twice(print_twice, 'func')
print('------3.2')
def do_four(f, sentence):
    do_twice(f, sentence)
    do_twice(f, sentence)

do_four(print_twice, 'func')



print('------3.3')
def window():
    col = '+ - - - - + - - - - +'
    row = '|         |         |'
    row_4 = row + '\n' + row + '\n' + row + '\n' + row

    print(col)
    print(row_4)
    print(col)
    print(row_4)
    print(col)

window()
