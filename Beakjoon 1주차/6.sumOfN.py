def solve(a:list) -> int:
    if not a or (len(a) > 3000000):
        return 0
    
    ans = 0

    for i in a:
        if not (0 <= i <= 1000000):
            return 0
        
        ans += i
    
    return ans