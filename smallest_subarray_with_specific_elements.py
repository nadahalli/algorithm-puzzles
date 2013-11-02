from collections import defaultdict

a = [1, 3, 1, 1, 2, 10, 2, 4, 3, 4, 5]
elems = set([3, 10, 2])

found = defaultdict(int)

i = j = mini = minj = 0

def findmin(mini, minj, i, j):
    if j - i < minj - mini:
        minj = j
        mini = i
    return mini, minj

while len(elems) - len(found) > 0:
    if a[j] in elems:
        found[a[j]] += 1
    j += 1

mini, minj = i, j

while j < len(a):
    if a[j] in elems:
        found[a[j]] += 1
    j += 1    
    while True:
        if a[i] in found:
            if found[a[i]] == 1:
                break
            else:
                found[a[i]] -= 1
        i += 1        
    mini, minj = findmin(mini, minj, i, j)

print mini, minj
print a[mini:minj]
        
    
    
