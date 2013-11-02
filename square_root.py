def square_root(s):
    i = 1
    j = s
    while (abs(j - i) > 0.001):
        print i, j
        i = (i + j) / 2.0
        j = s * 1.0/i
    return i

print square_root(100)
