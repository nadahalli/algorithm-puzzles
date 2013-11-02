a = [3, 10, 1, 2]

def choose(a, i, j, n, turn):
    if n == 2:
        if turn == 'me': 
            return max(a[i], a[j-1])
        else:
            return min(a[i], a[j-1])
    next_turn = 'him' if turn == 'me' else 'me'

    l = choose(a, i + 1, j, n - 1, next_turn)
    r = choose(a, i, j - 1, n - 1, next_turn)

    if turn == 'me':
        if l > r:
            return l + a[i]
        else:
            return r + a[j-1]
    else:
        return max(l, r)
        
        
print choose(a, 0, len(a), len(a), 'me')
