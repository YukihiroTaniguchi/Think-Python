print('------8.3')
prefixes = 'JKLMNOPQ'
sufix = 'ack'

for letter in prefixes:
    sufix = 'ack'
    if letter == 'O' or letter == 'Q':
        sufix = 'uack'
    print(letter + sufix)

print('------8.6')
def find(word, letter, start):
    index = start
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1


print('find(\'banana\', \'a\', 2)',find('banana', 'a', 2))

print('------8.7')

def count(word, letter):
    count_num = 0
    for char in word:
        if char == letter:
            count_num =  count_num + 1
    return count_num

print('count(\'banana\', \'a\')', count('banana', 'a'))
