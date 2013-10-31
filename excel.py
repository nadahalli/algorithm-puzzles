_map = {
    0: 'A',
    1: 'B',
    2: 'C',
}

siz = len(_map)

def convert(i):
    ret = []
    while (i > 0):
        i = i - 1
        r = i % siz
        ret.append(_map[r])
        i = i/siz
    ret.reverse()
    return ''.join(ret)


for i in range(1, 20):
    print convert(i)
    #print '-' * 10
