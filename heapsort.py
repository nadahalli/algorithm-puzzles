a = [1, 10, 15, 20]
b = [2, 3, 5, 10, 11, 14]
c = [100]
d = [10, 20, 30, 40, 50]
e = [1, 2, 3, 4, 5, 6, 7, 8]

arr = [a, b, c, d, e]

def heapify(arr, i, n):
    left = 2 * i
    right = 2 * i + 1
    large = None
    if left < n and arr[left] > arr[i]:
        large = left
    else:
        large = i
    if right < n and arr[right] > arr[large]:
        large = right

    if large != i:
        arr[i], arr[large] = arr[large], arr[i]
        heapify(arr, large, n)

x = [10, 11, 12, 2, 3, 4, 100, 120, 40]

def make_heap(arr):
    i = (len(arr) - 1) / 2
    while i >= 0:
        heapify(x, i, len(arr))
        i -= 1

def heap_sort(arr):
    make_heap(arr)
    for i in range(len(arr)):
        n = len(arr) - i - 1
        arr[0], arr[n] = arr[n], arr[0]
        heapify(arr, 0, n)

