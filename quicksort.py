from itertools import chain

def hoare(a, p, q):
    x = a[p]
    i = p - 1
    j = q
    while True:
        while True:
            i += 1
            if a[i] >= x:
                break
                
        while True:
            j -= 1
            if a[j] <= x:
                break
        if i < j:
            a[i], a[j] = a[j], a[i]
        else:
            return j
def quick(a, p, r):
    if p < r:
        q = hoare(a, p, r)
        quick(a, p, q)
        quick(a, q + 1, r)
    
a = [10, 13, 12, 11, 10, 10, 10, 7, 8, 9, 1, 2]

quick(a, 0, len(a))

print a    
