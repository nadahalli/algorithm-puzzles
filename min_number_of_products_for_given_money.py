products = [1, 2, 3, 4]
cost = 6

memoized = {}
def find_min(products, cost):
    memo_key = (len(products), cost)
    value = memoized.get(memo_key)
    if value:
        return value
    ret_val = float('inf')
    if cost == 0:
        ret_val = 0
    elif cost < 0:
        ret_val = float('inf')
    else:
        min_found = float('inf')
        for i in range(len(products)):
            restofem = products[i + 1:]
            sol_restofem = find_min(restofem, cost - products[i])
            if sol_restofem == float('inf'):
                continue
            if sol_restofem + 1 < min_found:
                min_found = sol_restofem + 1
        ret_val = min_found
    memoized[memo_key] = ret_val
    return ret_val

print find_min(products, cost)

