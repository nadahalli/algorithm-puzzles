from collections import deque

memo = {}

def find_floor(neggs, nfloors):
    memo_key = (neggs, nfloors)
    value = memo.get(memo_key)
    if value:
        return value
    if neggs == 1:
        ret_val = nfloors
    elif nfloors == 0:
        ret_val = 0
    else:
        minmax = float('inf')
        for floor in range(nfloors):
            pre = find_floor(neggs - 1, floor)
            post = find_floor(neggs, nfloors - floor - 1)
            min_canidate = max(pre, post)
            if min_canidate < minmax:
                minmax = min_canidate
        ret_val = minmax + 1
        memo[memo_key] = ret_val
    return ret_val 

neggs = 2
nfloors = 100
print find_floor(neggs, nfloors)
                
        
            
            
                
