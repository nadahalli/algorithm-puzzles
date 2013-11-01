from collections import deque

def factorial(n):
    stack = deque()
    stack.appendleft(n)
    fact = 1
    while len(stack):
        i = stack.popleft()
        if i == 0:
            fact *= 1
            break
        fact *= i
        stack.appendleft(i - 1)
    return fact

print factorial(5)

def binsearch(a, i, j, x):
    stack = deque()
    stack.appendleft((i, j))
    while len(stack):
        i, j = stack.popleft()
        if i >= j:
            return -1
        mid = (i + j) / 2
        if a[mid] == x:
            return mid
        if x > a[mid]:
            stack.appendleft((mid + 1, j))
        else:
            stack.appendleft((i, mid))

a = [1, 2, 3, 4, 5, 6, 7, 8]
print binsearch(a, 0, len(a), 10)
    
