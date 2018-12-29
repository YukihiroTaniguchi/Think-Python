def nested_sum(l):
    sum_l = 0
    for item in l:
        for num in item:
            sum_l += num
    return sum_l

def cumsum(l):
    cumsum_l = []
    for i in range(len(l)):
        cumsum_l.append(sum(l[:i + 1]))
    return cumsum_l

def middle(l):
    middle_l = l[1:-1]
    return middle_l

def chop(l):
    del l[0]
    del l[-1]

def is_sorted(l):
    l_2 = l[:]
    l_2.sort()
    if l == l_2:
        return True
    return False
