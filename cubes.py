n = 1729

i = j = 1

def sum_of_cubes(i, j):
    return (i * i * i) + (j * j * j)

while True:
    answer = sum_of_cubes(i, j)
    if j == 1 and answer > n:
        print 'No anwer'
        break
    elif answer == n:
        print i, j
        break
    else:
        if j < i:
            j += 1
        else:
            j = 1
            i += 1
        
