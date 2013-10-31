input = 'ABBABCBCABAAA'

def find_palindromic(a, i, j):
    if i == j - 1:
        return a[i]
    if i == j - 2:
        if a[i] == a[j - 1]:
            return a[i] + a[j - 1]
        else:
            return ''
    else:
        p1 = p2 = p3 = ''
        if a[i] == a[j - 1]:
            p1 = a[i] + find_palindromic(input, i + 1, j - 1) + a[j - 1]
        else:
            p2 = find_palindromic(input, i, j - 1)
            p3 = find_palindromic(input, i + 1, j)
        if len(p1) > len(p2) and len(p1) > len(p3):
            return p1
        elif len(p2) > len(p3):
            return p2
        else:
            return p3

print find_palindromic(input, 0, len(input))
    
