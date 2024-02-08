import sys
sys.setrecursionlimit(10**6)

# def fib_Tile(n: int, memo_fib: list[str]) -> list[str]:
# 	if n == 1:
# 		memo_fib[n] = ["1"]
# 		return ["1"]
	
# 	elif n == 2:
# 		memo_fib[n] = ["11", "00"]
# 		return ["11", "00"]
	
# 	else: 
# 		memo_fib[n] = [i + "1" for i in fib_Tile(n - 1, memo_fib)] + [i + "00" for i in fib_Tile(n - 2, memo_fib)]

# 	return memo_fib[n]


def fib_Tile(n: int, memo_fib: list[str]) -> int:
    if n >= 3:
        memo_fib[n % 3] = fib_Tile(n - 1, memo_fib) + fib_Tile(n - 2, memo_fib) % 15746
    
    return memo_fib[n % 3]


def fib_Tile(n: int, memo_fib: list[str]) -> int:
    memo_fib[1] = 1
    memo_fib[2] = 2
	
    for i in range(3, n + 1):
        memo_fib[i % 3] = (memo_fib[(i - 1) % 3] + memo_fib[(i - 2) % 3]) % 15746
    
    return memo_fib[n % 3]


if __name__ == "__main__":
	
	n = int(sys.stdin.readline())
	memo_fib = [0] * 3
	print(fib_Tile(n, memo_fib))