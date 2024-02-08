import sys


def fib_DP(n: int, memo_fib: list[int]) -> int:
	if n < 2:
		memo_fib[n] = n
		return n

	if memo_fib[n] == 0:
		memo_fib[n] = fib_DP(n - 1, memo_fib) + fib_DP(n - 2, memo_fib)

	return memo_fib[n]


n = int(sys.stdin.readline())


memo_fib = [0 for _ in range(n + 1)]
print(fib_DP(n, memo_fib))