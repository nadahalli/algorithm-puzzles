from collections import defaultdict

a = [1, 2, 2, 2, 2, 2, 1, 3, 3, 1]
k = 2
n = len(a)
q = defaultdict(int)
i = j = 0
maxi = maxj = maxsum = currsum = 0

while j < n:
    if a[j] in q or len(q) < k:
        q[a[j]] += 1
        currsum += 1
        if currsum > maxsum:
            maxsum = currsum
            maxi = i
            maxj = j
        j += 1
    else:
        if q[a[i]] == 1:
            del q[a[i]]
        else:
            q[a[i]] -= 1
        i += 1
        currsum -= 1

print a
print a[maxi: maxj], maxsum



