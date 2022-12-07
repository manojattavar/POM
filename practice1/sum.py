l = [1, 2, 3, 4]

def sum1(l):
    if len(l) == 1:
        return l[0]
    else:
        return sum(l[1:])

print(sum1(l))