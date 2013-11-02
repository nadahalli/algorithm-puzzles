a = [3, 3, 2, 1, 2, 1, 1]
column_width = k = 6

def word_wrap(a, start, end, k):
    if start == end:
        return 0, None
    minimum = float('inf')
    mini = -1
    minsol = [[]]
    sum = 0
    for i in range(start, end):
        sum += a[i]
        if sum > k:
            break
        pre = (k - sum) * (k - sum)
        post, sol = word_wrap(a, i + 1, end, k)
        cost = pre + post
        if cost < minimum:
            minimum = cost
            mini = i
            minsol = sol
    sol = [a[start:mini + 1]]
    if minsol:
        sol.extend(minsol)
    return minimum, sol

print word_wrap(a, 0, len(a), k)
