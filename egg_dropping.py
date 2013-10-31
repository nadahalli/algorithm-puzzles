neggs = 3
nfloors = 100

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
        min_diff = float('inf')
        for floor in range(nfloors):
            pre = find_floor(neggs - 1, floor)
            post = find_floor(neggs, nfloors - floor - 1)
            diff = pre - post if pre > post else post - pre
            if diff < min_diff:
                min_diff = diff
                ret_val = pre + 1
        memo[memo_key] = ret_val
    return ret_val 

print find_floor(neggs, nfloors)
                
        
            
            
                
