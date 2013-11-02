n = 1729

i = 0

def sum_of_cubes(i, j):
    return (i * i * i) + (j * j * j)

while True:
    search = sum_of_cubes(i, i)
    if search == n:
        print i, i
        break
    elif search < n:
        i += 1
    else:
        found = False
        for j in range(i - 1, 1, -1):
            if sum_of_cubes(i, j) == n:
                print i, j
                found = True
                break 
        if not found:
            print 'No Answer'
        break
                
