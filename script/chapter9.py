print('------9.2')
print('--------1')

def over_20_char(dir):
    fin = open(dir)
    for line in fin:
        word = fin.readline()
        if len(word) > 20:
            print(word)

dir = 'others/words.txt'
# over_20_char(dir)

print('--------2')

def has_no_e(str):
    if 'e' in str:
        return True
    return False

def get_percentage_no_e(dir):
    fin = open(dir)
    count = 0
    num_lines = sum(1 for line_1 in open(dir))
    for line in fin:
        word = fin.readline()
        if not has_no_e(word):
            print(word)
            count = count + 1
    return count / num_lines *100

# print('get_percentage_no_e(dir)',get_percentage_no_e(dir), '%')

print('------9.7')
print('--------7')

def get_2_3(word):
    count = 0
    for i in range(0, len(word) - 1, 2):
        if word[i] == word[i+1] :
            count = count + 1
    if count == 3:
        return True
    return False


def cartalk1(dir):
    fin = open(dir)
    list2_3 = []
    for line in fin:
        word = fin.readline()
        if get_2_3(word):
            list2_3.append(word)
    return list2_3

print('cartalk1(dir)', cartalk1(dir))
