def mergesort(a, b, start, end):
    if start + 1 == end:
        return
    else:
        mid = (start + end)/2
    mergesort(a, b, start, mid)
    mergesort(a, b, mid, end)
    i = start
    j = mid
    k = start
    while i < mid and j < end:
        if a[i] < a[j]:
            b[k] = a[i]
            i += 1
        else:
            b[k] = a[j]
            j += 1
        k += 1
    if i == mid:
        tailstart = j
        tailend = end
    else:
        tailstart = i
        tailend = mid
    while tailstart < tailend:
        b[k] = a[tailstart]
        k += 1
        tailstart += 1
    for i in range(start, end):
        a[i] = b[i]
        
    
a = [10, 11, 8, 0, 1, 2, 9, 4]
b = [-1 for i in range(len(a))]
mergesort(a, b, 0, len(a))
print a
